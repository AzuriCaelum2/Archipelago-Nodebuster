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
has_crypto_mine = Has("Crypto Mine")
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

damage1 = HasAny("Damage1", "Damage2", "Damage3", "Damage4", "Damage5")
damage10 = (HasAny("Damage4", "Damage5") |
            Has("Damage3", 2) |
            (Has("Damage3") & (HasAll("Damage2", "Damage1") |
                              Has("Damage1", 4))) |
            Has("Damage2", 4) |
            (HasAllCounts({"Damage2": 3, "Damage1": 1}) |
             HasAllCounts({"Damage2": 2, "Damage1": 4}) |
             HasAllCounts({"Damage2": 1, "Damage1": 7}) |
             Has("Damage1", 10)))
damage15 = (HasAny("Damage4", "Damage5") |
            (Has("Damage3", 3)) |
            (Has("Damage3", 2) & (Has("Damage2") |
                                  Has("Damage1", 3))) |
            (Has("Damage3", 1) & (Has("Damage2", 3) |
                                  HasAllCounts({"Damage2": 2, "Damage1": 3}) |
                                  HasAllCounts({"Damage2": 1, "Damage1": 6}) |
                                  Has("Damage1", 9))) |
            (Has("Damage2", 5)) |
            (HasAllCounts({"Damage2": 4, "Damage1": 3})) |
            (HasAllCounts({"Damage2": 3, "Damage1": 6})) |
            (HasAllCounts({"Damage2": 2, "Damage1": 9})) |
            (HasAllCounts({"Damage2": 1, "Damage1": 12})) |
            (Has("Damage1", 15)))
damage31 = (Has("Damage5") |
            HasAllCounts({"Damage4": 1, "Damage3": 1}) |
            HasAllCounts({"Damage4": 1, "Damage2": 2}) |
            HasAllCounts({"Damage4": 1, "Damage1": 6}) |
            (Has("Damage3", 4) & HasAny("Damage2", "Damage1")) |
            (Has("Damage3", 3) & (Has("Damage2", 5) |
                                  HasAllCounts({"Damage2": 4, "Damage1": 1}) |
                                  HasAllCounts({"Damage2": 3, "Damage1": 4}) |
                                  HasAllCounts({"Damage2": 2, "Damage1": 7}) |
                                  HasAllCounts({"Damage2": 1, "Damage1": 10}) |
                                  Has("Damage1", 13))) |
            (Has("Damage3", 2) & (Has("Damage2", 7) |
                                  HasAllCounts({"Damage2": 6, "Damage1": 1}) |
                                  HasAllCounts({"Damage2": 5, "Damage1": 4}) |
                                  HasAllCounts({"Damage2": 4, "Damage1": 7}) |
                                  HasAllCounts({"Damage2": 3, "Damage1": 10}) |
                                  HasAllCounts({"Damage2": 2, "Damage1": 13}))) |
            (Has("Damage3", 1) & (Has("Damage2", 9) |
                                  HasAllCounts({"Damage2": 8, "Damage1": 1}) |
                                  HasAllCounts({"Damage2": 7, "Damage1": 4}) |
                                  HasAllCounts({"Damage2": 6, "Damage1": 7}) |
                                  HasAllCounts({"Damage2": 5, "Damage1": 10}) |
                                  HasAllCounts({"Damage2": 4, "Damage1": 13}))) |
            Has("Damage2", 11) |
            HasAllCounts({"Damage2": 10, "Damage1": 1}) |
            HasAllCounts({"Damage2": 9, "Damage1": 4}) |
            HasAllCounts({"Damage2": 8, "Damage1": 7}) |
            HasAllCounts({"Damage2": 7, "Damage1": 10}) |
            HasAllCounts({"Damage2": 6, "Damage1": 13}))
damage37 = (Has("Damage5") |
            Has("Damage4", 2) |
           (Has("Damage4", 1) & (Has("Damage3", 2) |
                                 Has("Damage3", 1) & (Has("Damage2", 2) |
                                                     (Has("Damage2", 1) & Has("Damage1", 3)) |
                                                      Has("Damage1", 6)) |
                                 Has("Damage2", 4) |
                                 HasAllCounts({"Damage2": 3, "Damage1": 3}) |
                                 HasAllCounts({"Damage2": 2, "Damage1": 6}) |
                                 HasAllCounts({"Damage2": 1, "Damage1": 9}))) |
            Has("Damage3", 7) |
           (Has("Damage3", 6) & HasAny("Damage1", "Damage2")) |
           (Has("Damage3", 5) & (Has("Damage2", 3) |
                                 HasAllCounts({"Damage2": 2, "Damage1": 1}) |
                                 HasAllCounts({"Damage2": 1, "Damage1": 4}) |
                                 Has("Damage1", 7))) |
           (Has("Damage3", 4) & (Has("Damage2", 5) |
                                 HasAllCounts({"Damage2": 4, "Damage1": 1}) |
                                 HasAllCounts({"Damage2": 3, "Damage1": 4}) |
                                 HasAllCounts({"Damage2": 2, "Damage1": 7}) |
                                 HasAllCounts({"Damage2": 1, "Damage1": 10}) |
                                 Has("Damage1", 13))) |
           (Has("Damage3", 3) & (Has("Damage2", 7) |
                                 HasAllCounts({"Damage2": 6, "Damage1": 4}) |
                                 HasAllCounts({"Damage2": 5, "Damage1": 7}) |
                                 HasAllCounts({"Damage2": 4, "Damage1": 10}) |
                                 HasAllCounts({"Damage2": 3, "Damage1": 13}))) |
           (Has("Damage3", 2) & (Has("Damage2", 9) |
                                 HasAllCounts({"Damage2": 8, "Damage1": 1}) |
                                 HasAllCounts({"Damage2": 7, "Damage1": 4}) |
                                 HasAllCounts({"Damage2": 6, "Damage1": 7}) |
                                 HasAllCounts({"Damage2": 5, "Damage1": 10}))) |
           (Has("Damage3", 1) & (HasAllCounts({"Damage2": 10, "Damage1": 1}) |
                                 HasAllCounts({"Damage2": 9, "Damage1": 4}) |
                                 HasAllCounts({"Damage2": 8, "Damage1": 7}) |
                                 HasAllCounts({"Damage2": 7, "Damage1": 10}) |
                                 HasAllCounts({"Damage2": 6, "Damage1": 13}))) |
            HasAllCounts({"Damage3": 10, "Damage1": 7}) |
            HasAllCounts({"Damage3": 9, "Damage1": 10}) |
            HasAllCounts({"Damage3": 8, "Damage1": 13}))
damage45 = (Has("Damage5") |
            (Has("Damage4", 2)) |
            (Has("Damage4", 1) & (Has("Damage3", 4)) |
                                  (Has("Damage3", 3) & HasAny("Damage2", "Damage1")) |
                                  (Has("Damage3", 2) & (Has("Damage2", 3) |
                                                        HasAllCounts({"Damage2": 2, "Damage1": 2}) |
                                                        HasAllCounts({"Damage2": 1, "Damage1": 5}) |
                                                        Has("Damage1", 8))) |
                                  (Has("Damage3", 1) & (Has("Damage2", 5) |
                                                        HasAllCounts({"Damage2": 4, "Damage1": 2}) |
                                                        HasAllCounts({"Damage2": 3, "Damage1": 5}) |
                                                        HasAllCounts({"Damage2": 2, "Damage1": 8}) |
                                                        HasAllCounts({"Damage2": 1, "Damage1": 11}) |
                                                        Has("Damage1", 14))) |
                                  (Has("Damage2", 7)) |
                                  (HasAllCounts({"Damage2": 6, "Damage1": 2})) |
                                  (HasAllCounts({"Damage2": 6, "Damage1": 2})) |
                                  (HasAllCounts({"Damage2": 6, "Damage1": 2})) |
                                  (HasAllCounts({"Damage2": 6, "Damage1": 2})) |
                                  (HasAllCounts({"Damage2": 6, "Damage1": 2}))) |
            (Has("Damage3", 8)) |
            (Has("Damage3", 7) & (Has("Damage2") |
                                  Has("Damage1", 3))) |
            (Has("Damage3", 6) & (Has("Damage2", 3) |
                                  HasAllCounts({"Damage2": 2, "Damage1": 3}) |
                                  HasAllCounts({"Damage2": 1, "Damage1": 6}) |
                                  Has("Damage1", 9))) |
            (Has("Damage3", 5) & (Has("Damage2", 5) |
                                  HasAllCounts({"Damage2": 4, "Damage1": 3}) |
                                  HasAllCounts({"Damage2": 3, "Damage1": 6}) |
                                  HasAllCounts({"Damage2": 2, "Damage1": 9}) |
                                  HasAllCounts({"Damage2": 1, "Damage1": 12}) |
                                  Has("Damage1", 15))) |
            (Has("Damage3", 4) & (Has("Damage2", 7) |
                                  HasAllCounts({"Damage2": 6, "Damage1": 3}) |
                                  HasAllCounts({"Damage2": 5, "Damage1": 6}) |
                                  HasAllCounts({"Damage2": 4, "Damage1": 9}) |
                                  HasAllCounts({"Damage2": 3, "Damage1": 12}) |
                                  HasAllCounts({"Damage2": 2, "Damage1": 15}))) |
            (Has("Damage3", 3) & (Has("Damage2", 9) |
                                  HasAllCounts({"Damage2": 8, "Damage1": 3}) |
                                  HasAllCounts({"Damage2": 7, "Damage1": 6}) |
                                  HasAllCounts({"Damage2": 6, "Damage1": 9}) |
                                  HasAllCounts({"Damage2": 5, "Damage1": 12}) |
                                  HasAllCounts({"Damage2": 4, "Damage1": 15}))) |
            (Has("Damage3", 2) & (HasAllCounts({"Damage2": 10, "Damage1": 3}) |
                                  HasAllCounts({"Damage2": 9, "Damage1": 6}) |
                                  HasAllCounts({"Damage2": 8, "Damage1": 9}) |
                                  HasAllCounts({"Damage2": 7, "Damage1": 12}) |
                                  HasAllCounts({"Damage2": 6, "Damage1": 15}))) |
            (Has("Damage3", 1) & (HasAllCounts({"Damage2": 10, "Damage1": 9}) |
                                  HasAllCounts({"Damage2": 9, "Damage1": 12}) |
                                  HasAllCounts({"Damage2": 8, "Damage1": 15}))) |
            HasAllCounts({"Damage2": 10, "Damage1": 15}))
