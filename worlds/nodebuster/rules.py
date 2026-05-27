from dataclasses import dataclass
from typing import TYPE_CHECKING, NamedTuple
from BaseClasses import CollectionState
from rule_builder.rules import *
from Utils import visualize_regions
from .Options import BossDrops, Goal
from .items import progressive_item_to_vanilla, progressive_item_map, get_power_from_vanilla_items, get_power_from_progressive_item
from .regions import nodebuster_regions_all

if TYPE_CHECKING:
    from . import NodebusterWorld, nodebuster_regions_all
else:
    NodebusterWorld = object


def reached_location(location: str, world: NodebusterWorld, state: CollectionState, player: int) -> bool:
    result = False
    try:
        loc = world.get_location(location)
        result = loc in state.locations_checked
    except KeyError:
        pass
    return result

boss_mode_off = OptionFilter(BossDrops, False)
infinity_mode_off = OptionFilter(Goal, Goal.option_release_virus)
has_crypto_mine = Has("CryptoMine")
has_access_to_blue_enemies = HasAny("NodeFinder1", "Progressive Blue Spawn")
has_milestones_upgrade = Has("Milestones")
has_access_to_net_and_nodes = has_crypto_mine & has_access_to_blue_enemies
has_access_to_yellow_enemies = HasAny("YellowSpawn1", "YellowSpawn2", "Progressive Yellow Spawn")
has_critical_damage = Has("CritChance1") & HasAny("CritDamage1", "CritDamage2", "Progressive Critical Damage")

def has_number_of_upgrades_per_category(world: NodebusterWorld, state: CollectionState, player: int, group: str, count: int) -> bool:
    vanilla_damage_reqs = progressive_item_to_vanilla(group, count)
    items_list = list(progressive_item_map[group].keys())
    return (
            state.has_all_counts(vanilla_damage_reqs, player)
            or state.has(group, player, count)
            or state.count_from_list(items_list, player) >= count
    )

class ProgItemMapping(NamedTuple):
    count: int
    power: int