damage63 = (Has("Damage5") |
            (Has("Damage4", 3)) |
            (Has("Damage4", 2) & (Has("Damage3", 3)) |
                                  (Has("Damage3", 2) & HasAny("Damage2", "Damage1")) |
                                  (Has("Damage3", 1) & (Has("Damage2", 3) |
                                                        HasAllCounts({"Damage2": 2, "Damage1": 3}) |
                                                        HasAllCounts({"Damage2": 1, "Damage1": 6}) |
                                                        Has("Damage1", 9))) |
                                  (Has("Damage2", 5)) |
                                  (HasAllCounts({"Damage2": 4, "Damage1": 1})) |
                                  (HasAllCounts({"Damage2": 3, "Damage1": 4})) |
                                  (HasAllCounts({"Damage2": 2, "Damage1": 7})) |
                                  (HasAllCounts({"Damage2": 1, "Damage1": 10})) |
                                  (Has("Damage1", 13))) |
            (Has("Damage4") & (Has("Damage3", 7) |
                               Has("Damage3", 6) & (Has("Damage2") |
                                                    Has("Damage1", 2)) |
                               Has("Damage3", 5) & (Has("Damage2", 3) |
                                                    HasAllCounts({"Damage2": 2, "Damage1": 2}) |
                                                    HasAllCounts({"Damage2": 1, "Damage1": 5}) |
                                                    Has("Damage1", 8)) |
                               Has("Damage3", 4) & (Has("Damage2", 5) |
                                                    HasAllCounts({"Damage2": 4, "Damage1": 2}) |
                                                    HasAllCounts({"Damage2": 3, "Damage1": 5}) |
                                                    HasAllCounts({"Damage2": 2, "Damage1": 8}) |
                                                    HasAllCounts({"Damage2": 1, "Damage1": 11}) |
                                                    Has("Damage1", 14)) |
                               Has("Damage3", 3) & (Has("Damage2", 7) |
                                                    HasAllCounts({"Damage2": 6, "Damage1": 2}) |
                                                    HasAllCounts({"Damage2": 5, "Damage1": 5}) |
                                                    HasAllCounts({"Damage2": 4, "Damage1": 8}) |
                                                    HasAllCounts({"Damage2": 3, "Damage1": 11}) |
                                                    HasAllCounts({"Damage2": 2, "Damage1": 14})) |
                               Has("Damage3", 2) & (Has("Damage2", 9) |
                                                    HasAllCounts({"Damage2": 8, "Damage1": 2}) |
                                                    HasAllCounts({"Damage2": 7, "Damage1": 5}) |
                                                    HasAllCounts({"Damage2": 6, "Damage1": 8}) |
                                                    HasAllCounts({"Damage2": 5, "Damage1": 11}) |
                                                    HasAllCounts({"Damage2": 4, "Damage1": 14})) |
                               Has("Damage3", 1) & (HasAllCounts({"Damage2": 10, "Damage1": 2}) |
                                                    HasAllCounts({"Damage2": 9, "Damage1": 5}) |
                                                    HasAllCounts({"Damage2": 8, "Damage1": 8}) |
                                                    HasAllCounts({"Damage2": 7, "Damage1": 11}) |
                                                    HasAllCounts({"Damage2": 6, "Damage1": 14})) |
                               HasAllCounts({"Damage2": 10, "Damage1": 8}) |
                               HasAllCounts({"Damage2": 9, "Damage1": 11}) |
                               HasAllCounts({"Damage2": 8, "Damage1": 14}))) |
            (Has("Damage3", 10) & (Has("Damage2") |
                                   Has("Damage1", 3))) |
            (Has("Damage3", 9) & (Has("Damage2", 3) |
                                  HasAllCounts({"Damage2": 2, "Damage1": 3}) |
                                  HasAllCounts({"Damage2": 1, "Damage1": 6}) |
                                  Has("Damage1", 9))) |
            (Has("Damage3", 8) & (Has("Damage2", 5) |
                                   HasAllCounts({"Damage2": 4, "Damage1": 3}) |
                                   HasAllCounts({"Damage2": 3, "Damage1": 6}) |
                                   HasAllCounts({"Damage2": 2, "Damage1": 9}) |
                                   HasAllCounts({"Damage2": 1, "Damage1": 12}) |
                                   Has("Damage1", 15))) |
            (Has("Damage3", 7) & (Has("Damage2", 7) |
                                   HasAllCounts({"Damage2": 6, "Damage1": 3}) |
                                   HasAllCounts({"Damage2": 5, "Damage1": 6}) |
                                   HasAllCounts({"Damage2": 4, "Damage1": 9}) |
                                   HasAllCounts({"Damage2": 3, "Damage1": 12}) |
                                   HasAllCounts({"Damage2": 2, "Damage1": 15}))) |
            (Has("Damage3", 6) & (Has("Damage2", 9) |
                                  HasAllCounts({"Damage2": 8, "Damage1": 3}) |
                                  HasAllCounts({"Damage2": 7, "Damage1": 6}) |
                                  HasAllCounts({"Damage2": 6, "Damage1": 9}) |
                                  HasAllCounts({"Damage2": 5, "Damage1": 12}) |
                                  HasAllCounts({"Damage2": 4, "Damage1": 15}))) |
            (Has("Damage3", 5) & (HasAllCounts({"Damage2": 10, "Damage1": 3}) |
                                  HasAllCounts({"Damage2": 9, "Damage1": 6}) |
                                  HasAllCounts({"Damage2": 8, "Damage1": 9}) |
                                  HasAllCounts({"Damage2": 7, "Damage1": 12}) |
                                  HasAllCounts({"Damage2": 6, "Damage1": 15}))) |
            (Has("Damage3", 4) & (HasAllCounts({"Damage2": 10, "Damage1": 9}) |
                                  HasAllCounts({"Damage2": 9, "Damage1": 12}) |
                                  HasAllCounts({"Damage2": 8, "Damage1": 15}))) |
            (HasAllCounts({"Damage3": 3, "Damage2": 10, "Damage1": 15})))
damage81 = (Has("Damage5") |
           (Has("Damage4", 3) & (Has("Damage3") |
                                 Has("Damage2", 2) |
                                 HasAllCounts({"Damage2": 1, "Damage1": 3}) |
                                 Has("Damage1", 6))) |
           (Has("Damage4", 2) & (Has("Damage3", 6)) |
                                 (Has("Damage3", 5) & HasAny("Damage2", "Damage1")) |
                                 (Has("Damage3", 4) & (Has("Damage2", 3) |
                                                       (HasAllCounts({"Damage2": 2, "Damage1": 1}) |
                                                        HasAllCounts({"Damage2": 1, "Damage1": 4}) |
                                                        Has("Damage1", 7)))) |
                                 (Has("Damage3", 3) & (Has("Damage2", 5) |
                                                       HasAllCounts({"Damage2": 4, "Damage1": 1}) |
                                                       HasAllCounts({"Damage2": 3, "Damage1": 4}) |
                                                       HasAllCounts({"Damage2": 2, "Damage1": 7}) |
                                                       HasAllCounts({"Damage2": 1, "Damage1": 10}) |
                                                       Has("Damage1", 13))) |
                                 (Has("Damage3", 2) & (Has("Damage2", 7) |
                                                       HasAllCounts({"Damage2": 6, "Damage1": 1}) |
                                                       HasAllCounts({"Damage2": 5, "Damage1": 4}) |
                                                       HasAllCounts({"Damage2": 4, "Damage1": 7}) |
                                                       HasAllCounts({"Damage2": 3, "Damage1": 10}) |
                                                       HasAllCounts({"Damage2": 2, "Damage1": 13}))) |
                                 (Has("Damage3", 1) & (Has("Damage2", 9) |
                                                       HasAllCounts({"Damage2": 8, "Damage1": 1}) |
                                                       HasAllCounts({"Damage2": 7, "Damage1": 4}) |
                                                       HasAllCounts({"Damage2": 6, "Damage1": 7}) |
                                                       HasAllCounts({"Damage2": 5, "Damage1": 10}) |
                                                       HasAllCounts({"Damage2": 4, "Damage1": 13}))) |
                                 HasAllCounts({"Damage2": 10, "Damage1": 1}) |
                                 HasAllCounts({"Damage2": 9, "Damage1": 4}) |
                                 HasAllCounts({"Damage2": 8, "Damage1": 7}) |
                                 HasAllCounts({"Damage2": 7, "Damage1": 10}) |
                                 HasAllCounts({"Damage2": 6, "Damage1": 13})) |
            (Has("Damage4", 1) & (Has("Damage3", 10) |
                                  (Has("Damage3", 9) & (Has("Damage2") |
                                                        Has("Damage1", 2))) |
                                  (Has("Damage3", 8) & (Has("Damage2", 3) |
                                                        HasAllCounts({"Damage2": 2, "Damage1": 2}) |
                                                        HasAllCounts({"Damage2": 1, "Damage1": 5}) |
                                                        Has("Damage1", 8))) |
                                  (Has("Damage3", 7) & (Has("Damage2", 5) |
                                                        HasAllCounts({"Damage2": 4, "Damage1": 2}) |
                                                        HasAllCounts({"Damage2": 3, "Damage1": 5}) |
                                                        HasAllCounts({"Damage2": 2, "Damage1": 8}) |
                                                        HasAllCounts({"Damage2": 1, "Damage1": 11}) |
                                                        Has("Damage1", 14))) |
                                  (Has("Damage3", 6) & (Has("Damage2", 7) |
                                                        HasAllCounts({"Damage2": 6, "Damage1": 2}) |
                                                        HasAllCounts({"Damage2": 5, "Damage1": 5}) |
                                                        HasAllCounts({"Damage2": 4, "Damage1": 8}) |
                                                        HasAllCounts({"Damage2": 3, "Damage1": 11}) |
                                                        HasAllCounts({"Damage2": 2, "Damage1": 14}))) |
                                  (Has("Damage3", 5) & (Has("Damage2", 9) |
                                                        HasAllCounts({"Damage2": 8, "Damage1": 2}) |
                                                        HasAllCounts({"Damage2": 7, "Damage1": 5}) |
                                                        HasAllCounts({"Damage2": 6, "Damage1": 8}) |
                                                        HasAllCounts({"Damage2": 5, "Damage1": 11}) |
                                                        HasAllCounts({"Damage2": 4, "Damage1": 14}))) |
                                  (Has("Damage3", 4) & (HasAllCounts({"Damage2": 10, "Damage1": 2}) |
                                                        HasAllCounts({"Damage2": 9, "Damage1": 5}) |
                                                        HasAllCounts({"Damage2": 8, "Damage1": 8}) |
                                                        HasAllCounts({"Damage2": 7, "Damage1": 11}) |
                                                        HasAllCounts({"Damage2": 6, "Damage1": 14}))) |
                                  (Has("Damage3", 3) & (HasAllCounts({"Damage2": 10, "Damage1": 8}) |
                                                        HasAllCounts({"Damage2": 9, "Damage1": 11}) |
                                                        HasAllCounts({"Damage2": 8, "Damage1": 14}))) |
                                  (Has("Damage3", 2) & (HasAllCounts({"Damage2": 10, "Damage1": 14})))) |
             (Has("Damage3", 10) & (Has("Damage2", 7) |
                                   HasAllCounts({"Damage2": 6, "Damage1": 3}) |
                                    HasAllCounts({"Damage2": 5, "Damage1": 6}) |
                                    HasAllCounts({"Damage2": 4, "Damage1": 9}) |
                                    HasAllCounts({"Damage2": 3, "Damage1": 12}) |
                                    HasAllCounts({"Damage2": 2, "Damage1": 15}))) |
             (Has("Damage3", 9) & (Has("Damage2", 9) |
                                   HasAllCounts({"Damage2": 8, "Damage1": 3}) |
                                   HasAllCounts({"Damage2": 7, "Damage1": 6}) |
                                   HasAllCounts({"Damage2": 6, "Damage1": 9}) |
                                   HasAllCounts({"Damage2": 5, "Damage1": 12}) |
                                   HasAllCounts({"Damage2": 4, "Damage1": 15}))) |
             (Has("Damage3", 8) & (HasAllCounts({"Damage2": 10, "Damage1": 6}) |
                                   HasAllCounts({"Damage2": 9, "Damage1": 9}) |
                                   HasAllCounts({"Damage2": 8, "Damage1": 12}) |
                                   HasAllCounts({"Damage2": 7, "Damage1": 15}))) |
             (Has("Damage3", 7) & (HasAllCounts({"Damage2": 10, "Damage1": 9}) |
                                   HasAllCounts({"Damage2": 9, "Damage1": 12}) |
                                   HasAllCounts({"Damage2": 8, "Damage1": 15}))) |
             HasAllCounts({"Damage3": 6, "Damage2": 10, "Damage1": 15})))
damage91 = (Has("Damage5") |
           (Has("Damage4", 3) & (Has("Damage3", 3)) |
                                (Has("Damage3", 2) & (HasAll("Damage1", "Damage2") |
                                                      Has("Damage1", 4)) |
                                 Has("Damage3", 1) & (HasAllCounts({"Damage3": 3, "Damage1": 1}) |
                                                      HasAllCounts({"Damage3": 2, "Damage1": 4}) |
                                                      HasAllCounts({"Damage3": 1, "Damage1": 7}) |
                                                      Has("Damage1", 10)))) |
           (Has("Damage4", 2) & (Has("Damage3", 7) |
                                (Has("Damage3", 6) & (Has("Damage2", 2) |
                                                     (HasAllCounts({"Damage2": 1, "Damage1": 2}) |
                                                      Has("Damage1", 5)))) |
                                (Has("Damage3", 5) & (Has("Damage2", 4) |
                                                      HasAllCounts({"Damage2": 3, "Damage1": 2}) |
                                                      HasAllCounts({"Damage2": 2, "Damage1": 5}) |
                                                      HasAllCounts({"Damage2": 1, "Damage1": 8}))) |
                                (Has("Damage3", 4) & (Has("Damage2", 6) |
                                                       HasAllCounts({"Damage2": 5, "Damage1": 2}) |
                                                       HasAllCounts({"Damage2": 4, "Damage1": 5}) |
                                                       HasAllCounts({"Damage2": 3, "Damage1": 8}) |
                                                       HasAllCounts({"Damage2": 2, "Damage1": 11}) |
                                                       HasAllCounts({"Damage2": 1, "Damage1": 14}))) |
                                (Has("Damage3", 3) & (Has("Damage2", 8) |
                                                      HasAllCounts({"Damage2": 7, "Damage1": 2}) |
                                                      HasAllCounts({"Damage2": 6, "Damage1": 5}) |
                                                      HasAllCounts({"Damage2": 5, "Damage1": 8}) |
                                                      HasAllCounts({"Damage2": 4, "Damage1": 11}) |
                                                      HasAllCounts({"Damage2": 3, "Damage1": 14}))) |
                                (Has("Damage3", 2) & (Has("Damage2", 10) |
                                                      HasAllCounts({"Damage2": 9, "Damage1": 2}) |
                                                      HasAllCounts({"Damage2": 8, "Damage1": 5}) |
                                                      HasAllCounts({"Damage2": 7, "Damage1": 8}) |
                                                      HasAllCounts({"Damage2": 6, "Damage1": 11}) |
                                                      HasAllCounts({"Damage2": 5, "Damage1": 14}))) |
                                (Has("Damage3", 1) & (HasAllCounts({"Damage2": 10, "Damage1": 5}) |
                                                      HasAllCounts({"Damage2": 9, "Damage1": 8}) |
                                                      HasAllCounts({"Damage2": 8, "Damage1": 11}) |
                                                      HasAllCounts({"Damage2": 7, "Damage1": 14}))) |
                                 HasAllCounts({"Damage2": 10, "Damage1": 11}) |
                                 HasAllCounts({"Damage2": 9, "Damage1": 14}))) |
           (Has("Damage4", 1) & (Has("Damage3", 10) & (Has("Damage2", 2) |
                                                       HasAllCounts({"Damage2": 1, "Damage1": 3}) |
                                                       Has("Damage1", 6))) |
                                (Has("Damage3", 9) & (Has("Damage2", 4) |
                                                      HasAllCounts({"Damage2": 3, "Damage1": 3}) |
                                                      HasAllCounts({"Damage2": 2, "Damage1": 6}) |
                                                      HasAllCounts({"Damage2": 1, "Damage1": 9}) |
                                                      Has("Damage1", 12))) |
                                (Has("Damage3", 8) & (Has("Damage2", 6) |
                                                      HasAllCounts({"Damage2": 5, "Damage1": 3}) |
                                                      HasAllCounts({"Damage2": 4, "Damage1": 6}) |
                                                      HasAllCounts({"Damage2": 3, "Damage1": 9}) |
                                                      HasAllCounts({"Damage2": 2, "Damage1": 12}) |
                                                      HasAllCounts({"Damage2": 1, "Damage1": 15}))) |
                                (Has("Damage3", 7) & (Has("Damage2", 8) |
                                                      HasAllCounts({"Damage2": 7, "Damage1": 3}) |
                                                      HasAllCounts({"Damage2": 6, "Damage1": 6}) |
                                                      HasAllCounts({"Damage2": 5, "Damage1": 9}) |
                                                      HasAllCounts({"Damage2": 4, "Damage1": 12}) |
                                                      HasAllCounts({"Damage2": 3, "Damage1": 15}))) |
                                (Has("Damage3", 6) & (Has("Damage2", 10) |
                                                      HasAllCounts({"Damage2": 9, "Damage1": 3}) |
                                                      HasAllCounts({"Damage2": 8, "Damage1": 6}) |
                                                      HasAllCounts({"Damage2": 7, "Damage1": 9}) |
                                                      HasAllCounts({"Damage2": 6, "Damage1": 12}) |
                                                      HasAllCounts({"Damage2": 5, "Damage1": 15})))) |
           (Has("Damage3", 10) & (HasAllCounts({"Damage2": 10, "Damage1": 1}) |
                                   HasAllCounts({"Damage2": 9, "Damage1": 4}) |
                                   HasAllCounts({"Damage2": 8, "Damage1": 7}) |
                                   HasAllCounts({"Damage2": 7, "Damage1": 10}) |
                                   HasAllCounts({"Damage2": 6, "Damage1": 13}))) |
           (Has("Damage3", 9) & (HasAllCounts({"Damage2": 10, "Damage1": 7}) |
                                  HasAllCounts({"Damage2": 9, "Damage1": 10}) |
                                  HasAllCounts({"Damage2": 8, "Damage1": 13}))) |
           (Has("Damage3", 8) & HasAllCounts({"Damage2": 10, "Damage1": 13})))