additional_damage: list = ["DamagePerEnemy1", "Undamaged1", "Execute1", "Undamaged2", "Execute2", "MaxHealthToDamage1"]
regen: list = ["HealthRegen1", "HealthRegen2", "DropHeal1", "MaxHealthHeal1", "StealMaxHealth1", "MaxHealthHeal2", "StealMaxHealth2", "StealMaxHealth3"]
armor: list = ["Armor1", "Armor2", "ArmorPerEnemy1", "Armor3", "Armor4", "Armor5", "Armor6", "MaxHealthToArmor1", "Armor7", "FocusArmor1", "MaxHealthToArmor2", "RampingArmor1"]
progressive_item_map: dict[str, list[ProgItemMapping]] = {

    "Progressive Damage": [
        ProgItemMapping(15, 1),
        ProgItemMapping(10, 3),
        ProgItemMapping(10, 6),
        ProgItemMapping(3, 25),
        ProgItemMapping(5, 100),
    ],

    "Progressive Additional Damage": [
        ProgItemMapping(5, 1),
        ProgItemMapping(6, 1),
        ProgItemMapping(6, 1),
        ProgItemMapping(4, 1),
        ProgItemMapping(4, 1),
        ProgItemMapping(1, 1),
    ],

    "Progressive Damage Per Second": [
        ProgItemMapping(3, 1),
    ],

    "Progressive Critical Damage": [
        ProgItemMapping(10, 50),
        ProgItemMapping(8, 200),
    ],

    "Progressive Boss Damage": [
        ProgItemMapping(10, 50),
        ProgItemMapping(10, 100),
    ],

    "Progressive Health": [
        ProgItemMapping(10, 4),
        ProgItemMapping(8, 12),
        ProgItemMapping(10, 80),
        ProgItemMapping(10, 300),
        ProgItemMapping(3, 4000),
        ProgItemMapping(5, 50000),
        ProgItemMapping(5, 100000),
    ],

    "Progressive Regen": [
        ProgItemMapping(5, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(10, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(5, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
    ],

    "Progressive Lifesteal": [
        ProgItemMapping(5, 1),     #max solo/cm pow= 5/5
        ProgItemMapping(5, 50),    #max solo/cm pow= 250/255
        ProgItemMapping(1, 8),    #max solo/cm pow= 8/263
        ProgItemMapping(3, 1000), #max solo/cm pow= 3000/3263
        ProgItemMapping(2, 5000), #max solo/cm pow= 10000/13263
    ],

    "Progressive SpawnRate": [
        ProgItemMapping(15, 50),  #max solo/cm pow= 750/750
        ProgItemMapping(1, 200), #max solo/cm pow= 200/950
        ProgItemMapping(5, 100), #max solo/cm pow= 500/1450
        ProgItemMapping(5, 400), #max solo/cm pow= 2000/3450
    ],

    "Progressive Blue Spawn": [
        ProgItemMapping(5, 1),
    ],

    "Progressive Yellow Spawn": [
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
    ],

    "Progressive Armor": [
        ProgItemMapping(10, 1),
        ProgItemMapping(5, 1),
        ProgItemMapping(10, 1),
        ProgItemMapping(10, 1),
        ProgItemMapping(10, 1),
        ProgItemMapping(20, 1),
        ProgItemMapping(30, 1),
        ProgItemMapping(5, 1),
        ProgItemMapping(5, 1),
        ProgItemMapping(5, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(5, 1),
    ],

    "Progressive Boss Armor": [
        ProgItemMapping(10, 1),
        ProgItemMapping(8, 25),
    ],

    "Progressive Infinity": [
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
    ],

    "Progressive Red Milestone Reward": [
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
    ],

    "Progressive Blue Milestone Reward": [
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
    ],

    "Progressive Yellow Milestone Reward": [
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1),
        ProgItemMapping(1, 1)
    ],
}

DAMAGE_POWER: dict[str, int] = {
    "Damage1": 1,
    "Damage2": 3,
    "Damage3": 6,
    "Damage4": 25,
    "Damage5": 100,
}

BOSS_DAMAGE_POWER: dict[str, int] = {
    "BossDamage1": 50,
    "BossDamage2": 100,
}

HEALTH_POWER: dict[str, int] = {
    "Health1": 4,
    "Health2": 12,
    "Health3": 80,
    "Health4": 300,
    "Health5": 4000,
    "Health6": 50000,
    "Health7": 100000,
}

LIFESTEAL_POWER: dict[str, int] = {
    "Salvaging1": 1,
    "Lifesteal1": 50,
    "Salvaging2": 8,
    "Lifesteal2": 1000,
    "Lifesteal3": 5000,
}

BOSS_ARMOR_POWER: dict[str, int] = {
    "BossArmor1": 1,
    "BossArmor2": 25,
}

CRIT_DAMAGE_POWER: dict[str, int] = {
    "CritDamage1": 50,
    "CritDamage2": 200,
}

SPAWN_RATE_POWER: dict[str, int] = {
    "SpawnRate1": 50,
    "SpawnRate2": 200,
    "SpawnRate3": 100,
    "SpawnRate4": 500,
}

@dataclass()
class DamagePowerRule(Rule[NodebusterWorld], game="Nodebuster"):
    required_power: int

    def _instantiate(self, world: NodebusterWorld) -> Rule.Resolved:
        return self.Resolved(self.required_power, player=world.player)

    class Resolved(Rule.Resolved):
        required_power: int

        def _evaluate(self, state: CollectionState) -> bool:
            total_power = sum(
                state.count(item_name, self.player) * power
                for item_name, power in DAMAGE_POWER.items()
            )
            return total_power >= self.required_power

        def item_dependencies(self) -> dict[str, set[int]]:
            return {item_name: {id(self)} for item_name in DAMAGE_POWER}

        def explain_str(self, state: CollectionState | None = None) -> str:
            if state is None:
                return str(self)
            total_power = sum(
                state.count(item_name, self.player) * power
                for item_name, power in DAMAGE_POWER.items()
            )
            return f"{total_power}/{self.required_power} damage power"

        def __str__(self) -> str:
            return f"at least {self.required_power} damage power"

@dataclass()
class BossDamagePowerRule(Rule[NodebusterWorld], game="Nodebuster"):
    required_power: int

    def _instantiate(self, world: NodebusterWorld) -> Rule.Resolved:
        return self.Resolved(self.required_power, player=world.player)

    class Resolved(Rule.Resolved):
        required_power: int

        def _evaluate(self, state: CollectionState) -> bool:
            total_power = sum(
                state.count(item_name, self.player) * power
                for item_name, power in BOSS_DAMAGE_POWER.items()
            )
            return total_power >= self.required_power

        def item_dependencies(self) -> dict[str, set[int]]:
            return {item_name: {id(self)} for item_name in BOSS_DAMAGE_POWER}

        def explain_str(self, state: CollectionState | None = None) -> str:
            if state is None:
                return str(self)
            total_power = sum(
                state.count(item_name, self.player) * power
                for item_name, power in BOSS_DAMAGE_POWER.items()
            )
            return f"{total_power}/{self.required_power} boss damage power"

        def __str__(self) -> str:
            return f"at least {self.required_power} boss damage power"

@dataclass()
class HealthPowerRule(Rule[NodebusterWorld], game="Nodebuster"):
    required_power: int

    def _instantiate(self, world: NodebusterWorld) -> Rule.Resolved:
        return self.Resolved(self.required_power, player=world.player)

    class Resolved(Rule.Resolved):
        required_power: int

        def _evaluate(self, state: CollectionState) -> bool:
            total_power = sum(
                state.count(item_name, self.player) * power
                for item_name, power in HEALTH_POWER.items()
            )
            return total_power >= self.required_power

        def item_dependencies(self) -> dict[str, set[int]]:
            return {item_name: {id(self)} for item_name in HEALTH_POWER}

        def explain_str(self, state: CollectionState | None = None) -> str:
            if state is None:
                return str(self)
            total_power = sum(
                state.count(item_name, self.player) * power
                for item_name, power in HEALTH_POWER.items()
            )
            return f"{total_power}/{self.required_power} health power"

        def __str__(self) -> str:
            return f"at least {self.required_power} health power"

@dataclass()
class LifestealPowerRule(Rule[NodebusterWorld], game="Nodebuster"):
    required_power: int

    def _instantiate(self, world: NodebusterWorld) -> Rule.Resolved:
        return self.Resolved(self.required_power, player=world.player)

    class Resolved(Rule.Resolved):
        required_power: int

        def _evaluate(self, state: CollectionState) -> bool:
            total_power = sum(
                state.count(item_name, self.player) * power
                for item_name, power in LIFESTEAL_POWER.items()
            )
            return total_power >= self.required_power

        def item_dependencies(self) -> dict[str, set[int]]:
            return {item_name: {id(self)} for item_name in LIFESTEAL_POWER}

        def explain_str(self, state: CollectionState | None = None) -> str:
            if state is None:
                return str(self)
            total_power = sum(
                state.count(item_name, self.player) * power
                for item_name, power in LIFESTEAL_POWER.items()
            )
            return f"{total_power}/{self.required_power} lifesteal power"

        def __str__(self) -> str:
            return f"at least {self.required_power} lifesteal power"

@dataclass()
class BossArmorPowerRule(Rule[NodebusterWorld], game="Nodebuster"):
    required_power: int

    def _instantiate(self, world: NodebusterWorld) -> Rule.Resolved:
        return self.Resolved(self.required_power, player=world.player)

    class Resolved(Rule.Resolved):
        required_power: int

        def _evaluate(self, state: CollectionState) -> bool:
            total_power = sum(
                state.count(item_name, self.player) * power
                for item_name, power in BOSS_ARMOR_POWER.items()
            )
            return total_power >= self.required_power

        def item_dependencies(self) -> dict[str, set[int]]:
            return {item_name: {id(self)} for item_name in BOSS_ARMOR_POWER}

        def explain_str(self, state: CollectionState | None = None) -> str:
            if state is None:
                return str(self)
            total_power = sum(
                state.count(item_name, self.player) * power
                for item_name, power in BOSS_ARMOR_POWER.items()
            )
            return f"{total_power}/{self.required_power} boss armor power"

        def __str__(self) -> str:
            return f"at least {self.required_power} boss armor power"

@dataclass()
class CritDamagePowerRule(Rule[NodebusterWorld], game="Nodebuster"):
    required_power: int

    def _instantiate(self, world: NodebusterWorld) -> Rule.Resolved:
        return self.Resolved(self.required_power, player=world.player)

    class Resolved(Rule.Resolved):
        required_power: int

        def _evaluate(self, state: CollectionState) -> bool:
            total_power = sum(
                state.count(item_name, self.player) * power
                for item_name, power in CRIT_DAMAGE_POWER.items()
            )
            return total_power >= self.required_power

        def item_dependencies(self) -> dict[str, set[int]]:
            return {item_name: {id(self)} for item_name in CRIT_DAMAGE_POWER}

        def explain_str(self, state: CollectionState | None = None) -> str:
            if state is None:
                return str(self)
            total_power = sum(
                state.count(item_name, self.player) * power
                for item_name, power in CRIT_DAMAGE_POWER.items()
            )
            return f"{total_power}/{self.required_power} crit damage power"

        def __str__(self) -> str:
            return f"at least {self.required_power} crit damage power"

@dataclass()
class SpawnRatePowerRule(Rule[NodebusterWorld], game="Nodebuster"):
    required_power: int

    def _instantiate(self, world: NodebusterWorld) -> Rule.Resolved:
        return self.Resolved(self.required_power, player=world.player)

    class Resolved(Rule.Resolved):
        required_power: int

        def _evaluate(self, state: CollectionState) -> bool:
            total_power = sum(
                state.count(item_name, self.player) * power
                for item_name, power in SPAWN_RATE_POWER.items()
            )
            return total_power >= self.required_power

        def item_dependencies(self) -> dict[str, set[int]]:
            return {item_name: {id(self)} for item_name in SPAWN_RATE_POWER}

        def explain_str(self, state: CollectionState | None = None) -> str:
            if state is None:
                return str(self)
            total_power = sum(
                state.count(item_name, self.player) * power
                for item_name, power in SPAWN_RATE_POWER.items()
            )
            return f"{total_power}/{self.required_power} spawn rate power"

        def __str__(self) -> str:
            return f"at least {self.required_power} spawn rate power"

damage1 = DamagePowerRule(1)
damage10 = DamagePowerRule(10)
damage15 = DamagePowerRule(15)
damage31 = DamagePowerRule(31)
damage37 = DamagePowerRule(37)
damage45 = DamagePowerRule(45)
damage63 = DamagePowerRule(63)
damage81 = DamagePowerRule(81)
damage91 = DamagePowerRule(91)
damage166 = DamagePowerRule(166)
damage180 = DamagePowerRule(180)
damage580 = DamagePowerRule(580)
damage680 = DamagePowerRule(680)

bossdamage50 = BossDamagePowerRule(50)
bossdamage350 = BossDamagePowerRule(350)
bossdamage400 = BossDamagePowerRule(400)
bossdamage500 = BossDamagePowerRule(500)
bossdamage700 = BossDamagePowerRule(700)
bossdamage900 = BossDamagePowerRule(900)
bossdamage1000 = BossDamagePowerRule(1000)
bossdamage1500 = BossDamagePowerRule(1500)


addidamage1 = HasAny("DamagePerEnemy1", "Undamaged1", "Execute1", "Undamaged2", "Execute2", "MaxHealthToDamage1")
addidamage5 = HasFromList(*additional_damage, count=5)
addidamage6 = HasFromList(*additional_damage, count=6)
addidamage7 = HasFromList(*additional_damage, count=7)
addidamage11 = HasFromList(*additional_damage, count=11)
addidamage17 = HasFromList(*additional_damage, count=17)
addidamage21 = HasFromList(*additional_damage, count=21)
addidamage25 = HasFromList(*additional_damage, count=25)
addidamage26 = HasFromList(*additional_damage, count=26)

dps1 = Has("RampingDamage1")
dps3 = Has("RampingDamage1", 3)

lifesteal1 = LifestealPowerRule(1)
lifesteal2 = LifestealPowerRule(2)
lifesteal5 = LifestealPowerRule(5)
lifesteal51 = LifestealPowerRule(51)
lifesteal205 = LifestealPowerRule(205)
lifesteal263 = LifestealPowerRule(263)
lifesteal8263 = LifestealPowerRule(8263)
lifesteal13263 = LifestealPowerRule(13263)

bossarmor1 = BossArmorPowerRule(1)
bossarmor2 = BossArmorPowerRule(2)
bossarmor10 = BossArmorPowerRule(10)
bossarmor160 = BossArmorPowerRule(160)
bossarmor210 = BossArmorPowerRule(210)

regen1 = HasFromList(*regen, count=1)
regen5 = HasFromList(*regen, count=5)
regen6 = HasFromList(*regen, count=6)
regen7 = HasFromList(*regen, count=7)
regen14 = HasFromList(*regen, count=14)
regen17 = HasFromList(*regen, count=17)
regen25 = HasFromList(*regen, count=25)

critdamage50 = CritDamagePowerRule(50)
critdamage200 = CritDamagePowerRule(200)
critdamage500 = CritDamagePowerRule(500)
critdamage2100 = CritDamagePowerRule(2100)

infinity1 = HasAny("Infinity1", "Infinity2", "Infinity3", "Infinity4", "Infinity5", "Infinity6", "Infinity7", "Infinity8", "Infinity9")

spawnrate1 = SpawnRatePowerRule(1)
spawnrate950 = SpawnRatePowerRule(950)
spawnrate1050 = SpawnRatePowerRule(1050)
spawnrate1450 = SpawnRatePowerRule(1450)
spawnrate3450 = SpawnRatePowerRule(3450)

bluespawn5 = Has("NodeFinder1", 5)

health1 = HealthPowerRule(1)
health40 = HealthPowerRule(40)
health88 = HealthPowerRule(88)
health376 = HealthPowerRule(376)
health696 = HealthPowerRule(696)
health1016 = HealthPowerRule(1016)
health2216 = HealthPowerRule(2216)
health4016 = HealthPowerRule(4016)
health265936 = HealthPowerRule(265936)
health365936 = HealthPowerRule(365936)
health765936 = HealthPowerRule(765936)

armor1 = HasFromList(*armor, count=1)
armor10 = HasFromList(*armor, count=10)
armor11 = HasFromList(*armor, count=11)
armor12 = HasFromList(*armor, count=12)
armor15 = HasFromList(*armor, count=15)
armor17 = HasFromList(*armor, count=17)
armor32 = HasFromList(*armor, count=32)
armor35 = HasFromList(*armor, count=35)
armor36 = HasFromList(*armor, count=36)
armor45 = HasFromList(*armor, count=45)
armor65 = HasFromList(*armor, count=65)
armor66 = HasFromList(*armor, count=66)
armor95 = HasFromList(*armor, count=95)
armor98 = HasFromList(*armor, count=98)
armor102 = HasFromList(*armor, count=102)
armor108 = HasFromList(*armor, count=108)
armor110 = HasFromList(*armor, count=110)

@dataclass()
class ProgItemRule(Rule[NodebusterWorld], game="Nodebuster"):
    prog_item: str
    target_power: int

    @override
    def _instantiate(self, world: NodebusterWorld) -> Rule.Resolved:
        total: int = 0
        count: int = 0
        power: int = 0
        mapping: list[ProgItemMapping] = progressive_item_map[self.prog_item]
        idx: int = 0
        while power < self.target_power:
            count += 1
            total += 1
            power += mapping[idx].power
            if count == mapping[idx].count:
                count = 0
                idx += 1
        return Has(self.prog_item, total).resolve(world)

can_beat_boss0 = ((ProgItemRule("Progressive Damage", 10) | damage10) #75r upgrades
                & (ProgItemRule("Progressive Health", 40) | health40)
                & (ProgItemRule("Progressive Regen", 1) | regen1)
                & (ProgItemRule("Progressive Armor", 1) | armor1)
                & (ProgItemRule("Progressive Boss Armor", 2) | bossarmor2))
can_beat_boss1 = ((ProgItemRule("Progressive Damage", 15) | damage15 ) #300r upgrades
                & (ProgItemRule("Progressive Additional Damage", 5) | addidamage5)
                & (ProgItemRule("Progressive Health", 88) | health88)
                & (ProgItemRule("Progressive Regen", 5) | regen5)
                & (ProgItemRule("Progressive Lifesteal", 2) | lifesteal2)
                & (ProgItemRule("Progressive Armor", 10) | armor10)
                & (ProgItemRule("Progressive Boss Armor", 10) | bossarmor10)
                & (ProgItemRule("Progressive Boss Damage", 50) | bossdamage50))
can_beat_boss2 = ((ProgItemRule("Progressive Damage", 45) | damage45) #800r upgrades
                & (ProgItemRule("Progressive Additional Damage", 5) | addidamage5)
                & (ProgItemRule("Progressive Health", 376) | health376)
                & (ProgItemRule("Progressive Regen", 6) | regen6)
                & (ProgItemRule("Progressive Lifesteal", 5) | lifesteal5)
                & (ProgItemRule("Progressive Armor", 12) | armor12)
                & (ProgItemRule("Progressive Boss Armor", 10) | bossarmor10)
                & (ProgItemRule("Progressive Boss Damage", 350) | bossdamage350))
can_beat_boss3 = ((ProgItemRule("Progressive Damage", 63) | damage63) #1200r upgrades
                & (ProgItemRule("Progressive Additional Damage", 5) | addidamage5)
                & (ProgItemRule("Progressive Health", 696) | health696)
                & (ProgItemRule("Progressive Regen", 6) | regen6)
                & (ProgItemRule("Progressive Lifesteal", 205) | lifesteal205)
                & (ProgItemRule("Progressive Armor", 17) | armor17)
                & (ProgItemRule("Progressive Boss Armor", 10) | bossarmor10)
                & (ProgItemRule("Progressive Boss Damage", 400) | bossdamage400))
can_beat_boss4 = ((ProgItemRule("Progressive Damage", 81) | damage81) #1600r upgrades
                & (ProgItemRule("Progressive Additional Damage", 7) | addidamage7)
                & (ProgItemRule("Progressive Health", 1016) | health1016)
                & (ProgItemRule("Progressive Regen", 7) | regen7)
                & (ProgItemRule("Progressive Lifesteal", 263) | lifesteal263)
                & (ProgItemRule("Progressive Armor", 32) | armor32)
                & (ProgItemRule("Progressive Boss Armor", 10) | bossarmor10)
                & (ProgItemRule("Progressive Boss Damage", 500) | bossdamage500))
can_beat_boss5 = ((ProgItemRule("Progressive Damage", 180) | damage180) #2500r upgrades
                & (ProgItemRule("Progressive Additional Damage", 11) | addidamage11)
                & (ProgItemRule("Progressive Health", 1016) | health1016)
                & (ProgItemRule("Progressive Regen", 14) | regen14)
                & (ProgItemRule("Progressive Lifesteal", 263) | lifesteal263)
                & (ProgItemRule("Progressive Armor", 66) | armor66)
                & (ProgItemRule("Progressive Boss Armor", 160) | bossarmor160)
                & (ProgItemRule("Progressive Boss Damage", 700) | bossdamage700))
can_beat_boss6 = ((ProgItemRule("Progressive Damage", 180) | damage180) #7000r upgrades
                & (ProgItemRule("Progressive Additional Damage", 21) | addidamage21)
                & (ProgItemRule("Progressive Health", 2216) | health2216)
                & (ProgItemRule("Progressive Regen", 17) | regen17)
                & (ProgItemRule("Progressive Lifesteal", 263) | lifesteal263)
                & (ProgItemRule("Progressive Armor", 98) | armor98)
                & (ProgItemRule("Progressive Boss Armor", 210) | bossarmor210)
                & (ProgItemRule("Progressive Boss Damage", 900) | bossdamage900))
can_beat_boss7 = ((ProgItemRule("Progressive Damage", 580) | damage580) #10000r upgrades
                & (ProgItemRule("Progressive Additional Damage", 25) | addidamage25)
                & (ProgItemRule("Progressive Health", 4016) | health4016)
                & (ProgItemRule("Progressive Regen", 17) | regen17)
                & (ProgItemRule("Progressive Lifesteal", 8263) | lifesteal8263)
                & (ProgItemRule("Progressive Armor", 102) | armor102)
                & (ProgItemRule("Progressive Boss Armor", 210) | bossarmor210)
                & (ProgItemRule("Progressive Boss Damage", 1000) | bossdamage1000))
can_beat_boss8 = ((ProgItemRule("Progressive Damage", 680) | damage680) #40000r upgrades
                & (ProgItemRule("Progressive Additional Damage", 25) | addidamage25)
                & (ProgItemRule("Progressive Health", 365936) | health365936)
                & (ProgItemRule("Progressive Regen", 25) | regen25)
                & (ProgItemRule("Progressive Lifesteal", 13263) | lifesteal13263)
                & (ProgItemRule("Progressive Armor", 108) | armor108)
                & (ProgItemRule("Progressive Boss Armor", 210) | bossarmor210)
                & (ProgItemRule("Progressive Boss Damage", 1000) | bossdamage1000)
                & (ProgItemRule("Progressive Damage Per Second", 1) | dps1)
                & (ProgItemRule("Progressive Critical Damage", 200) | critdamage200)
                & has_critical_damage)
can_beat_boss9 = ((ProgItemRule("Progressive Damage", 680) | damage680) #?r upgrades
                & (ProgItemRule("Progressive Additional Damage", 26) | addidamage26)
                & (ProgItemRule("Progressive Health", 365936) | health365936)
                & (ProgItemRule("Progressive Regen", 25) | regen25)
                & (ProgItemRule("Progressive Lifesteal", 13263) | lifesteal13263)
                & (ProgItemRule("Progressive Armor", 108) | armor108)
                & (ProgItemRule("Progressive Boss Armor", 210) | bossarmor210)
                & (ProgItemRule("Progressive Boss Damage", 1500) | bossdamage1500)
                & (ProgItemRule("Progressive Damage Per Second", 3) | dps3)
                & (ProgItemRule("Progressive Critical Damage", 500) | critdamage500)
                & (ProgItemRule("Progressive Infinity", 1) | infinity1)
                & has_critical_damage)
can_beat_boss10 = ((ProgItemRule("Progressive Damage", 680) | damage680) #73000r upgrades
                 & (ProgItemRule("Progressive Additional Damage", 26) | addidamage26)
                 & (ProgItemRule("Progressive Health", 765936) | health765936)
                 & (ProgItemRule("Progressive Regen", 25) | regen25)
                 & (ProgItemRule("Progressive Lifesteal", 13263) | lifesteal13263)
                 & (ProgItemRule("Progressive Armor", 108) | armor108)
                 & (ProgItemRule("Progressive Boss Armor", 210) | bossarmor210)
                 & (ProgItemRule("Progressive Boss Damage", 1500) | bossdamage1500)
                 & (ProgItemRule("Progressive Damage Per Second", 3) | dps3)
                 & (ProgItemRule("Progressive Critical Damage", 500) | critdamage500)
                 & (ProgItemRule("Progressive Infinity", 1) | infinity1)
                 & has_critical_damage)
can_beat_boss11 = ((ProgItemRule("Progressive Damage", 680) | damage680) #100000r upgrades
                 & (ProgItemRule("Progressive Additional Damage", 26) | addidamage26)
                 & (ProgItemRule("Progressive Health", 765936) | health765936)
                 & (ProgItemRule("Progressive Regen", 25) | regen25)
                 & (ProgItemRule("Progressive Lifesteal", 13263) | lifesteal13263)
                 & (ProgItemRule("Progressive Armor", 108) | armor108)
                 & (ProgItemRule("Progressive Boss Armor", 210) | bossarmor210)
                 & (ProgItemRule("Progressive Boss Damage", 1500) | bossdamage1500)
                 & (ProgItemRule("Progressive Damage Per Second", 3) | dps3)
                 & (ProgItemRule("Progressive Critical Damage", 500) | critdamage500)
                 & (ProgItemRule("Progressive Infinity", 1) | infinity1)
                 & has_critical_damage)
can_beat_boss12 = ((ProgItemRule("Progressive Damage", 680) | damage680) #175000r upgrades
                 & (ProgItemRule("Progressive Additional Damage", 26) | addidamage26)
                 & (ProgItemRule("Progressive Health", 765936) | health765936)
                 & (ProgItemRule("Progressive Regen", 25) | regen25)
                 & (ProgItemRule("Progressive Lifesteal", 13263) | lifesteal13263)
                 & (ProgItemRule("Progressive Armor", 108) | armor108)
                 & (ProgItemRule("Progressive Boss Armor", 210) | bossarmor210)
                 & (ProgItemRule("Progressive Boss Damage", 1500) | bossdamage1500)
                 & (ProgItemRule("Progressive Damage Per Second", 3) | dps3)
                 & (ProgItemRule("Progressive Critical Damage", 2100) | critdamage2100)
                 & (ProgItemRule("Progressive Infinity", 1) | infinity1)
                 & has_critical_damage)
can_beat_boss13 = ((ProgItemRule("Progressive Damage", 680) | damage680) #220000r upgrades
                 & (ProgItemRule("Progressive Additional Damage", 26) | addidamage26)
                 & (ProgItemRule("Progressive Health", 765936) | health765936)
                 & (ProgItemRule("Progressive Regen", 25) | regen25)
                 & (ProgItemRule("Progressive Lifesteal", 13263) | lifesteal13263)
                 & (ProgItemRule("Progressive Armor", 108) | armor108)
                 & (ProgItemRule("Progressive Boss Armor", 210) | bossarmor210)
                 & (ProgItemRule("Progressive Boss Damage", 1500) | bossdamage1500)
                 & (ProgItemRule("Progressive Damage Per Second", 3) | dps3)
                 & (ProgItemRule("Progressive Critical Damage", 2100) | critdamage2100)
                 & (ProgItemRule("Progressive Infinity", 1) | infinity1)
                 & has_critical_damage)

can_start_red_milestones = has_milestones_upgrade
can_grind_red_milestones = has_milestones_upgrade & can_beat_boss13 & (ProgItemRule("Progressive SpawnRate", 3450) | spawnrate3450)

can_start_blue_milestones = has_milestones_upgrade & has_access_to_blue_enemies
can_grind_blue_milestones = has_milestones_upgrade & can_beat_boss13 & (ProgItemRule("Progressive SpawnRate", 3450) | spawnrate3450) & (ProgItemRule("Progressive Blue Spawn", 5) | bluespawn5)

can_start_yellow_milestones = has_milestones_upgrade & has_access_to_yellow_enemies
can_grind_yellow_milestones = has_milestones_upgrade & can_beat_boss13 & (ProgItemRule("Progressive SpawnRate", 3450) | spawnrate3450) & (ProgItemRule("Progressive Blue Spawn", 5) | bluespawn5)

has_all_infinities = HasAll("Infinity1", "Infinity2", "Infinity3", "Infinity4", "Infinity5", "Infinity6", "Infinity7", "Infinity8", "Infinity9") | Has("Progressive Infinity", 9)
can_release_virus = has_crypto_mine & Has("Laboratory") & can_beat_boss13 & (infinity_mode_off | has_all_infinities)
released_virus = Has("Virus Deployed")


def get_location_rules_lookup(world, player: int) -> dict:
    rules_lookup = {
        "Armor2-1": can_beat_boss0,
        "Armor2-2": can_beat_boss0,
        "Armor2-3": can_beat_boss0,
        "Armor2-4": can_beat_boss0,
        "Armor2-5": can_beat_boss0,
        "Armor3-1": can_beat_boss1,
        "Armor3-2": can_beat_boss1,
        "Armor3-3": can_beat_boss1,
        "Armor3-4": can_beat_boss1,
        "Armor3-5": can_beat_boss1,
        "Armor3-6": can_beat_boss1,
        "Armor3-7": can_beat_boss1,
        "Armor3-8": can_beat_boss1,
        "Armor3-9": can_beat_boss1,
        "Armor3-10": can_beat_boss1,
        "Armor4-1": can_beat_boss1,
        "Armor4-2": can_beat_boss1,
        "Armor4-3": can_beat_boss1,
        "Armor4-4": can_beat_boss1,
        "Armor4-5": can_beat_boss1,
        "Armor4-6": can_beat_boss1,
        "Armor4-7": can_beat_boss1,
        "Armor4-8": can_beat_boss1,
        "Armor4-9": can_beat_boss1,
        "Armor4-10": can_beat_boss1,
        "Armor5-1": can_beat_boss0,
        "Armor5-2": can_beat_boss0,
        "Armor5-3": can_beat_boss0,
        "Armor5-4": can_beat_boss0,
        "Armor5-5": can_beat_boss0,
        "Armor5-6": can_beat_boss0,
        "Armor5-7": can_beat_boss0,
        "Armor5-8": can_beat_boss0,
        "Armor5-9": can_beat_boss0,
        "Armor5-10": can_beat_boss0,
        "Armor5-11": can_beat_boss0,
        "Armor5-12": can_beat_boss0,
        "Armor5-13": can_beat_boss0,
        "Armor5-14": can_beat_boss0,
        "Armor5-15": can_beat_boss0,
        "Armor5-16": can_beat_boss0,
        "Armor5-17": can_beat_boss0,
        "Armor5-18": can_beat_boss0,
        "Armor5-19": can_beat_boss0,
        "Armor5-20": can_beat_boss0,
        "Armor6-1": can_beat_boss1,
        "Armor6-2": can_beat_boss1,
        "Armor6-3": can_beat_boss1,
        "Armor6-4": can_beat_boss1,
        "Armor6-5": can_beat_boss1,
        "Armor6-6": can_beat_boss1,
        "Armor6-7": can_beat_boss1,
        "Armor6-8": can_beat_boss1,
        "Armor6-9": can_beat_boss1,
        "Armor6-10": can_beat_boss1,
        "Armor6-11": can_beat_boss1,
        "Armor6-12": can_beat_boss1,
        "Armor6-13": can_beat_boss1,
        "Armor6-14": can_beat_boss1,
        "Armor6-15": can_beat_boss1,
        "Armor6-16": can_beat_boss1,
        "Armor6-17": can_beat_boss1,
        "Armor6-18": can_beat_boss1,
        "Armor6-19": can_beat_boss1,
        "Armor6-20": can_beat_boss1,
        "Armor6-21": can_beat_boss1,
        "Armor6-22": can_beat_boss1,
        "Armor6-23": can_beat_boss1,
        "Armor6-24": can_beat_boss1,
        "Armor6-25": can_beat_boss1,
        "Armor6-26": can_beat_boss1,
        "Armor6-27": can_beat_boss1,
        "Armor6-28": can_beat_boss1,
        "Armor6-29": can_beat_boss1,
        "Armor6-30": can_beat_boss1,
        "Armor7-1": can_beat_boss5,
        "Armor7-2": can_beat_boss5,
        "Armor7-3": can_beat_boss5,
        "Armor7-4": can_beat_boss5,
        "Armor7-5": can_beat_boss5,
        "ArmorPerEnemy1-1": can_beat_boss0,
        "ArmorPerEnemy1-2": can_beat_boss1,
        "ArmorPerEnemy1-3": can_beat_boss1,
        "ArmorPerEnemy1-4": can_beat_boss1,
        "ArmorPerEnemy1-5": can_beat_boss1,
        "ArmorPerEnemy1-6": can_beat_boss1,
        "ArmorPerEnemy1-7": can_beat_boss1,
        "ArmorPerEnemy1-8": can_beat_boss2,
        "ArmorPerEnemy1-9": can_beat_boss2,
        "ArmorPerEnemy1-10": can_beat_boss3,
        "AutoCollect-1": has_access_to_blue_enemies,
        "AutoCollect-2": has_access_to_blue_enemies,
        "AutoCollect-3": has_access_to_blue_enemies,
        "AutoCollect-4": has_access_to_blue_enemies,
        "AutoCollect-5": has_access_to_blue_enemies,
        "AutoCollect-6": has_access_to_blue_enemies,
        "AutoCollect-7": has_access_to_blue_enemies,
        "AutoCollect-8": has_access_to_blue_enemies,
        "BonusDropChance1-1": can_beat_boss0,
        "BonusDropChance1-2": can_beat_boss1,
        "BonusDropChance1-3": can_beat_boss2,
        "BonusDropChance1-4": can_beat_boss5,
        "BonusDropChance1-5": can_beat_boss7,
        "BossArmor2-1": has_access_to_blue_enemies,
        "BossArmor2-2": has_access_to_blue_enemies,
        "BossArmor2-3": has_access_to_blue_enemies,
        "BossArmor2-4": has_access_to_blue_enemies,
        "BossArmor2-5": has_access_to_blue_enemies,
        "BossArmor2-6": has_access_to_blue_enemies,
        "BossArmor2-7": has_access_to_blue_enemies,
        "BossArmor2-8": has_access_to_blue_enemies,
        "BossDamage1-2": can_beat_boss0,
        "BossDamage1-3": can_beat_boss0,
        "BossDamage1-4": can_beat_boss0,
        "BossDamage1-5": can_beat_boss0,
        "BossDamage1-6": can_beat_boss1,
        "BossDamage1-7": can_beat_boss1,
        "BossDamage1-8": can_beat_boss2,
        "BossDamage1-9": can_beat_boss3,
        "BossDamage1-10": can_beat_boss3,
        "BossDamage2-1": can_beat_boss5,
        "BossDamage2-2": can_beat_boss5,
        "BossDamage2-3": can_beat_boss5,
        "BossDamage2-4": can_beat_boss6,
        "BossDamage2-5": can_beat_boss6,
        "BossDamage2-6": can_beat_boss6,
        "BossDamage2-7": can_beat_boss7,
        "BossDamage2-8": can_beat_boss7,
        "BossDamage2-9": can_beat_boss7,
        "BossDamage2-10": can_beat_boss7,
        "CritChance1-1": can_beat_boss2,
        "CritChance1-2": can_beat_boss4,
        "CritChance1-3": can_beat_boss5,
        "CritChance1-4": can_beat_boss5,
        "CritChance1-5": can_beat_boss5,
        "CritChance1-6": can_beat_boss6,
        "CritChance1-7": can_beat_boss7,
        "CritChance1-8": can_beat_boss7,
        "CritChance1-9": can_beat_boss7,
        "CritChance1-10": can_beat_boss7,
        "CritDamage1-1": can_beat_boss2,
        "CritDamage1-2": can_beat_boss4,
        "CritDamage1-3": can_beat_boss5,
        "CritDamage1-4": can_beat_boss5,
        "CritDamage1-5": can_beat_boss5,
        "CritDamage1-6": can_beat_boss6,
        "CritDamage1-7": can_beat_boss7,
        "CritDamage1-8": can_beat_boss7,
        "CritDamage1-9": can_beat_boss7,
        "CritDamage1-10": can_beat_boss7,
        "CritDamage2-1": can_beat_boss10,
        "CritDamage2-2": can_beat_boss10,
        "CritDamage2-3": can_beat_boss11,
        "CritDamage2-4": can_beat_boss11,
        "CritDamage2-5": can_beat_boss11,
        "CritDamage2-6": can_beat_boss12,
        "CritDamage2-7": can_beat_boss12,
        "CritDamage2-8": can_beat_boss12,
        "CryptoMine-1": has_access_to_blue_enemies,
        "Damage2-1": can_beat_boss0,
        "Damage2-2": can_beat_boss0,
        "Damage2-3": can_beat_boss0,
        "Damage2-4": can_beat_boss0,
        "Damage2-5": can_beat_boss0,
        "Damage2-6": can_beat_boss0,
        "Damage2-7": can_beat_boss0,
        "Damage2-8": can_beat_boss0,
        "Damage2-9": can_beat_boss1,
        "Damage2-10": can_beat_boss1,
        "Damage3-1": has_access_to_blue_enemies,
        "Damage3-2": has_access_to_blue_enemies,
        "Damage3-3": has_access_to_blue_enemies,
        "Damage3-4": has_access_to_blue_enemies,
        "Damage3-5": has_access_to_blue_enemies,
        "Damage3-6": has_access_to_blue_enemies,
        "Damage3-7": has_access_to_blue_enemies,
        "Damage3-8": has_access_to_blue_enemies,
        "Damage3-9": has_access_to_blue_enemies,
        "Damage3-10": has_access_to_blue_enemies,
        "Damage4-1": has_access_to_blue_enemies,
        "Damage4-2": has_access_to_blue_enemies,
        "Damage4-3": has_access_to_blue_enemies,
        "Damage5-1": can_beat_boss5,
        "Damage5-2": can_beat_boss5,
        "Damage5-3": can_beat_boss5,
        "Damage5-4": can_beat_boss6,
        "Damage5-5": can_beat_boss6,
        "DamagePerEnemy1-2": can_beat_boss0,
        "DamagePerEnemy1-3": can_beat_boss0,
        "DamagePerEnemy1-4": can_beat_boss1,
        "DamagePerEnemy1-5": can_beat_boss2,
        "EnemyDeathPulseBolts-1": can_beat_boss6,
        "EnemyDeathPulseBolts-2": can_beat_boss7,
        "EnemyDeathPulseBolts-3": can_beat_boss7,
        "EnemyDeathPulseBolts-4": can_beat_boss7,
        "EnemyDeathPulseBolts-5": can_beat_boss7,
        "EnemyDeathPulseBolts-6": can_beat_boss7,
        "Execute1-1": can_beat_boss2,
        "Execute1-2": can_beat_boss2,
        "Execute1-3": can_beat_boss3,
        "Execute1-4": can_beat_boss3,
        "Execute1-5": can_beat_boss4,
        "Execute1-6": can_beat_boss4,
        "Execute2-1": can_beat_boss6,
        "Execute2-2": can_beat_boss7,
        "Execute2-3": can_beat_boss7,
        "Execute2-4": can_beat_boss7,
        "ExplodersChance-1": has_access_to_blue_enemies,
        "FocusArmor1-1": can_beat_boss6,
        "FocusArmor1-2": can_beat_boss6,
        "FocusArmor1-3": can_beat_boss6,
        "FocusArmor1-4": can_beat_boss7,
        "FocusArmor1-5": can_beat_boss7,
        "Health2-5": can_beat_boss0,
        "Health2-6": can_beat_boss0,
        "Health2-7": can_beat_boss0,
        "Health2-8": can_beat_boss0,
        "Health3-1": can_beat_boss1,
        "Health3-2": can_beat_boss1,
        "Health3-3": can_beat_boss1,
        "Health3-4": can_beat_boss1,
        "Health3-5": can_beat_boss1,
        "Health3-6": can_beat_boss1,
        "Health3-7": can_beat_boss1,
        "Health3-8": can_beat_boss1,
        "Health3-9": can_beat_boss1,
        "Health3-10": can_beat_boss1,
        "Health4-1": can_beat_boss2,
        "Health4-2": can_beat_boss2,
        "Health4-3": can_beat_boss2,
        "Health4-4": can_beat_boss2,
        "Health4-5": can_beat_boss2,
        "Health4-6": can_beat_boss2,
        "Health4-7": can_beat_boss2,
        "Health4-8": can_beat_boss2,
        "Health4-9": can_beat_boss2,
        "Health4-10": can_beat_boss2,
        "Health5-1": can_beat_boss5,
        "Health5-2": can_beat_boss5,
        "Health5-3": can_beat_boss6,
        "Health7-1": can_beat_boss10,
        "Health7-2": can_beat_boss10,
        "Health7-3": can_beat_boss10,
        "Health7-4": can_beat_boss10,
        "Health7-5": can_beat_boss10,
        "Lifesteal1-1": has_access_to_blue_enemies,
        "Lifesteal1-2": has_access_to_blue_enemies,
        "Lifesteal1-3": has_access_to_blue_enemies,
        "Lifesteal1-4": has_access_to_blue_enemies,
        "Lifesteal1-5": has_access_to_blue_enemies,
        "Lifesteal2-1": can_beat_boss4,
        "Lifesteal2-2": can_beat_boss4,
        "Lifesteal2-3": can_beat_boss4,
        "Lifesteal3-1": can_beat_boss6,
        "Lifesteal3-2": can_beat_boss8,
        "LightningChance1-1": can_beat_boss9,
        "LightningChance1-2": can_beat_boss10,
        "LightningChance1-3": can_beat_boss11,
        "LightningChance1-4": can_beat_boss12,
        "LightningChance1-5": can_beat_boss13,
        "LightningDamage1-1": has_access_to_blue_enemies,
        "LightningDamage1-2": has_access_to_blue_enemies,
        "LightningDamage1-3": has_access_to_blue_enemies,
        "LightningDamage1-4": has_access_to_blue_enemies,
        "LightningDamage1-5": has_access_to_blue_enemies,
        "LightningDamage1-6": has_access_to_blue_enemies,
        "LightningDamage1-7": has_access_to_blue_enemies,
        "LightningDamage1-8": has_access_to_blue_enemies,
        "MaxHealthHeal1-1": has_access_to_blue_enemies,
        "MaxHealthHeal1-2": has_access_to_blue_enemies,
        "MaxHealthHeal1-3": has_access_to_blue_enemies,
        "MaxHealthHeal1-4": has_access_to_blue_enemies,
        "MaxHealthHeal1-5": has_access_to_blue_enemies,
        "MaxHealthHeal1-6": has_access_to_blue_enemies,
        "MaxHealthHeal1-7": has_access_to_blue_enemies,
        "MaxHealthHeal1-8": has_access_to_blue_enemies,
        "MaxHealthHeal1-9": has_access_to_blue_enemies,
        "MaxHealthHeal1-10": has_access_to_blue_enemies,
        "MaxHealthHeal2-1": can_beat_boss6,
        "MaxHealthHeal2-2": can_beat_boss6,
        "MaxHealthHeal2-3": can_beat_boss6,
        "MaxHealthHeal2-4": can_beat_boss6,
        "MaxHealthHeal2-5": can_beat_boss6,
        "MaxHealthToArmor1-1": has_access_to_blue_enemies,
        "MaxHealthToArmor1-2": has_access_to_blue_enemies,
        "MaxHealthToArmor1-3": has_access_to_blue_enemies,
        "MaxHealthToArmor1-4": has_access_to_blue_enemies,
        "MaxHealthToArmor1-5": has_access_to_blue_enemies,
        "MaxHealthToArmor2-1": can_beat_boss8,
        "MaxHealthToDamage1-1": can_beat_boss10,
        "MovingPulser1-1": can_beat_boss5,
        "MovingPulser1-2": can_beat_boss7,
        "MovingPulser1-3": can_beat_boss7,
        "MovingPulser1-4": can_beat_boss10,
        "MovingPulser1-5": can_beat_boss12,
        "MovingPulserSize1-1": has_access_to_blue_enemies,
        "MovingPulserSize1-2": has_access_to_blue_enemies,
        "MovingPulserSize1-3": has_access_to_blue_enemies,
        "MovingPulserSize1-4": has_access_to_blue_enemies,
        "MovingPulserSize1-5": has_access_to_blue_enemies,
        "MovingPulserSize1-6": has_access_to_blue_enemies,
        "MovingPulserSpeed1-1": has_access_to_blue_enemies,
        "MovingPulserSpeed1-2": has_access_to_blue_enemies,
        "MovingPulserSpeed1-3": has_access_to_blue_enemies,
        "MovingPulserSpeed1-4": has_access_to_blue_enemies,
        "MovingPulserSpeed1-5": has_access_to_blue_enemies,
        "NodeFinder1-1": has_access_to_blue_enemies & can_beat_boss0,
        "NodeFinder1-2": can_beat_boss3,
        "NodeFinder1-3": can_beat_boss5,
        "NodeFinder1-4": can_beat_boss5,
        "NodeFinder1-5": can_beat_boss6,
        "PickupRadius1-1": can_beat_boss0,
        "PickupRadius1-2": can_beat_boss3,
        "PickupRadius1-3": can_beat_boss5,
        "PickupRadius1-4": can_beat_boss7,
        "PickupRadius1-5": can_beat_boss9,
        "PulseBoltDamage1-1": can_beat_boss1,
        "PulseBoltDamage1-2": can_beat_boss1,
        "PulseBoltDamage1-3": can_beat_boss1,
        "PulseBoltDamage1-4": can_beat_boss1,
        "PulseBoltDamage1-5": can_beat_boss2,
        "PulseBoltDamage1-6": can_beat_boss2,
        "PulseBoltDamage1-7": can_beat_boss3,
        "PulseBoltDamage1-8": can_beat_boss3,
        "PulseBoltDamage1-9": can_beat_boss4,
        "PulseBoltDamage1-10": can_beat_boss4,
        "PulseBoltDamage2-1": can_beat_boss7,
        "PulseBoltDamage2-2": can_beat_boss7,
        "PulseBoltDamage2-3": can_beat_boss7,
        "PulseBoltExplode-1": has_access_to_blue_enemies,
        "PulseBolts-1": has_access_to_blue_enemies,
        "RampingArmor1-1": can_beat_boss8,
        "RampingArmor1-2": can_beat_boss10,
        "RampingArmor1-3": can_beat_boss11,
        "RampingArmor1-4": can_beat_boss11,
        "RampingArmor1-5": can_beat_boss12,
        "RampingDamage1-1": can_beat_boss7,
        "RampingDamage1-2": can_beat_boss10,
        "RampingDamage1-3": can_beat_boss12,
        "Salvaging1-1": can_beat_boss0,
        "Salvaging1-2": can_beat_boss0,
        "Salvaging1-3": can_beat_boss0,
        "Salvaging1-4": can_beat_boss0,
        "Salvaging1-5": can_beat_boss0,
        "Salvaging2-1": has_access_to_blue_enemies,
        "Size1-8": can_beat_boss0,
        "Size1-9": can_beat_boss0,
        "Size1-10": can_beat_boss0,
        "SpawnRate1-10": can_beat_boss0,
        "SpawnRate1-11": can_beat_boss0,
        "SpawnRate1-12": can_beat_boss0,
        "SpawnRate1-13": can_beat_boss0,
        "SpawnRate1-14": can_beat_boss0,
        "SpawnRate1-15": can_beat_boss0,
        "SpawnRate3-1": can_beat_boss4,
        "SpawnRate3-2": can_beat_boss4,
        "SpawnRate3-3": can_beat_boss4,
        "SpawnRate3-4": can_beat_boss5,
        "SpawnRate3-5": can_beat_boss5,
        "SpawnRate4-1": can_beat_boss7,
        "SpawnRate4-2": can_beat_boss7,
        "SpawnRate4-3": can_beat_boss7,
        "SpawnRate4-4": can_beat_boss7,
        "SpawnRate4-5": can_beat_boss8,
        "StealMaxHealth1-1": has_access_to_blue_enemies,
        "StealMaxHealth2-1": has_access_to_blue_enemies,
        "StealMaxHealth3-1": can_beat_boss8,
        "Undamaged1-1": can_beat_boss2,
        "Undamaged1-2": can_beat_boss2,
        "Undamaged1-3": can_beat_boss3,
        "Undamaged1-4": can_beat_boss3,
        "Undamaged1-5": can_beat_boss4,
        "Undamaged1-6": can_beat_boss4,
        "Undamaged2-1": can_beat_boss6,
        "Undamaged2-2": can_beat_boss7,
        "Undamaged2-3": can_beat_boss7,
        "Undamaged2-4": can_beat_boss7,
        "YellowSpawn1-1": can_beat_boss2,
        "YellowSpawn2-1": has_access_to_blue_enemies,
        # Milestones
        "Milestones-1": has_access_to_blue_enemies,
        "Reds500": has_milestones_upgrade,
        "Blues10": has_milestones_upgrade,
        "Reds2k": has_milestones_upgrade,
        "Blues100": has_milestones_upgrade,
        "Reds4k": has_milestones_upgrade,
        "Blues200": has_milestones_upgrade,
        "Reds6k": has_milestones_upgrade,
        "Blues300": has_milestones_upgrade,
        "Reds8k": has_milestones_upgrade,
        "Blues500": has_milestones_upgrade,
        "Reds10k": can_grind_red_milestones,
        "Blues800": can_grind_blue_milestones,
        "Yellows5": can_grind_yellow_milestones,
        "Reds15k": can_grind_red_milestones,
        "Blues1.2k": can_grind_blue_milestones,
        "Yellows10": can_grind_yellow_milestones,
        "Reds20k": can_grind_red_milestones,
        "Blues1.6k": can_grind_blue_milestones,
        "Yellows15": can_grind_yellow_milestones,
        "Reds30k": can_grind_red_milestones,
        "Blues2k": can_grind_blue_milestones,
        "Reds50k": can_grind_red_milestones,
        "Blues4k": can_grind_blue_milestones,
        "Reds100k": can_grind_red_milestones,
        "Blues8k": can_grind_blue_milestones,
        # Boss Drop progressive order
        "AttackSpeed1-1": Has("Boss Drop", 1) | (boss_mode_off & can_beat_boss0),
        "AttackSpeed2-1": Has("Boss Drop", 2) | (boss_mode_off & has_access_to_blue_enemies & can_beat_boss2),
        "SpawnRate2-1": Has("Boss Drop", 3) | (boss_mode_off & can_beat_boss3),
        "DropHeal1-1": Has("Boss Drop", 4) | (boss_mode_off & can_beat_boss4),
        "Size2-1": Has("Boss Drop", 5) | (boss_mode_off & has_access_to_blue_enemies & can_beat_boss5),
        "Size3-1": Has("Boss Drop", 6) | (boss_mode_off & has_access_to_blue_enemies & can_beat_boss13),
        "MovingPulserSize2-1": Has("Boss Drop", 7) | (boss_mode_off & has_access_to_blue_enemies & can_beat_boss13),
        "PulseBoltCount2-1": Has("Boss Drop", 8) | (boss_mode_off),
        "Infinity1-1": Has("Boss Drop", 9) | boss_mode_off,
        "Infinity2-1": Has("Boss Drop", 10) | boss_mode_off,
        "Infinity3-1": Has("Boss Drop", 11) | boss_mode_off,
        "Infinity4-1": Has("Boss Drop", 12) | boss_mode_off,
        "Infinity5-1": Has("Boss Drop", 13) | boss_mode_off,
        "Infinity6-1": Has("Boss Drop", 14) | (boss_mode_off & can_beat_boss11),
        "Infinity7-1": Has("Boss Drop", 15) | (boss_mode_off & can_beat_boss12),
        "Infinity8-1": Has("Boss Drop", 16) | (boss_mode_off & can_beat_boss13),
        "Infinity9-1": Has("Boss Drop", 17) | boss_mode_off,
        # Boss Requirements
        "Boss-0": can_beat_boss0,
        "Boss-1": can_beat_boss1,
        "Boss-2": can_beat_boss2,
        "Boss-3": can_beat_boss3,
        "Boss-4": can_beat_boss4,
        "Boss-5": can_beat_boss5,
        "Boss-6": can_beat_boss6,
        "Boss-7": can_beat_boss7,
        "Boss-8": can_beat_boss8,
        "Boss-9": can_beat_boss9,
        "Boss-10": can_beat_boss10,
        "Boss-11": can_beat_boss11,
        "Boss-12": can_beat_boss12,
        "Boss-13": can_beat_boss13,
        "Boss-14": can_beat_boss13,
        "Boss-15": can_beat_boss13,
        "Boss-16": can_beat_boss13,
        "Boss-17": can_beat_boss13,
        "Boss-18": can_beat_boss13,
        "Boss-19": can_beat_boss13,
        "Boss-20": can_beat_boss13,
        "Boss-21": can_beat_boss13,
        "Boss-22": can_beat_boss13,
        "Boss-23": can_beat_boss13,
        "Boss-24": can_beat_boss13,
        "Boss-25": can_beat_boss13,
        # Goal
        "Virus Released": can_release_virus,
    }
    return rules_lookup


def set_region_rules(world, player: int) -> dict:
        # Bits
        # Node
        world.get_region("Menu").connect(world.get_region("Upgrade Tree"), "Skill Tree")
        world.get_region("Upgrade Tree").connect(world.get_region("Damage1Root"), "Damage1")
        world.get_region("Upgrade Tree").connect(world.get_region("Milestone Page"), "Milestone Page", has_milestones_upgrade)
        world.get_region("Upgrade Tree").connect(world.get_region("Boss Drops"), "Boss Kills")
        world.get_region("Damage1Root").connect(world.get_region("Endurance"), "Health1", ProgItemRule("Progressive Damage", 1) | damage1)
        world.get_region("Damage1Root").connect(world.get_region("Connection Buster"), "DamagePerEnemy1", (ProgItemRule("Progressive Damage", 1) | damage1) & can_beat_boss0)
        world.get_region("Damage1Root").connect(world.get_region("Crowding"), "SpawnRate1", ProgItemRule("Progressive Damage", 1) | damage1)
        world.get_region("Endurance").connect(world.get_region("Firewall"), "Armor1", ProgItemRule("Progressive Health", 1) | health1)
        world.get_region("Endurance").connect(world.get_region("Repair Tool"), "HealthRegen1", ProgItemRule("Progressive Health", 1) | health1)
        world.get_region("Crowding").connect(world.get_region("Swarming"), "SpawnRate2", ProgItemRule("Progressive SpawnRate", 1) | spawnrate1)
        world.get_region("Crowding").connect(world.get_region("Bit Boost"), "BitBoost1", ProgItemRule("Progressive SpawnRate", 1) | spawnrate1)
        world.get_region("Crowding").connect(world.get_region("Influence"), "Size1", ProgItemRule("Progressive SpawnRate", 1) | spawnrate1)
        world.get_region("Firewall").connect(world.get_region("Antivirus"), "Armor2", (ProgItemRule("Progressive Armor", 10) | armor10) & can_beat_boss0)
        world.get_region("Firewall").connect(world.get_region("Boss Guard"), "BossArmor1")
        world.get_region("Influence").connect(world.get_region("Magnet"), "PickupRadius1", can_beat_boss0)
        world.get_region("Boss Guard").connect(world.get_region("Better Endurance"), "Health2L", (ProgItemRule("Progressive Lifesteal", 1) | lifesteal1) | (ProgItemRule("Progressive Boss Armor", 1) | bossarmor1))
        world.get_region("Repair Tool").connect(world.get_region("Salvaging"), "Salvaging", can_beat_boss0)
        world.get_region("Salvaging").connect(world.get_region("Better Endurance"), "Health2R", (ProgItemRule("Progressive Lifesteal", 1) | lifesteal1) | (ProgItemRule("Progressive Boss Armor", 1) | bossarmor1))
        world.get_region("Salvaging").connect(world.get_region("Sapper"), "Lifesteal1", (ProgItemRule("Progressive Lifesteal", 1) | lifesteal1) & has_access_to_blue_enemies)
        world.get_region("Salvaging").connect(world.get_region("Skilled Salvager"), "Salvaging2", (ProgItemRule("Progressive Lifesteal", 5) | lifesteal5) & has_access_to_blue_enemies)
        world.get_region("Connection Buster").connect(world.get_region("Giant Slayer"), "BossDamage1", (ProgItemRule("Progressive Additional Damage", 1) | addidamage1) & can_beat_boss0)
        world.get_region("Giant Slayer").connect(world.get_region("Colossus Slayer"), "BossDamage2", can_beat_boss5)
        world.get_region("Giant Slayer").connect(world.get_region("Repeating"), "AttackSpeed1", ProgItemRule("Progressive Additional Damage", 1) | addidamage1)
        world.get_region("Repeating").connect(world.get_region("Proficiency"), "Damage2", can_beat_boss0)
        world.get_region("Repeating").connect(world.get_region("Repeat-Repeating"), "AttackSpeed2")
        world.get_region("Bit Boost").connect(world.get_region("Node Finder"), "NodeFinder1", can_beat_boss0)
        world.get_region("Bit Boost").connect(world.get_region("Plundering"), "BonusDropChance1", can_beat_boss0)
        world.get_region("Proficiency").connect(world.get_region("Potency"), "Damage3", (ProgItemRule("Progressive Damage", 31) | damage31) & has_access_to_blue_enemies)
        world.get_region("Repeat-Repeating").connect(world.get_region("Pulse Bolts"), "PulseBolts", has_access_to_blue_enemies)
        world.get_region("Swarming").connect(world.get_region("Infesting"), "SpawnRate3", (ProgItemRule("Progressive SpawnRate", 950) | spawnrate950) & can_beat_boss4)
        world.get_region("Better Endurance").connect(world.get_region("Big Heart"), "Health3", can_beat_boss1)
        world.get_region("Better Endurance").connect(world.get_region("Self-Repair"), "HealthRegen2")
        world.get_region("Big Heart").connect(world.get_region("Transplant"), "Health4", has_crypto_mine & can_beat_boss2)
        world.get_region("Self-Repair").connect(world.get_region("Scaling Regeneration"), "MaxHealthHeal1", has_access_to_blue_enemies & can_beat_boss6)
        world.get_region("Antivirus").connect(world.get_region("Bolster"), "Armor3", (ProgItemRule("Progressive Armor", 15) | armor15) & can_beat_boss1)
        world.get_region("Antivirus").connect(world.get_region("Swarm Defense System"), "ArmorPerEnemy1", (ProgItemRule("Progressive Armor", 11) | armor11) & can_beat_boss0)
        world.get_region("Bolster").connect(world.get_region("Super Armor"), "Armor4", (ProgItemRule("Progressive Armor", 35) | armor35) & can_beat_boss1)
        world.get_region("Potency").connect(world.get_region("First Strike"), "Undamaged1", (ProgItemRule("Progressive Damage", 37) | damage37) & can_beat_boss2)
        world.get_region("Potency").connect(world.get_region("Nodeblade"), "Damage4", (ProgItemRule("Progressive Damage", 91) | damage91) & has_access_to_blue_enemies)
        world.get_region("Potency").connect(world.get_region("Crit Chance"), "CritChance1", (ProgItemRule("Progressive Damage", 37) | damage37) & can_beat_boss2)
        world.get_region("First Strike").connect(world.get_region("Last Strike"), "Execute1", (ProgItemRule("Progressive Additional Damage", 6) | addidamage6) & can_beat_boss2)
        world.get_region("First Strike").connect(world.get_region("Ambush"), "Undamaged2", can_beat_boss6)
        world.get_region("Last Strike").connect(world.get_region("Finishing Blow"), "Execute2", (ProgItemRule("Progressive Additional Damage", 17) | addidamage17) & can_beat_boss6)
        world.get_region("Nodeblade").connect(world.get_region("Auto Pulser"), "MovingPulser1", has_crypto_mine & can_beat_boss5)
        world.get_region("Nodeblade").connect(world.get_region("Netblade"), "Damage5", ((ProgItemRule("Progressive Damage", 166) | damage166) & has_crypto_mine) & can_beat_boss5)
        world.get_region("Crit Chance").connect(world.get_region("Crit Damage"), "CritDamage1", Has("CritChance1") & can_beat_boss2)
        world.get_region("Crit Damage").connect(world.get_region("Big Crit"), "CritDamage2", ((ProgItemRule("Progressive Critical Damage", 50) | critdamage50) & has_crypto_mine) & can_beat_boss10)
        world.get_region("Pulse Bolts").connect(world.get_region("Bolt Damage"), "PulseBoltDamage1", Has("PulseBolts") & can_beat_boss1)
        world.get_region("Pulse Bolts").connect(world.get_region("Bolt Count"), "PulseBoltCount1", Has("PulseBolts"))
        world.get_region("Bolt Damage").connect(world.get_region("Bolt Burst"), "PulseBoltExplode", has_access_to_blue_enemies & Has("PulseBoltDamage1"))
        world.get_region("Bolt Count").connect(world.get_region("Bolt Barrage"), "PulseBoltCount2", Has("PulseBoltCount2"))
        world.get_region("Bolt Burst").connect(world.get_region("Bolt Lethality"), "PulseBoltDamage2L", HasAny("PulseBoltExplode", "PulseBoltCount2") & has_crypto_mine & can_beat_boss6)
        world.get_region("Bolt Barrage").connect(world.get_region("Bolt Lethality"), "PulseBoltDamage2R", HasAny("PulseBoltExplode", "PulseBoltCount2") & has_crypto_mine & can_beat_boss6)
        world.get_region("Sapper").connect(world.get_region("Patcher"), "DropHeal1", ProgItemRule("Progressive Lifesteal", 51) | lifesteal51)
        world.get_region("Scaling Regeneration").connect(world.get_region("Drainer"), "Lifesteal2", (ProgItemRule("Progressive Regen", 17) | regen17) & has_crypto_mine & can_beat_boss4)
        world.get_region("Infesting").connect(world.get_region("Domain Expansion"), "Size2", ProgItemRule("Progressive SpawnRate", 1050) | spawnrate1050)
        world.get_region("Infesting").connect(world.get_region("Overloaded"), "SpawnRate4", (ProgItemRule("Progressive SpawnRate", 1450) | spawnrate1450) & has_crypto_mine & can_beat_boss7)
        world.get_region("Domain Expansion").connect(world.get_region("Crypto Mine"), "CryptoMine", has_access_to_blue_enemies)
        world.get_region("Domain Expansion").connect(world.get_region("B.I.G."), "Size3")
        world.get_region("Super Armor").connect(world.get_region("Anti-Purple"), "BossArmor2", (ProgItemRule("Progressive Armor", 36) | armor36) & has_access_to_blue_enemies)
        world.get_region("Super Armor").connect(world.get_region("Bit Armor"), "Armor5", (ProgItemRule("Progressive Armor", 45) | armor45) & can_beat_boss0)
        world.get_region("Bit Armor").connect(world.get_region("Byte Armor"), "Armor6", (ProgItemRule("Progressive Armor", 65) | armor65) & can_beat_boss1)
        world.get_region("Byte Armor").connect(world.get_region("Net Armor"), "Armor7", ((ProgItemRule("Progressive Armor", 95) | armor95) & has_crypto_mine) & can_beat_boss5)
        world.get_region("Byte Armor").connect(world.get_region("Focus Armor"), "FocusArmor1", (ProgItemRule("Progressive Armor", 95) | armor95) & can_beat_boss6)
        world.get_region("Byte Armor").connect(world.get_region("Blood Armor"), "MaxHealthToArmor1", (ProgItemRule("Progressive Armor", 95) | armor95) & has_access_to_blue_enemies)
        world.get_region("Blood Armor").connect(world.get_region("Blood Visage"), "MaxHealthToArmor2", (ProgItemRule("Progressive Armor", 110) | armor110) & has_crypto_mine & can_beat_boss8)
        world.get_region("B.I.G.").connect(world.get_region("Auto-Collect"), "AutoCollect", has_access_to_blue_enemies & can_beat_boss13)
        world.get_region("Crypto Mine").connect(world.get_region("Processor Acquisition"), "YellowSpawn1", has_crypto_mine & can_beat_boss2)
        world.get_region("Crypto Mine").connect(world.get_region("Crypto Levels"), "CryptoLevel", has_crypto_mine & has_access_to_yellow_enemies)
        world.get_region("Node Finder").connect(world.get_region("Node Boost"), "NodeBoost1")
        world.get_region("Node Finder").connect(world.get_region("Milestones"), "Milestones", has_access_to_blue_enemies)
        world.get_region("Node Finder").connect(world.get_region("Spawn Exploders"), "ExplodersUpgrades", has_access_to_blue_enemies)
        world.get_region("Unending Parasite").connect(world.get_region("Parasite Evolution"), "StealMaxHealth2", has_access_to_blue_enemies)
        world.get_region("Parasite Evolution").connect(world.get_region("Indomitable"), "Health6", has_access_to_blue_enemies)
        world.get_region("Parasite Evolution").connect(world.get_region("Insatiable"), "StealMaxHealth3", can_beat_boss8)
        world.get_region("Indomitable").connect(world.get_region("Beyond"), "Health7", (ProgItemRule("Progressive Health", 265936) | health265936) & can_beat_boss10)
        world.get_region("Beyond").connect(world.get_region("Infinity"), "Infinity", has_access_to_blue_enemies)
        world.get_region("Auto Pulser").connect(world.get_region("Pulser Pursuit"), "MovingPulserSpeed1", has_access_to_blue_enemies)
        world.get_region("Auto Pulser").connect(world.get_region("Pulse Thumper"), "MovingPulserSize1", has_access_to_blue_enemies)
        world.get_region("Netblade").connect(world.get_region("Bloodblade"), "MaxHealthToDamage1", can_beat_boss10)
        world.get_region("Netblade").connect(world.get_region("Thundering"), "LightningDamage1", has_access_to_blue_enemies)
        world.get_region("Transplant").connect(world.get_region("Blood Injection"), "Health5", can_beat_boss5)
        world.get_region("Blood Injection").connect(world.get_region("Instant Repair"), "MaxHealthHeal2")
        world.get_region("Blood Injection").connect(world.get_region("Unending Parasite"), "StealMaxHealth1", has_access_to_blue_enemies)
        world.get_region("Boss Drops").connect(world.get_region("Prestige 0"), "BossDrop0")
        world.get_region("Prestige 0").connect(world.get_region("Prestige 1"), "BossDrop1")
        world.get_region("Prestige 1").connect(world.get_region("Prestige 2"), "BossDrop2")
        world.get_region("Prestige 2").connect(world.get_region("Prestige 3"), "BossDrop3")
        world.get_region("Prestige 3").connect(world.get_region("Prestige 4"), "BossDrop4")
        world.get_region("Prestige 4").connect(world.get_region("Prestige 5"), "BossDrop5")
        world.get_region("Prestige 5").connect(world.get_region("Prestige 6"), "BossDrop6")
        world.get_region("Prestige 6").connect(world.get_region("Prestige 7"), "BossDrop7")
        world.get_region("Prestige 7").connect(world.get_region("Prestige 8"), "BossDrop8")
        world.get_region("Prestige 8").connect(world.get_region("Prestige 9"), "BossDrop9")
        world.get_region("Prestige 9").connect(world.get_region("Prestige 10"), "BossDrop10")
        world.get_region("Prestige 10").connect(world.get_region("Prestige 11"), "BossDrop11")
        world.get_region("Prestige 11").connect(world.get_region("Prestige 12"), "BossDrop12")
        world.get_region("Prestige 12").connect(world.get_region("Prestige 13"), "BossDrop13")
        world.get_region("Prestige 13").connect(world.get_region("Prestige 14"), "BossDrop14")
        world.get_region("Prestige 14").connect(world.get_region("Prestige 15"), "BossDrop15")
        world.get_region("Prestige 15").connect(world.get_region("Prestige 16"), "BossDrop16")
        world.get_region("Prestige 16").connect(world.get_region("Prestige 17"), "BossDrop17")
        world.get_region("Prestige 17").connect(world.get_region("Prestige 18"), "BossDrop18")
        world.get_region("Prestige 18").connect(world.get_region("Prestige 19"), "BossDrop19")
        world.get_region("Prestige 19").connect(world.get_region("Prestige 20"), "BossDrop20")
        world.get_region("Prestige 20").connect(world.get_region("Prestige 21"), "BossDrop21")
        world.get_region("Prestige 21").connect(world.get_region("Prestige 22"), "BossDrop22")
        world.get_region("Prestige 22").connect(world.get_region("Prestige 23"), "BossDrop23")
        world.get_region("Prestige 23").connect(world.get_region("Prestige 24"), "BossDrop24")
        world.get_region("Prestige 24").connect(world.get_region("Prestige 25"), "BossDrop25")
        world.get_region("Milestone Page").connect(world.get_region("Red Milestones"), "Red Milestones", can_start_red_milestones)
        world.get_region("Milestone Page").connect(world.get_region("Blue Milestones"), "Blue Milestones", can_start_blue_milestones)
        world.get_region("Milestone Page").connect(world.get_region("Yellow Milestones"), "Yellow Milestones", can_start_yellow_milestones)
        world.get_region("Infinity").connect(world.get_region("Epilogue"), "Goal", can_release_virus)

def get_upgrade_connection_rules_lookup(world, player: int) -> dict:
    '''
    Create rules for regions based on the upgrade node connections and unlock logic.

    :param world:
    :param player:
    :return:
    '''
    rules_lookup = {
        "Crowding": (ProgItemRule("Progressive Damage", 1) | damage1),
        "Firewall": (ProgItemRule("Progressive Health", 1) | health1),
        "Repair Tool": (ProgItemRule("Progressive Health", 1) | health1),
        "Potency": (ProgItemRule("Progressive Damage", 31) | damage31),
        "Nodeblade": (ProgItemRule("Progressive Damage", 91) | damage91),
        "First Strike": (ProgItemRule("Progressive Damage", 37) | damage37),
        "Crit Chance": (ProgItemRule("Progressive Damage", 37) | damage37),
        "Crit Damage": Has("CritChance1"),
        "Big Crit":(ProgItemRule("Progressive Critical Damage", 50) | critdamage50),
        "Netblade": (ProgItemRule("Progressive Damage", 166) | damage166),
        "Giant Slayer": (ProgItemRule("Progressive Additional Damage", 1) | addidamage1),
        "Repeating": (ProgItemRule("Progressive Additional Damage", 1) | addidamage1),
        "Finishing Blow": (ProgItemRule("Progressive Additional Damage", 17) | addidamage17),
        "Beyond": (ProgItemRule("Progressive Health", 265936) | health265936),
        "Sapper": (ProgItemRule("Progressive Lifesteal", 1) | lifesteal1),
        "Skilled Salvager": (ProgItemRule("Progressive Lifesteal", 5) | lifesteal5),
        "Patcher": (ProgItemRule("Progressive Lifesteal", 51) | lifesteal51),
        "Better Endurance": (ProgItemRule("Progressive Lifesteal", 1) | lifesteal1) or (ProgItemRule("Progressive Boss Armor", 1) | bossarmor1),
        "Drainer": (ProgItemRule("Progressive Regen", 17) | regen17),
        "Bit Boost": (ProgItemRule("Progressive SpawnRate", 1) | spawnrate1),
        "Last Strike": (ProgItemRule("Progressive Additional Damage", 6) | addidamage6),
        "Influence": (ProgItemRule("Progressive SpawnRate", 1) | spawnrate1),
        "Swarming": (ProgItemRule("Progressive SpawnRate", 1) | spawnrate1),
        "Infesting": (ProgItemRule("Progressive SpawnRate", 950) | spawnrate950),
        "Overloaded": (ProgItemRule("Progressive SpawnRate", 1450) | spawnrate1450),
        "Antivirus": (ProgItemRule("Progressive Armor", 10) | armor10),
        "Swarm Defense System": (ProgItemRule("Progressive Armor", 11) | armor11),
        "Bolster": (ProgItemRule("Progressive Armor", 15) | armor15),
        "Super Armor": (ProgItemRule("Progressive Armor", 35) | armor35),
        "Anti-Purple": (ProgItemRule("Progressive Armor", 36) | armor36),
        "Bit Armor": (ProgItemRule("Progressive Armor", 45) | armor45),
        "Byte Armor": (ProgItemRule("Progressive Armor", 65) | armor65),
        "Blood Armor": (ProgItemRule("Progressive Armor", 95) | armor95),
        "Net Armor": (ProgItemRule("Progressive Armor", 95) | armor95),
        "Focus Armor": (ProgItemRule("Progressive Armor", 95) | armor95),
        "Blood Visage": (ProgItemRule("Progressive Armor", 110) | armor110),
        "Domain Expansion": (ProgItemRule("Progressive SpawnRate", 1050) | spawnrate1050),
        "Processor Acquisition": has_crypto_mine,
        # TODO: If these upgrades are considered progressive, add these rules back
        #"Plundering": lambda state: state.has("BitBoost1", player),
        #"Node Finder": lambda state: state.has("BitBoost1", player),
        #"Magnet": lambda state: state.has("Size1", player),
        #"B.I.G.": lambda state: state.has("Size2", player),
        #"Crypto Mine": lambda state: state.has_all("Size2", player),
        #"Auto-Collect": lambda state: state.has("Size3", player),
        "Bolt Damage": Has("PulseBolts"),
        "Bolt Count": Has("PulseBolts"),
        "Bolt Burst": Has("PulseBoltDamage1"),
        "Bolt Barrage": Has("PulseBoltCount2"),
        "Bolt Lethality": HasAny("PulseBoltExplode", "PulseBoltCount2"),
    }
    return rules_lookup

def set_nodebuster_connections(world: NodebusterWorld) -> None:
    player = world.player
    for starter, connections in nodebuster_regions_all.items():
        r = world.get_region(starter)
        for conn in connections:
            c = world.get_region(conn)
            #world.create_entrance(r, c)
            #r.connect(c)
    set_region_rules(world, player)


def set_nodebuster_rules(world: NodebusterWorld) -> None:
    player = world.player

    location_rules_lookup = get_location_rules_lookup(world, player)
    for location_name, rule in location_rules_lookup.items():
        world.set_rule(world.get_location(location_name), rule)

    # Goal
    world.set_completion_rule(released_virus)