damage166 = (Has("Damage5", 2) |
            (Has("Damage5") & (Has("Damage4", 3) |
                              (Has("Damage4", 2) & (Has("Damage3", 3) |
                                                   (Has("Damage3", 2) & (Has("Damage2", 2) |
                                                                        (HasAllCounts({"Damage2": 1, "Damage1": 1})))) |
                                                   (Has("Damage3", 1) & (Has("Damage2", 4) |
                                                                         HasAllCounts({"Damage2": 3, "Damage1": 1}) |
                                                                         HasAllCounts({"Damage2": 2, "Damage1": 4}) |
                                                                         HasAllCounts({"Damage2": 1, "Damage1": 7}) |
                                                                         Has("Damage1", 10))) |
                                                    Has("Damage2", 6) |
                                                    HasAllCounts({"Damage2": 5, "Damage1": 1}) |
                                                    HasAllCounts({"Damage2": 4, "Damage1": 4}) |
                                                    HasAllCounts({"Damage2": 3, "Damage1": 7}) |
                                                    HasAllCounts({"Damage2": 2, "Damage1": 10}) |
                                                    HasAllCounts({"Damage2": 1, "Damage1": 13}))) |
                              (Has("Damage4", 1) & (Has("Damage3", 5) |
                                                    (Has("Damage3", 4) & (Has("Damage2", 6) |
                                                                         HasAllCounts({"Damage2": 5, "Damage1": 2}) |
                                                                         HasAllCounts({"Damage2": 4, "Damage1": 5}) |
                                                                         HasAllCounts({"Damage2": 3, "Damage1": 8}) |
                                                                         HasAllCounts({"Damage2": 2, "Damage1": 11}) |
                                                                         HasAllCounts({"Damage2": 1, "Damage1": 14}))) |
                                                    (Has("Damage3", 3) & (Has("Damage2", 8) |
                                                                         HasAllCounts({"Damage2": 7, "Damage1": 2}) |
                                                                         HasAllCounts({"Damage2": 6, "Damage1": 5}) |
                                                                         HasAllCounts({"Damage2": 5, "Damage1": 8}) |
                                                                         HasAllCounts({"Damage2": 4, "Damage1": 11}) |
                                                                         HasAllCounts({"Damage2": 3, "Damage1": 14}))) |
                                                    (Has("Damage3", 2) & (Has("Damage2", 10) |
                                                                         HasAllCounts({"Damage2": 9, "Damage1": 2}) |
                                                                         HasAllCounts({"Damage2": 8, "Damage1": 5}) |
                                                                         HasAllCounts({"Damage2": 7, "Damage1": 8}) |
                                                                         HasAllCounts({"Damage2": 6, "Damage1": 11}) |
                                                                         HasAllCounts({"Damage2": 5, "Damage1": 14}))) |
                                                    (Has("Damage3", 1) & (HasAllCounts({"Damage2": 10, "Damage1": 5}) |
                                                                         HasAllCounts({"Damage2": 9, "Damage1": 8}) |
                                                                         HasAllCounts({"Damage2": 8, "Damage1": 11}) |
                                                                         HasAllCounts({"Damage2": 7, "Damage1": 14}))) |
                                                    HasAllCounts({"Damage2": 10, "Damage1": 11}) |
                                                    HasAllCounts({"Damage2": 9, "Damage1": 14}))) |
                              (Has("Damage3", 10) & (Has("Damage2", 2) |
                                                     HasAllCounts({"Damage2": 1, "Damage1": 3}) |
                                                     Has("Damage1", 6))) |
                              (Has("Damage3", 9) & (Has("Damage2", 4) |
                                                    HasAllCounts({"Damage2": 3, "Damage1": 3}) |
                                                    HasAllCounts({"Damage2": 2, "Damage1": 6}) |
                                                    HasAllCounts({"Damage2": 1, "Damage1": 9}) |
                                                    Has("Damage1", 12))) |
                              (Has("Damage3", 8) & (Has("Damage2", 6) |
                                                    HasAllCounts({"Damage2": 5, "Damage1": 3}) |
                                                    HasAllCounts({"Damage2": 4, "Damage1": 6}) |
                                                    HasAllCounts({"Damage2": 3, "Damage1": 9}) |
                                                    HasAllCounts({"Damage2": 2, "Damage1": 12}) |
                                                    HasAllCounts({"Damage2": 1, "Damage1": 15}))) |
                              (Has("Damage3", 7) & (Has("Damage2", 8) |
                                                    HasAllCounts({"Damage2": 7, "Damage1": 3}) |
                                                     HasAllCounts({"Damage2": 6, "Damage1": 6}) |
                                                     HasAllCounts({"Damage2": 5, "Damage1": 9}) |
                                                     HasAllCounts({"Damage2": 4, "Damage1": 12}) |
                                                     HasAllCounts({"Damage2": 3, "Damage1": 15}))) |
                              (Has("Damage3", 6) & (Has("Damage2", 10) |
                                                    HasAllCounts({"Damage2": 9, "Damage1": 3}) |
                                                    HasAllCounts({"Damage2": 8, "Damage1": 6}) |
                                                    HasAllCounts({"Damage2": 7, "Damage1": 9}) |
                                                    HasAllCounts({"Damage2": 6, "Damage1": 12}) |
                                                    HasAllCounts({"Damage2": 5, "Damage1": 15}))) |
                              (Has("Damage3", 5) & (HasAllCounts({"Damage2": 10, "Damage1": 6}) |
                                                     HasAllCounts({"Damage2": 9, "Damage1": 9}) |
                                                     HasAllCounts({"Damage2": 8, "Damage1": 12}) |
                                                     HasAllCounts({"Damage2": 7, "Damage1": 15}))) |
                              (Has("Damage3", 4) & (HasAllCounts({"Damage2": 10, "Damage1": 12}) |
                                                    HasAllCounts({"Damage2": 9, "Damage1": 15}))))) |
            (Has("Damage4", 3) & (Has("Damage3", 10) & (HasAllCounts({"Damage2": 10, "Damage1": 1}) |
                                                        HasAllCounts({"Damage2": 9, "Damage1": 4}) |
                                                        HasAllCounts({"Damage2": 8, "Damage1": 7}) |
                                                        HasAllCounts({"Damage2": 7, "Damage1": 10}) |
                                                        HasAllCounts({"Damage2": 6, "Damage1": 13}))) |
                                 (Has("Damage3", 9) & (HasAllCounts({"Damage2": 10, "Damage1": 7}) |
                                                       HasAllCounts({"Damage2": 9, "Damage1": 10}) |
                                                       HasAllCounts({"Damage2": 8, "Damage1": 13}))) |
                                  HasAllCounts({"Damage3": 8, "Damage2": 10, "Damage1": 13})))
damage180 = (Has("Damage5", 2) |
             (Has("Damage5", 1) & (Has("Damage4", 3) & (Has("Damage2", 2) |
                                                        (Has("Damage3")) |
                                                        HasAllCounts({"Damage2": 1, "Damage1": 2}))) |
                                   Has("Damage4", 2) & (Has("Damage3", 5)) |
                                                        (Has("Damage3", 4) & (Has("Damage2", 2) |
                                                                             HasAllCounts({"Damage2": 1, "Damage1": 3}) |
                                                                             Has("Damage1", 6))) |
                                                        (Has("Damage3", 3) & (Has("Damage2", 4) |
                                                                             HasAllCounts({"Damage2": 3, "Damage1": 3}) |
                                                                             HasAllCounts({"Damage2": 2, "Damage1": 6}) |
                                                                             HasAllCounts({"Damage2": 1, "Damage1": 9}) |
                                                                             Has("Damage1", 12))) |
                                                        (Has("Damage3", 2) & (Has("Damage2", 6) |
                                                                             HasAllCounts({"Damage2": 5, "Damage1": 3}) |
                                                                             HasAllCounts({"Damage2": 4, "Damage1": 6}) |
                                                                             HasAllCounts({"Damage2": 3, "Damage1": 9}) |
                                                                             HasAllCounts({"Damage2": 2, "Damage1": 12}) |
                                                                             HasAllCounts({"Damage2": 1, "Damage1": 15}))) |
                                                        (Has("Damage3", 1) & (Has("Damage2", 8) |
                                                                             HasAllCounts({"Damage2": 7, "Damage1": 3}) |
                                                                             HasAllCounts({"Damage2": 6, "Damage1": 6}) |
                                                                             HasAllCounts({"Damage2": 5, "Damage1": 9}) |
                                                                             HasAllCounts({"Damage2": 4, "Damage1": 12}) |
                                                                             HasAllCounts({"Damage2": 3, "Damage1": 15}))) |
                                                         (Has("Damage2", 10)) |
                                                         (HasAllCounts({"Damage2": 9, "Damage1": 3}) |
                                                          HasAllCounts({"Damage2": 8, "Damage1": 6}) |
                                                          HasAllCounts({"Damage2": 7, "Damage1": 9}) |
                                                          HasAllCounts({"Damage2": 6, "Damage1": 12}) |
                                                          HasAllCounts({"Damage2": 5, "Damage1": 15}))) |
             (HasAllCounts({"Damage3": 10, "Damage2": 10, "Damage1": 15})))
damage580 = (Has("Damage5", 5) & (Has("Damage4", 3) & (Has("Damage3") |
                                                       HasAllCounts({"Damage2": 1, "Damage1": 2}) |
                                                       Has("Damage1", 5)) |
                                  Has("Damage4", 2) & (Has("Damage3", 5)) |
                                  (Has("Damage3", 4) & (Has("Damage2", 2) |
                                                        HasAllCounts({"Damage2": 1, "Damage1": 3}) |
                                                        Has("Damage1", 6))) |
                                  (Has("Damage3", 3) & (Has("Damage2", 4) |
                                                        HasAllCounts({"Damage2": 3, "Damage1": 3}) |
                                                        HasAllCounts({"Damage2": 2, "Damage1": 6}) |
                                                        HasAllCounts({"Damage2": 1, "Damage1": 9}) |
                                                        Has("Damage1", 12))) |
                                  (Has("Damage3", 2) & (Has("Damage2", 6) |
                                                        HasAllCounts({"Damage2": 5, "Damage1": 3}) |
                                                        HasAllCounts({"Damage2": 4, "Damage1": 6}) |
                                                        HasAllCounts({"Damage2": 3, "Damage1": 9}) |
                                                        HasAllCounts({"Damage2": 2, "Damage1": 12}) |
                                                        HasAllCounts({"Damage2": 1, "Damage1": 15}))) |
                                  (Has("Damage3", 1) & (Has("Damage2", 8) |
                                                        HasAllCounts({"Damage2": 7, "Damage1": 3}) |
                                                        HasAllCounts({"Damage2": 6, "Damage1": 6}) |
                                                        HasAllCounts({"Damage2": 5, "Damage1": 9}) |
                                                        HasAllCounts({"Damage2": 4, "Damage1": 12}) |
                                                        HasAllCounts({"Damage2": 3, "Damage1": 15}))) |
                                  (Has("Damage2", 10)) |
                                  (HasAllCounts({"Damage2": 9, "Damage1": 3}) |
                                   HasAllCounts({"Damage2": 8, "Damage1": 6}) |
                                   HasAllCounts({"Damage2": 7, "Damage1": 9}) |
                                   HasAllCounts({"Damage2": 6, "Damage1": 12}) |
                                   HasAllCounts({"Damage2": 5, "Damage1": 15}))) |
             (HasAllCounts({"Damage5": 4, "Damage4": 3, "Damage3": 10, "Damage2": 10, "Damage1": 15})))
damage680 = HasAllCounts({"Damage5": 5, "Damage4": 3, "Damage3": 10, "Damage2": 10, "Damage1": 15})

bossdamage50 = HasAny("BossDamage1", "BossDamage2")
bossdamage350 = (Has("BossDamage2", 4) |
                 HasAllCounts({"BossDamage2": 3, "BossDamage1": 1}) |
                 HasAllCounts({"BossDamage2": 2, "BossDamage1": 3}) |
                 HasAllCounts({"BossDamage2": 1, "BossDamage1": 5}) |
                 Has("BossDamage1", 7))
bossdamage400 = (Has("BossDamage2", 4) |
                 HasAllCounts({"BossDamage2": 3, "BossDamage1": 2}) |
                 HasAllCounts({"BossDamage2": 2, "BossDamage1": 4}) |
                 HasAllCounts({"BossDamage2": 1, "BossDamage1": 6}) |
                 Has("BossDamage1", 8))
bossdamage500 = (Has("BossDamage2", 5) |
                 HasAllCounts({"BossDamage2": 4, "BossDamage1": 2}) |
                 HasAllCounts({"BossDamage2": 3, "BossDamage1": 4}) |
                 HasAllCounts({"BossDamage2": 2, "BossDamage1": 6}) |
                 HasAllCounts({"BossDamage2": 1, "BossDamage1": 8}) |
                 Has("BossDamage1", 10))
bossdamage700 = (Has("BossDamage2", 7) |
                 HasAllCounts({"BossDamage2": 6, "BossDamage1": 2}) |
                 HasAllCounts({"BossDamage2": 5, "BossDamage1": 4}) |
                 HasAllCounts({"BossDamage2": 4, "BossDamage1": 6}) |
                 HasAllCounts({"BossDamage2": 3, "BossDamage1": 8}) |
                 HasAllCounts({"BossDamage2": 2, "BossDamage1": 10}) )
bossdamage900 = (Has("BossDamage2", 9) |
                 HasAllCounts({"BossDamage2": 8, "BossDamage1": 2}) |
                 HasAllCounts({"BossDamage2": 7, "BossDamage1": 4}) |
                 HasAllCounts({"BossDamage2": 6, "BossDamage1": 6}) |
                 HasAllCounts({"BossDamage2": 5, "BossDamage1": 8}) |
                 HasAllCounts({"BossDamage2": 4, "BossDamage1": 10}) )
bossdamage1000 = (Has("BossDamage2", 10) |
                 HasAllCounts({"BossDamage2": 9, "BossDamage1": 2}) |
                 HasAllCounts({"BossDamage2": 8, "BossDamage1": 4}) |
                 HasAllCounts({"BossDamage2": 7, "BossDamage1": 6}) |
                 HasAllCounts({"BossDamage2": 6, "BossDamage1": 8}) |
                 HasAllCounts({"BossDamage2": 5, "BossDamage1": 10}) )
bossdamage1500 = HasAllCounts({"BossDamage2": 10, "BossDamage1": 10})


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

lifesteal1 = HasAny("Salvaging1", "Lifesteal1", "Salvaging2", "Lifesteal2", "Lifesteal3")
lifesteal2 = HasAny("Lifesteal1", "Salvaging2", "Lifesteal2", "Lifesteal3") | Has("Salvaging1", 2)
lifesteal5 = HasAny("Lifesteal1, Salvaging2" "Lifesteal2", "Lifesteal3") | Has("Salvaging1", 5)
lifesteal51 = HasAny("Lifesteal2", "Lifesteal3") | (Has("Lifesteal1") & HasAny("Salvaging1", "Salvaging2"))
lifesteal205 = HasAny("Lifesteal2", "Lifesteal3") | Has("Lifesteal1", 5) | (Has("Lifesteal1", 4) & (Has("Salvaging2") | Has("Salvaging1", 5)))
lifesteal263 = HasAny("Lifesteal2", "Lifesteal3") | HasAllCounts({"Lifesteal1": 5, "Salvaging2": 1, "Salvaging1": 5})
lifesteal8263 = Has("Lifesteal3", 2) | HasAllCounts({"Lifesteal3": 1, "Lifesteal2": 3, "Lifesteal1": 5, "Salvaging2": 1, "Salvaging1": 5})
lifesteal13263 = HasAllCounts({"Lifesteal3": 2, "Lifesteal2": 3, "Lifesteal1": 5, "Salvaging2": 1, "Salvaging1": 5})

bossarmor1 = HasAny("BossArmor1", "BossArmor2")
bossarmor2 = Has("BossArmor2") | Has("BossArmor1", 2)
bossarmor10 = Has("BossArmor2") | Has("BossArmor1", 10)
bossarmor160 = Has("BossArmor2", 7) | HasAllCounts({"BossArmor2": 6, "BossArmor1": 10})
bossarmor210 = HasAllCounts({"BossArmor2": 8, "BossArmor1": 10})

regen1 = HasFromList(*regen, count=1)
regen5 = HasFromList(*regen, count=5)
regen6 = HasFromList(*regen, count=6)
regen7 = HasFromList(*regen, count=7)
regen14 = HasFromList(*regen, count=14)
regen17 = HasFromList(*regen, count=17)
regen25 = HasFromList(*regen, count=25)

critdamage50 = HasAny("CritDamage1", "CritDamage2")
critdamage200 = Has("CritDamage2") | Has("CritDamage1", 4)
critdamage500 = Has("CritDamage2", 3) | HasAllCounts({"CritDamage2": 2, "CritDamage1": 2}) | HasAllCounts({"CritDamage2": 1, "CritDamage1": 6}) | Has("CritDamage1", 10)
critdamage2100 = HasAllCounts({"CritDamage2": 8, "CritDamage1": 6}) | HasAllCounts({"CritDamage2": 7, "CritDamage1": 10})

infinity1 = HasAny("Infinity1", "Infinity2", "Infinity3", "Infinity4", "Infinity5", "Infinity6", "Infinity7", "Infinity8", "Infinity9")

spawnrate1 = HasAny("SpawnRate1", "SpawnRate2", "SpawnRate3", "SpawnRate4")
spawnrate950 = (Has("SpawnRate4", 3) |
                (Has("SpawnRate4", 2) & (Has("SpawnRate2") |
                                        Has("SpawnRate3", 2) |
                                        HasAllCounts({"SpawnRate3": 1, "SpawnRate1": 2}) |
                                        Has("SpawnRate1", 3))) |
                (Has("SpawnRate4", 1) & (Has("SpawnRate3", 5) & HasAny("SpawnRate1", "SpawnRate2") |
                                        Has("SpawnRate3", 4) & (Has("SpawnRate2") |
                                                                Has("SpawnRate1", 3)) |
                                        Has("SpawnRate3", 3) & (HasAllCounts({"SpawnRate2": 1, "SpawnRate1": 1}) |
                                                                Has("SpawnRate1", 5)) |
                                        Has("SpawnRate3", 2) & (HasAllCounts({"SpawnRate2": 1, "SpawnRate1": 3}) |
                                                                Has("SpawnRate1", 7)) |
                                        Has("SpawnRate3", 1) & (HasAllCounts({"SpawnRate2": 1, "SpawnRate1": 5}) |
                                                                Has("SpawnRate1", 9)) |
                                        HasAllCounts({"SpawnRate2": 1, "SpawnRate1": 7}) |
                                        Has("SpawnRate1", 11))) |
                (Has("SpawnRate3", 5) & (HasAllCounts({"SpawnRate2": 1, "SpawnRate1": 5}) |
                                        Has("SpawnRate1", 9))) |
                (Has("SpawnRate3", 4) & (HasAllCounts({"SpawnRate2": 1, "SpawnRate1": 7}) |
                                        Has("SpawnRate1", 11))) |
                (Has("SpawnRate3", 3) & (HasAllCounts({"SpawnRate2": 1, "SpawnRate1": 9}) |
                                        Has("SpawnRate1", 13))) |
                (Has("SpawnRate3", 2) & (HasAllCounts({"SpawnRate2": 1, "SpawnRate1": 11}) |
                                        Has("SpawnRate1", 15))) |
                HasAllCounts({"SpawnRate2": 1, "SpawnRate1": 15}))
spawnrate1050 = (Has("SpawnRate4", 3) |
                (Has("SpawnRate4", 2) & (Has("SpawnRate3", 3)) |
                                        (Has("SpawnRate3", 2) & HasAny("SpawnRate2", "SpawnRate1")) |
                                        (Has("SpawnRate3", 1) & (Has("SpawnRate2") |
                                                                (Has("SpawnRate1", 3)) |
                                                                 HasAll("SpawnRate2", "SpawnRate1"))) |
                                        (HasAll("SpawnRate2", "SpawnRate1") |
                                        (Has("SpawnRate1", 3)))) |
                (Has("SpawnRate4", 1) & (Has("SpawnRate3", 5) & (Has("SpawnRate2") |
                                                                 Has("SpawnRate1", 3))) |
                                        (Has("SpawnRate3", 4) & (HasAll ("SpawnRate2", "SpawnRate1") |
                                                                (Has("SpawnRate1", 5)))) |
                                        (Has("SpawnRate3", 3) & (HasAllCounts({"SpawnRate2": 1, "SpawnRate1": 3}) |
                                                                (Has("SpawnRate1", 7)))) |
                                        (Has("SpawnRate3", 2) & (HasAllCounts({"SpawnRate2": 1, "SpawnRate1": 5}) |
                                                                (Has("SpawnRate1", 9)))) |
                                        (Has("SpawnRate3", 1) & (HasAllCounts({"SpawnRate2":1, "SpawnRate1": 7}) |
                                                                (Has("SpawnRate1", 11)))) |
                                        (HasAllCounts({"SpawnRate2": 1, "SpawnRate1": 9})) |
                                        (Has("SpawnRate1", 13))) |
                (Has("SpawnRate3", 5) & (HasAllCounts({"SpawnRate2": 1, "SpawnRate1": 7}) |
                                        (Has("SpawnRate1", 11)))) |
                (Has("SpawnRate3", 4) & (HasAllCounts({"SpawnRate2": 1, "SpawnRate1": 9}) |
                                        (Has("SpawnRate1", 13)))) |
                (Has("SpawnRate3", 3) & (HasAllCounts({"SpawnRate2": 1, "SpawnRate1": 11}) |
                                        (Has("SpawnRate1", 15)))) |
                (Has("SpawnRate3", 2) & (HasAllCounts({"SpawnRate2": 1, "SpawnRate1": 13}))) |
                 HasAllCounts({"SpawnRate3": 1, "SpawnRate2": 1, "SpawnRate1": 15}))


spawnrate1450 = (Has("SpawnRate4", 4) |
                 (Has("SpawnRate4", 3) & (Has("SpawnRate3", 3) |
                                         (Has("SpawnRate3", 2) & HasAny("SpawnRate2", "SpawnRate1")) |
                                         (Has("SpawnRate3", 1) & (Has("SpawnRate2") |
                                                                 Has("SpawnRate1", 3))) |
                                         (HasAll("SpawnRate2", "SpawnRate1")))) |
                 (Has("SpawnRate4", 2) & (Has("SpawnRate3", 5) & (Has("SpawnRate2") |
                                                                 Has("SpawnRate1", 3)) |
                                         (Has("SpawnRate3", 4) & (HasAllCounts({"SpawnRate2": 1, "SpawnRate1": 1}) |
                                                                 Has("SpawnRate1", 5))) |
                                         (Has("SpawnRate3", 3) & (HasAllCounts({"SpawnRate2": 1, "SpawnRate1": 3}) |
                                                                 Has("SpawnRate1", 7))) |
                                         (Has("SpawnRate3", 2) & (HasAllCounts({"SpawnRate2": 1, "SpawnRate1": 5}) |
                                                                 Has("SpawnRate1", 9))) |
                                         (Has("SpawnRate3", 1) & (HasAllCounts({"SpawnRate2": 1, "SpawnRate1": 7}) |
                                                                 Has("SpawnRate1", 11))) |
                                         HasAllCounts({"SpawnRate2": 1, "SpawnRate1": 9}) |
                                         Has("SpawnRate1", 13))) |
                 (Has("SpawnRate4", 1) & (Has("SpawnRate3", 5) & (HasAllCounts({"SpawnRate2": 1, "SpawnRate1": 7}) |
                                                                 Has("SpawnRate1", 11))) |
                                        (Has("SpawnRate3", 4) & (HasAllCounts({"SpawnRate2": 1, "SpawnRate1": 9}) |
                                                                 Has("SpawnRate1", 13))) |
                                        (Has("SpawnRate3", 3) & (HasAllCounts({"SpawnRate2": 1, "SpawnRate1": 11}) |
                                                                 Has("SpawnRate1", 15)))) |
                 HasAllCounts({"SpawnRate3": 5, "SpawnRate2": 1, "SpawnRate1": 15}))
spawnrate3450 = HasAllCounts({"SpawnRate4": 5, "SpawnRate3": 5, "SpawnRate2": 1, "SpawnRate1": 15})

bluespawn5 = Has("NodeFinder1", 5)

health1 = HasAny("Health1", "Health2", "Health3", "Health4", "Health5", "Health6", "Health7")
health40 = (HasAny("Health3", "Health4", "Health5", "Health6", "Health7") |
            Has("Health2", 4) |
            HasAllCounts({"Health2": 3, "Health1": 1}) |
            HasAllCounts({"Health2": 2, "Health1": 4}) |
            HasAllCounts({"Health2": 1, "Health1": 7}) |
            Has("Health1", 10))
health88 = (HasAny("Health4", "Health5", "Health6", "Health7") |
            Has("Health3", 2) |
            Has("Health3", 1) & (Has("Health2") | Has("Health1", 2)) |
            Has("Health2", 8) |
            HasAllCounts({"Health2": 7, "Health1": 1}) |
            HasAllCounts({"Health2": 6, "Health1": 4}) |
            HasAllCounts({"Health2": 5, "Health1": 7}) |
            HasAllCounts({"Health2": 4, "Health1": 10}))
health376 = (HasAny("Health5", "Health6", "Health7") |
             Has("Health4", 2) |
             (Has("Health4", 1) & (Has("Health3") |
                                   Has("Health2", 7) |
                                   HasAllCounts({"Health2": 6, "Health1": 1}) |
                                   HasAllCounts({"Health2": 5, "Health1": 4}) |
                                   HasAllCounts({"Health2": 4, "Health1": 7}) |
                                   HasAllCounts({"Health2": 3, "Health1": 10}))) |
             Has("Health3", 5) |
              (Has("Health3", 4) & (Has("Health2", 5) |
                                    HasAllCounts({"Health2": 4, "Health1": 2}) |
                                    HasAllCounts({"Health2": 3, "Health1": 5}) |
                                    HasAllCounts({"Health2": 2, "Health1": 8}))) |
              HasAllCounts({"Health3": 3, "Health2": 8, "Health1": 10}))
health696 = (HasAny("Health5", "Health6", "Health7") |
             Has("Health4", 3) |
             (Has("Health4", 2) & (Has("Health3", 2) |
                                   Has("Health3", 1) & (Has("Health2", 2) |
                                                        HasAllCounts({"Health2": 1, "Health1": 1}) |
                                                        Has("Health1", 4)) |
                                   Has("Health2", 8) |
                                   HasAllCounts({"Health2": 7, "Health1": 3}) |
                                   HasAllCounts({"Health2": 6, "Health1": 6}) |
                                   HasAllCounts({"Health2": 5, "Health1": 9}))) |
             (Has("Health4", 1) & (Has("Health3", 5) |
                                   (Has("Health3", 4) & (Has("Health2", 7) |
                                                         HasAllCounts({"Health2": 6, "Health1": 1}) |
                                                         HasAllCounts({"Health2": 5, "Health1": 4}) |
                                                         HasAllCounts({"Health2": 4, "Health1": 7}) |
                                                         HasAllCounts({"Health2": 3, "Health1": 10}))))))
health1016 = (HasAny("Health5", "Health6", "Health7") |
              Has("Health4", 4) |
              (Has("Health4", 3) & (Has("Health3", 2) |
                                    Has("Health3", 1) & (Has("Health2", 3) |
                                                         HasAllCounts({"Health2": 2, "Health1": 3}) |
                                                         HasAllCounts({"Health2": 1, "Health1": 6}) |
                                                         Has("Health1", 9)) |
                                    HasAllCounts({"Health2": 10, "Health1": 5}) |
                                    HasAllCounts({"Health2": 9, "Health1": 8}))))
health2216 = (HasAny("Health5", "Health6", "Health7") |
              Has("Health4", 7) |
              (Has("Health4", 6) & (Has("Health3", 6) |
                                    (Has("Health3", 5) & (Has("Health2", 2) |
                                                          HasAllCounts({"Health2": 1, "Health1": 1}) |
                                                          Has("Health1", 4))) |
                                    (Has("Health3", 4) & (Has("Health2", 8) |
                                                          HasAllCounts({"Health2": 7, "Health1": 3}) |
                                                          HasAllCounts({"Health2": 6, "Health1": 6}) |
                                                          HasAllCounts({"Health2": 5, "Health1": 9}))))) |
              (Has("Health4", 5) & (Has("Health3", 9) |
                                    Has("Health3", 8) & (Has("Health2", 7) |
                                                         HasAllCounts({"Health2": 6, "Health1": 1}) |
                                                         HasAllCounts({"Health2": 5, "Health1": 4}) |
                                                         HasAllCounts({"Health2": 4, "Health1": 7}) |
                                                         HasAllCounts({"Health2": 3, "Health1": 10})))))
health4016 = (HasAny("Health6", "Health7") |
              Has("Health5", 2) |
              (Has("Health5", 1) & (HasAny("Health4", "Health3") |
                                    Has("Health2", 2) |
                                    HasAllCounts({"Health2": 1, "Health1": 1}) |
                                    Has("Health1", 4))))
health265936 = (Has("Health7", 3) |
                (Has("Health7", 2) & (Has("Health6", 2) |
                                     Has("Health6", 1) & (Has("Health5", 4) |
                                                          HasAllCounts({"Health5": 3, "Health4": 10, "Health3": 10, "Health2": 8, "Health1": 10})))) |
                (Has("Health7", 1) & (Has("Health6", 4) |
                                      Has("Health6", 3) & (Has("Health5", 4) |
                                                           HasAllCounts({"Health5": 3, "Health4": 10, "Health3": 10, "Health2": 8, "Health1": 10})))) |
                (Has("Health6", 5) & (Has("Health5", 4) |
                                                           HasAllCounts({"Health5": 3, "Health4": 10, "Health3": 10, "Health2": 8, "Health1": 10}))))
health365936 = (Has("Health7", 4) |
                Has("Health7", 3) & (Has("Health6", 2) |
                                     (HasAllCounts({"Health6": 1, "Health5": 3, "Health4": 10, "Health3": 10, "Health2": 8, "Health1": 10}))))
health765936 = HasAllCounts({"Health7": 5, "Health6": 5, "Health5": 3, "Health4": 10, "Health3": 10, "Health2": 8, "Health1": 10})

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
        "AttackSpeed1-1": Has("Boss Drops", 1) | (boss_mode_off & can_beat_boss0),
        "AttackSpeed2-1": Has("Boss Drops", 2) | (boss_mode_off & has_access_to_blue_enemies & can_beat_boss2),
        "SpawnRate2-1": Has("Boss Drops", 3) | (boss_mode_off & can_beat_boss3),
        "DropHeal1-1": Has("Boss Drops", 4) | (boss_mode_off & can_beat_boss4),
        "Size2-1": Has("Boss Drops", 5) | (boss_mode_off & has_access_to_blue_enemies & can_beat_boss5),
        "Size3-1": Has("Boss Drops", 6) | (boss_mode_off & has_access_to_blue_enemies & can_beat_boss13),
        "MovingPulserSize2-1": Has("Boss Drops", 7) | (boss_mode_off & has_access_to_blue_enemies & can_beat_boss13),
        "PulseBoltCount2-1": Has("Boss Drops", 8) | (boss_mode_off),
        "Infinity1-1": Has("Boss Drops", 9) | boss_mode_off,
        "Infinity2-1": Has("Boss Drops", 10) | boss_mode_off,
        "Infinity3-1": Has("Boss Drops", 11) | boss_mode_off,
        "Infinity4-1": Has("Boss Drops", 12) | boss_mode_off,
        "Infinity5-1": Has("Boss Drops", 13) | boss_mode_off,
        "Infinity6-1": Has("Boss Drops", 14) | (boss_mode_off & can_beat_boss11),
        "Infinity7-1": Has("Boss Drops", 15) | (boss_mode_off & can_beat_boss12),
        "Infinity8-1": Has("Boss Drops", 16) | (boss_mode_off & can_beat_boss13),
        "Infinity9-1": Has("Boss Drops", 17) | boss_mode_off,
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
        world.set_rule(world.get_region("Crowding"), ProgItemRule("Progressive Damage", 1) | damage1)
        world.set_rule(world.get_region("Firewall"), ProgItemRule("Progressive Health", 1) | health1)
        world.set_rule(world.get_region("Repair Tool"), ProgItemRule("Progressive Health", 1) | health1)
        world.set_rule(world.get_region("Potency"), (ProgItemRule("Progressive Damage", 31) | damage31) & has_access_to_blue_enemies)
        world.set_rule(world.get_region("Nodeblade"), (ProgItemRule("Progressive Damage", 91) | damage91) & has_access_to_blue_enemies)
        world.set_rule(world.get_region("First Strike"), (ProgItemRule("Progressive Damage", 37) | damage37))
        world.set_rule(world.get_region("Crit Chance"), (ProgItemRule("Progressive Damage", 37) | damage37))
        world.set_rule(world.get_region("Crit Damage"), Has("CritChance1"))
        world.set_rule(world.get_region("Big Crit"), (ProgItemRule("Progressive Critical Damage", 50) | critdamage50) & has_crypto_mine)
        world.set_rule(world.get_region("Netblade"), (ProgItemRule("Progressive Damage", 166) | damage166) & has_crypto_mine)
        world.set_rule(world.get_region("Giant Slayer"), (ProgItemRule("Progressive Additional Damage", 1) | addidamage1))
        world.set_rule(world.get_region("Repeating"), (ProgItemRule("Progressive Additional Damage", 1) | addidamage1))
        world.set_rule(world.get_region("Finishing Blow"), (ProgItemRule("Progressive Additional Damage", 17) | addidamage17))
        world.set_rule(world.get_region("Beyond"), (ProgItemRule("Progressive Health", 265936) | health265936))
        world.set_rule(world.get_region("Sapper"), (ProgItemRule("Progressive Lifesteal", 1) | lifesteal1) & has_access_to_blue_enemies)
        world.set_rule(world.get_region("Skilled Salvager"), (ProgItemRule("Progressive Lifesteal", 5) | lifesteal5) & has_access_to_blue_enemies)
        world.set_rule(world.get_region("Patcher"), (ProgItemRule("Progressive Lifesteal", 51) | lifesteal51))
        world.set_rule(world.get_region("Better Endurance"), (ProgItemRule("Progressive Lifesteal", 1) | lifesteal1) | (ProgItemRule("Progressive Boss Armor", 1) | bossarmor1))
        world.set_rule(world.get_region("Drainer"), (ProgItemRule("Progressive Regen", 17) | regen17) & has_crypto_mine)
        world.set_rule(world.get_region("Bit Boost"), (ProgItemRule("Progressive SpawnRate", 1) | spawnrate1))
        world.set_rule(world.get_region("Last Strike"), (ProgItemRule("Progressive Additional Damage", 6) | addidamage6))
        world.set_rule(world.get_region("Influence"), (ProgItemRule("Progressive SpawnRate", 1) | spawnrate1))
        world.set_rule(world.get_region("Swarming"), (ProgItemRule("Progressive SpawnRate", 1) | spawnrate1))
        world.set_rule(world.get_region("Infesting"), (ProgItemRule("Progressive SpawnRate", 950) | spawnrate950))
        world.set_rule(world.get_region("Overloaded"), (ProgItemRule("Progressive SpawnRate", 1450) | spawnrate1450) & has_crypto_mine)
        world.set_rule(world.get_region("Antivirus"), (ProgItemRule("Progressive Armor", 10) | armor10))
        world.set_rule(world.get_region("Swarm Defense System"), (ProgItemRule("Progressive Armor", 11) | armor11))
        world.set_rule(world.get_region("Bolster"), (ProgItemRule("Progressive Armor", 15) | armor15))
        world.set_rule(world.get_region("Super Armor"), (ProgItemRule("Progressive Armor", 35) | armor35))
        world.set_rule(world.get_region("Anti-Purple"), (ProgItemRule("Progressive Armor", 36) | armor36) & has_access_to_blue_enemies)
        world.set_rule(world.get_region("Bit Armor"), (ProgItemRule("Progressive Armor", 45) | armor45))
        world.set_rule(world.get_region("Byte Armor"), (ProgItemRule("Progressive Armor", 65) | armor65))
        world.set_rule(world.get_region("Blood Armor"), (ProgItemRule("Progressive Armor", 95) | armor95) & has_access_to_blue_enemies)
        world.set_rule(world.get_region("Net Armor"), (ProgItemRule("Progressive Armor", 95) | armor95) & has_crypto_mine)
        world.set_rule(world.get_region("Focus Armor"), (ProgItemRule("Progressive Armor", 95) | armor95))
        world.set_rule(world.get_region("Blood Visage"), (ProgItemRule("Progressive Armor", 110) | armor110) & has_crypto_mine)
        world.set_rule(world.get_region("Domain Expansion"), (ProgItemRule("Progressive SpawnRate", 1050) | spawnrate1050))
        world.set_rule(world.get_region("Processor Acquisition"), has_crypto_mine)
        world.set_rule(world.get_region("Endurance"), (ProgItemRule("Progressive Damage", 1) | damage1))
        world.set_rule(world.get_region("Connection Buster"), (ProgItemRule("Progressive Damage", 1) | damage1))
        world.set_rule(world.get_region("Pulse Bolts"), has_access_to_blue_enemies)
        world.set_rule(world.get_region("Scaling Regeneration"), has_access_to_blue_enemies)
        world.set_rule(world.get_region("Auto-Collect"), has_access_to_blue_enemies)
        world.set_rule(world.get_region("Crypto Mine"), has_access_to_blue_enemies)
        world.set_rule(world.get_region("Milestones"), has_access_to_blue_enemies)
        world.set_rule(world.get_region("Spawn Exploders"), has_access_to_blue_enemies)
        world.set_rule(world.get_region("Unending Parasite"), has_access_to_blue_enemies)
        world.set_rule(world.get_region("Bolt Burst"), has_access_to_blue_enemies & Has("PulseBoltDamage1"))
        world.set_rule(world.get_region("Pulser Pursuit"), has_access_to_blue_enemies)
        world.set_rule(world.get_region("Pulse Thumper"), has_access_to_blue_enemies)
        world.set_rule(world.get_region("Parasite Evolution"), has_access_to_blue_enemies)
        world.set_rule(world.get_region("Indomitable"), has_access_to_blue_enemies)
        world.set_rule(world.get_region("Thundering"), has_access_to_blue_enemies)
        world.set_rule(world.get_region("Infinity"), has_access_to_blue_enemies)
        world.set_rule(world.get_region("Bolt Damage"), Has("PulseBolts"))
        world.set_rule(world.get_region("Bolt Count"), Has("PulseBolts"))
        world.set_rule(world.get_region("Bolt Barrage"), Has("PulseBoltCount2"))
        world.set_rule(world.get_region("Bolt Lethality"), HasAny("PulseBoltExplode", "PulseBoltCount2") & has_crypto_mine)
        world.set_rule(world.get_region("Epilogue"), can_release_virus)
        # Node off of Netcoin
        #"Thundering": lambda state: has_access_to_net_and_nodes(world, state, player),
        #"Pulser Pursuit": lambda state: has_access_to_net_and_nodes(world, state, player),
        #"Pulse Thumper": lambda state: has_access_to_net_and_nodes(world, state, player),
        #"Unending Parasite": lambda state: has_access_to_net_and_nodes(world, state, player),
        # Netcoin
        world.set_rule(world.get_region("Auto Pulser"), has_crypto_mine)
        world.set_rule(world.get_region("Transplant"), has_crypto_mine)
        world.set_rule(world.get_region("Crypto Levels"), has_crypto_mine)
        # Milestones
        world.set_rule(world.get_region("Milestone Page"), has_milestones_upgrade)
        world.set_rule(world.get_region("Red Milestones"), can_start_red_milestones)
        world.set_rule(world.get_region("Blue Milestones"), can_start_blue_milestones)
        world.set_rule(world.get_region("Yellow Milestones"), can_start_yellow_milestones)


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
            r.connect(c)
    set_region_rules(world, player)


def set_nodebuster_rules(world: NodebusterWorld) -> None:
    player = world.player

    location_rules_lookup = get_location_rules_lookup(world, player)
    for location_name, rule in location_rules_lookup.items():
        world.set_rule(world.get_location(location_name), rule)

    # Goal
    world.set_completion_rule(released_virus)