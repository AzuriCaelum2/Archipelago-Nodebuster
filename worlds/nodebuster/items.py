from typing import TypedDict

from BaseClasses import Item, ItemClassification

base_id = 268000


class NodebusterItem(Item):
    name: str = "Nodebuster"


class ItemDict(TypedDict):
    name: str
    count: int
    classification: ItemClassification


upgrade_items: list[ItemDict] = [
    {"name": "Damage1", "count": 15, 'classification': ItemClassification.progression},
    {"name": "Health1", "count": 10, 'classification': ItemClassification.progression},
    {"name": "SpawnRate1", "count": 15, 'classification': ItemClassification.progression},
    {"name": "Armor1", "count": 10, 'classification': ItemClassification.progression},
    {"name": "BitBoost1", "count": 1, 'classification': ItemClassification.useful},
    {"name": "Size1", "count": 10, 'classification': ItemClassification.useful},
    {"name": "BossArmor1", "count": 10, 'classification': ItemClassification.progression},
    {"name": "HealthRegen1", "count": 5, 'classification': ItemClassification.progression},
    {"name": "NodeFinder1", "count": 5, 'classification': ItemClassification.progression},
    {"name": "Salvaging1", "count": 5, 'classification': ItemClassification.progression},
    {"name": "DamagePerEnemy1", "count": 5, 'classification': ItemClassification.progression},
    {"name": "BossDamage1", "count": 10, 'classification': ItemClassification.progression},
    {"name": "AttackSpeed1", "count": 1, 'classification': ItemClassification.useful},
    {"name": "BonusDropChance1", "count": 5, 'classification': ItemClassification.useful},
    {"name": "ExplodersChance", "count": 1, 'classification': ItemClassification.useful},
    {"name": "Health2", "count": 8, 'classification': ItemClassification.progression},
    {"name": "Armor2", "count": 5, 'classification': ItemClassification.progression},
    {"name": "Lifesteal1", "count": 5, 'classification': ItemClassification.progression},
    {"name": "Damage2", "count": 10, 'classification': ItemClassification.progression},
    {"name": "PickupRadius1", "count": 5, 'classification': ItemClassification.useful},
    {"name": "HealthRegen2", "count": 1, 'classification': ItemClassification.progression},
    {"name": "Milestones", "count": 1, 'classification': ItemClassification.progression},
    {"name": "Salvaging2", "count": 1, 'classification': ItemClassification.progression},
    {"name": "AttackSpeed2", "count": 1, 'classification': ItemClassification.useful},
    {"name": "SpawnRate2", "count": 1, 'classification': ItemClassification.progression},
    {"name": "NodeBoost1", "count": 1, 'classification': ItemClassification.useful},
    {"name": "ArmorPerEnemy1", "count": 10, 'classification': ItemClassification.progression},
    {"name": "Armor3", "count": 10, 'classification': ItemClassification.progression},
    {"name": "DropHeal1", "count": 1, 'classification': ItemClassification.progression},
    {"name": "Health3", "count": 10, 'classification': ItemClassification.progression},
    {"name": "PulseBolts", "count": 1, 'classification': ItemClassification.progression},
    {"name": "PulseBoltDamage1", "count": 10, 'classification': ItemClassification.progression},
    {"name": "PulseBoltCount1", "count": 5, 'classification': ItemClassification.progression},
    {"name": "ExplodersSize", "count": 5, 'classification': ItemClassification.useful},
    {"name": "MaxHealthHeal1", "count": 10, 'classification': ItemClassification.progression},
    {"name": "Armor4", "count": 10, 'classification': ItemClassification.progression},
    {"name": "BossArmor2", "count": 8, 'classification': ItemClassification.progression},
    {"name": "Damage3", "count": 10, 'classification': ItemClassification.progression},
    {"name": "Undamaged1", "count": 6, 'classification': ItemClassification.progression},
    {"name": "Execute1", "count": 6, 'classification': ItemClassification.progression},
    {"name": "CritChance1", "count": 10, 'classification': ItemClassification.progression},
    {"name": "SpawnRate3", "count": 5, 'classification': ItemClassification.progression},
    {"name": "Armor5", "count": 20, 'classification': ItemClassification.progression},
    {"name": "Damage4", "count": 3, 'classification': ItemClassification.progression},
    {"name": "Size2", "count": 1, 'classification': ItemClassification.useful},
    {"name": "CryptoMine", "count": 1, 'classification': ItemClassification.progression},
    {"name": "Health4", "count": 10, 'classification': ItemClassification.progression},
    {"name": "YellowSpawn1", "count": 1, 'classification': ItemClassification.progression},
    {"name": "Armor6", "count": 30, 'classification': ItemClassification.progression},
    {"name": "BossDamage2", "count": 10, 'classification': ItemClassification.progression},
    {"name": "Lifesteal2", "count": 3, 'classification': ItemClassification.progression},
    {"name": "MovingPulser1", "count": 5, 'classification': ItemClassification.useful},
    {"name": "Size3", "count": 3, 'classification': ItemClassification.useful},
    {"name": "MovingPulserSize1", "count": 6, 'classification': ItemClassification.useful},
    {"name": "MovingPulserAttackSpeed1", "count": 5, 'classification': ItemClassification.useful},
    {"name": "Health5", "count": 3, 'classification': ItemClassification.progression},
    {"name": "Lifesteal3", "count": 2, 'classification': ItemClassification.progression},
    {"name": "MaxHealthToArmor1", "count": 5, 'classification': ItemClassification.progression},
    {"name": "CritDamage1", "count": 10, 'classification': ItemClassification.progression},
    {"name": "Damage5", "count": 5, 'classification': ItemClassification.progression},
    {"name": "Armor7", "count": 5, 'classification': ItemClassification.progression},
    {"name": "FocusArmor1", "count": 5, 'classification': ItemClassification.progression},
    {"name": "StealMaxHealth1", "count": 1, 'classification': ItemClassification.progression},
    {"name": "PulseBoltExplode", "count": 1, 'classification': ItemClassification.progression},
    {"name": "MovingPulserSize2", "count": 1, 'classification': ItemClassification.useful},
    {"name": "PulseBoltCount2", "count": 1, 'classification': ItemClassification.progression},
    {"name": "PulseBoltDamage2", "count": 3, 'classification': ItemClassification.useful},
    {"name": "MovingPulserSpeed1", "count": 5, 'classification': ItemClassification.useful},
    {"name": "Undamaged2", "count": 4, 'classification': ItemClassification.progression},
    {"name": "Execute2", "count": 4, 'classification': ItemClassification.progression},
    {"name": "MaxHealthHeal2", "count": 5, 'classification': ItemClassification.progression},
    {"name": "RampingDamage1", "count": 3, 'classification': ItemClassification.progression},
    {"name": "EnemyDeathPulseBolts", "count": 6, 'classification': ItemClassification.useful},
    {"name": "SpawnRate4", "count": 5, 'classification': ItemClassification.progression},
    {"name": "StealMaxHealth2", "count": 1, 'classification': ItemClassification.progression},
    {"name": "MaxHealthToArmor2", "count": 1, 'classification': ItemClassification.progression},
    {"name": "RampingArmor1", "count": 5, 'classification': ItemClassification.progression},
    {"name": "Health6", "count": 5, 'classification': ItemClassification.progression},
    {"name": "StealMaxHealth3", "count": 1, 'classification': ItemClassification.progression},
    {"name": "LightningChance1", "count": 5, 'classification': ItemClassification.useful},
    {"name": "LightningChainCount1", "count": 8, 'classification': ItemClassification.useful},
    {"name": "LightningDamage1", "count": 8, 'classification': ItemClassification.useful},
    {"name": "CritDamage2", "count": 8, 'classification': ItemClassification.progression},
    {"name": "MaxHealthToDamage1", "count": 1, 'classification': ItemClassification.progression},
    {"name": "Health7", "count": 5, 'classification': ItemClassification.progression},
    {"name": "Infinity1", "count": 1, 'classification': ItemClassification.progression},
    {"name": "Infinity2", "count": 1, 'classification': ItemClassification.progression},
    {"name": "Infinity3", "count": 1, 'classification': ItemClassification.progression},
    {"name": "Infinity4", "count": 1, 'classification': ItemClassification.progression},
    {"name": "Infinity5", "count": 1, 'classification': ItemClassification.progression},
    {"name": "Infinity6", "count": 1, 'classification': ItemClassification.progression},
    {"name": "Infinity7", "count": 1, 'classification': ItemClassification.progression},
    {"name": "Infinity8", "count": 1, 'classification': ItemClassification.progression},
    {"name": "Infinity9", "count": 1, 'classification': ItemClassification.progression},
    {"name": "Laboratory", "count": 1, 'classification': ItemClassification.progression},
    {"name": "YellowSpawn2", "count": 1, 'classification': ItemClassification.progression},
    {"name": "AutoCollect", "count": 8, 'classification': ItemClassification.useful}
]

milestone_items: list[ItemDict] = [
    {"name": "Reds500", "count": 1, "classification": ItemClassification.filler},
    {"name": "Blues10", "count": 1, "classification": ItemClassification.filler},
    {"name": "Reds2k", "count": 1, "classification": ItemClassification.filler},
    {"name": "Blues100", "count": 1, "classification": ItemClassification.filler},
    {"name": "Reds4k", "count": 1, "classification": ItemClassification.filler},
    {"name": "Blues200", "count": 1, "classification": ItemClassification.filler},
    {"name": "Reds6k", "count": 1, "classification": ItemClassification.filler},
    {"name": "Blues300", "count": 1, "classification": ItemClassification.filler},
    {"name": "Reds8k", "count": 1, "classification": ItemClassification.filler},
    {"name": "Blues500", "count": 1, "classification": ItemClassification.filler},
    {"name": "Reds10k", "count": 1, "classification": ItemClassification.filler},
    {"name": "Blues800", "count": 1, "classification": ItemClassification.filler},
    {"name": "Yellows5", "count": 1, "classification": ItemClassification.filler},
    {"name": "Reds15k", "count": 1, "classification": ItemClassification.filler},
    {"name": "Blues1.2k", "count": 1, "classification": ItemClassification.filler},
    {"name": "Yellows10", "count": 1, "classification": ItemClassification.filler},
    {"name": "Reds20k", "count": 1, "classification": ItemClassification.filler},
    {"name": "Blues1.6k", "count": 1, "classification": ItemClassification.filler},
    {"name": "Yellows15", "count": 1, "classification": ItemClassification.filler},
    {"name": "Reds30k", "count": 1, "classification": ItemClassification.filler},
    {"name": "Blues2k", "count": 1, "classification": ItemClassification.filler},
    {"name": "Reds50k", "count": 1, "classification": ItemClassification.filler},
    {"name": "Blues4k", "count": 1, "classification": ItemClassification.filler},
    {"name": "Reds100k", "count": 1, "classification": ItemClassification.filler},
    {"name": "Blues8k", "count": 1, "classification": ItemClassification.filler},
]

crypto_level_items: list[ItemDict] = [
    {"name": "CryptoLevel", "count": 36, "classification": ItemClassification.filler}
]

boss_drop_items: list[ItemDict] = [
    {"name": "Boss Drop", "count": 26, "classification": ItemClassification.progression},
]

junk_items: list[ItemDict] = [
    {"name": "Extra Bits", "count": 0, "classification": ItemClassification.filler},
    {"name": "Extra Nodes", "count": 0, "classification": ItemClassification.filler},
]

goal_items: list[ItemDict] = [
    {"name": "Virus Deployed", "count": 0, "classification": ItemClassification.progression}
]

progressive_items: list[ItemDict] = [
    {"name": "Progressive Damage", "count": 43, "classification": ItemClassification.progression},
    {"name": "Progressive Additional Damage", "count": 26, "classification": ItemClassification.progression},
    {"name": "Progressive Damage Per Second", "count": 3, "classification": ItemClassification.progression},
    {"name": "Progressive Critical Damage", "count": 18, "classification": ItemClassification.progression},
    {"name": "Progressive Boss Damage", "count": 20, "classification": ItemClassification.progression},
    {"name": "Progressive Health", "count": 51, "classification": ItemClassification.progression},
    {"name": "Progressive Regen", "count": 25, "classification": ItemClassification.progression},
    {"name": "Progressive Lifesteal", "count": 16, "classification": ItemClassification.progression},
    {"name": "Progressive SpawnRate", "count": 26, "classification": ItemClassification.progression},
    {"name": "Progressive Blue Spawn", "count": 5, "classification": ItemClassification.progression},
    {"name": "Progressive Yellow Spawn", "count": 2, "classification": ItemClassification.progression},
    {"name": "Progressive Armor", "count": 116, "classification": ItemClassification.progression},
    {"name": "Progressive Boss Armor", "count": 18, "classification": ItemClassification.progression},
    {"name": "Progressive Infinity", "count": 9, "classification": ItemClassification.progression},
    #{ "name": "Progressive Milestone Reward", "count":25,"classification":ItemClassification.filler},
    {"name": "Progressive Red Milestone Reward", "count": 11, "classification": ItemClassification.filler},
    {"name": "Progressive Blue Milestone Reward", "count": 11, "classification": ItemClassification.filler},
    {"name": "Progressive Yellow Milestone Reward", "count": 3, "classification": ItemClassification.filler},
]

progressive_items_exclude_list: list[str] = [
    # Progressive Damage
    "Damage1", "Damage2", "Damage3", "Damage4", "Damage5",
    # Progressive Additional Damage
    "DamagePerEnemy1", "Undamaged1", "Execute1", "Undamaged2", "Execute2", "MaxHealthToDamage1",
    # Progressive Damage Per Second
    "RampingDamage1",
    # Progressive Critical Damage
    "CritDamage1", "CritDamage2",
    # Progressive Boss Damage
    "BossDamage1", "BossDamage2",
    # Progressive Health
    "Health1", "Health2", "Health3", "Health4", "Health5", "Health6", "Health7",
    # Progressive Regen
    "HealthRegen1", "HealthRegen2", "DropHeal1", "MaxHealthHeal1",
    "StealMaxHealth1", "MaxHealthHeal2", "StealMaxHealth2", "StealMaxHealth3",
    # Progressive Lifesteal
    "Salvaging1", "Lifesteal1", "Salvaging2", "Lifesteal2", "Lifesteal3",
    # Progressive SpawnRate
    "SpawnRate1", "SpawnRate2", "SpawnRate3", "SpawnRate4",
    # Progressive Blue Spawn
    "NodeFinder1",
    # Progressive Yellow Spawn
    "YellowSpawn1", "YellowSpawn2",
    # Progressive Armor
    "Armor1", "Armor2", "ArmorPerEnemy1", "Armor3", "Armor4", "Armor5", "Armor6",
    "MaxHealthToArmor1", "Armor7", "FocusArmor1", "MaxHealthToArmor2", "RampingArmor1",
    # Progressive Boss Armor
    "BossArmor1", "BossArmor2",
    # Progressive Infinity
    "Infinity1", "Infinity2", "Infinity3", "Infinity4",
    "Infinity5", "Infinity6", "Infinity7", "Infinity8", "Infinity9",
    # Progressive Red Milestone Reward
    "Reds500", "Reds2k", "Reds4k", "Reds6k", "Reds8k",
    "Reds10k", "Reds15k", "Reds20k", "Reds30k", "Reds50k", "Reds100k",
    # Progressive Blue Milestone Reward
    "Blues10", "Blues100", "Blues200", "Blues300", "Blues500",
    "Blues800", "Blues1.2k", "Blues1.6k", "Blues2k", "Blues4k", "Blues8k",
    # Progressive Yellow Milestone Reward
    "Yellows5", "Yellows10", "Yellows15",
]

progressive_item_map: dict = {
    "Progressive Damage": {
        "Damage1": {"start": 0, "count": 15, "power": 1},   #max solo/cm pow= 15/15
        "Damage2": {"start": 15, "count": 10, "power": 3},  #max solo/cm pow= 30/45
        "Damage3": {"start": 25, "count": 10, "power": 6},  #max solo/cm pow= 60/105
        "Damage4": {"start": 35, "count": 3, "power": 25},  #max solo/cm pow= 75/180
        "Damage5": {"start": 38, "count": 5, "power": 100}, #max solo/cm pow= 500/680
    },

    "Progressive Additional Damage": {
        "DamagePerEnemy1": {"start": 0, "count": 5, "power": 1},
        "Undamaged1": {"start": 5, "count": 6, "power": 1},
        "Execute1": {"start": 11, "count": 6, "power": 1},
        "Undamaged2": {"start": 17, "count": 4, "power": 1},
        "Execute2": {"start": 21, "count": 4, "power": 1},
        "MaxHealthToDamage1": {"start": 25, "count": 1, "power": 1},
    },

    "Progressive Damage Per Second": {
        "RampingDamage1": {"start": 0, "count": 3, "power": 1},
    },

    "Progressive Critical Damage": {
        "CritDamage1": {"start": 0, "count": 10, "power": 50},
        "CritDamage2": {"start": 10, "count": 8, "power": 200},
    },

    "Progressive Boss Damage": {
        "BossDamage1": {"start": 0, "count": 10, "power": 50},
        "BossDamage2": {"start": 10, "count": 10, "power": 100},
    },

    "Progressive Health": {
        "Health1": {"start": 0, "count": 10, "power": 4},
        "Health2": {"start": 10, "count": 8, "power": 12},
        "Health3": {"start": 18, "count": 10, "power": 80},
        "Health4": {"start": 28, "count": 10, "power": 300},
        "Health5": {"start": 38, "count": 3, "power": 4000},
        "Health6": {"start": 41, "count": 5, "power": 50000},
        "Health7": {"start": 46, "count": 5, "power": 100000},
    },

    "Progressive Regen": {
        "HealthRegen1": {"start": 0, "count": 5, "power": 1},
        "HealthRegen2": {"start": 5, "count": 1, "power": 1},
        "DropHeal1": {"start": 6, "count": 1, "power": 1},
        "MaxHealthHeal1": {"start": 7, "count": 10, "power": 1},
        "StealMaxHealth1": {"start": 17, "count": 1, "power": 1},
        "MaxHealthHeal2": {"start": 18, "count": 5, "power": 1},
        "StealMaxHealth2": {"start": 23, "count": 1, "power": 1},
        "StealMaxHealth3": {"start": 24, "count": 1, "power": 1},
    },

    "Progressive Lifesteal": {
        "Salvaging1": {"start": 0, "count": 5, "power": 1},     #max solo/cm pow= 5/5
        "Lifesteal1": {"start": 5, "count": 5, "power": 50},    #max solo/cm pow= 250/255
        "Salvaging2": {"start": 10, "count": 1, "power": 8},    #max solo/cm pow= 8/263
        "Lifesteal2": {"start": 11, "count": 3, "power": 1000}, #max solo/cm pow= 3000/3263
        "Lifesteal3": {"start": 14, "count": 2, "power": 5000}, #max solo/cm pow= 10000/13263
    },

    "Progressive SpawnRate": {
        "SpawnRate1": {"start": 0, "count": 15, "power": 50},  #max solo/cm pow= 750/750
        "SpawnRate2": {"start": 15, "count": 1, "power": 200}, #max solo/cm pow= 200/950
        "SpawnRate3": {"start": 16, "count": 5, "power": 100}, #max solo/cm pow= 500/1450
        "SpawnRate4": {"start": 21, "count": 5, "power": 400}, #max solo/cm pow= 2000/3450
    },

    "Progressive Blue Spawn": {
        "NodeFinder1": {"start": 0, "count": 5, "power": 1},
    },

    "Progressive Yellow Spawn": {
        "YellowSpawn1": {"start": 0, "count": 1, "power": 1},
        "YellowSpawn2": {"start": 1, "count": 1, "power": 1},
    },

    "Progressive Armor": {
        "Armor1": {"start": 0, "count": 10, "power": 1},
        "Armor2": {"start": 10, "count": 5, "power": 1},
        "ArmorPerEnemy1": {"start": 15, "count": 10, "power": 1},
        "Armor3": {"start": 25, "count": 10, "power": 1},
        "Armor4": {"start": 35, "count": 10, "power": 1},
        "Armor5": {"start": 45, "count": 20, "power": 1},
        "Armor6": {"start": 65, "count": 30, "power": 1},
        "MaxHealthToArmor1": {"start": 95, "count": 5, "power": 1},
        "Armor7": {"start": 100, "count": 5, "power": 1},
        "FocusArmor1": {"start": 105, "count": 5, "power": 1},
        "MaxHealthToArmor2": {"start": 110, "count": 1, "power": 1},
        "RampingArmor1": {"start": 111, "count": 5, "power": 1},
    },

    "Progressive Boss Armor": {
        "BossArmor1": {"start": 0, "count": 10, "power": 1},
        "BossArmor2": {"start": 10, "count": 8, "power": 25},
    },

    "Progressive Infinity": {
        "Infinity1": {"start": 0, "count": 1, "power": 1},
        "Infinity2": {"start": 1, "count": 1, "power": 1},
        "Infinity3": {"start": 2, "count": 1, "power": 1},
        "Infinity4": {"start": 3, "count": 1, "power": 1},
        "Infinity5": {"start": 4, "count": 1, "power": 1},
        "Infinity6": {"start": 5, "count": 1, "power": 1},
        "Infinity7": {"start": 6, "count": 1, "power": 1},
        "Infinity8": {"start": 7, "count": 1, "power": 1},
        "Infinity9": {"start": 8, "count": 1, "power": 1},
    },

    "Progressive Red Milestone Reward": {
        "Reds500": {"start": 0, "count": 1, "power": 1},
        "Reds2k": {"start": 1, "count": 1, "power": 1},
        "Reds4k": {"start": 2, "count": 1, "power": 1},
        "Reds6k": {"start": 3, "count": 1, "power": 1},
        "Reds8k": {"start": 4, "count": 1, "power": 1},
        "Reds10k": {"start": 5, "count": 1, "power": 1},
        "Reds15k": {"start": 6, "count": 1, "power": 1},
        "Reds20k": {"start": 7, "count": 1, "power": 1},
        "Reds30k": {"start": 8, "count": 1, "power": 1},
        "Reds50k": {"start": 9, "count": 1, "power": 1},
        "Reds100k": {"start": 10, "count": 1, "power": 1},
    },

    "Progressive Blue Milestone Reward": {
        "Blues10": {"start": 0, "count": 1, "power": 1},
        "Blues100": {"start": 1, "count": 1, "power": 1},
        "Blues200": {"start": 2, "count": 1, "power": 1},
        "Blues300": {"start": 3, "count": 1, "power": 1},
        "Blues500": {"start": 4, "count": 1, "power": 1},
        "Blues800": {"start": 5, "count": 1, "power": 1},
        "Blues1.2k": {"start": 6, "count": 1, "power": 1},
        "Blues1.6k": {"start": 7, "count": 1, "power": 1},
        "Blues2k": {"start": 8, "count": 1, "power": 1},
        "Blues4k": {"start": 9, "count": 1, "power": 1},
        "Blues8k": {"start": 10, "count": 1, "power": 1},
    },

    "Progressive Yellow Milestone Reward": {
        "Yellows5": {"start": 0, "count": 1, "power": 1},
        "Yellows10": {"start": 1, "count": 1, "power": 1},
        "Yellows15": {"start": 2, "count": 1, "power": 1},
    }
}

all_items = upgrade_items + milestone_items + crypto_level_items + boss_drop_items + progressive_items + goal_items + junk_items
all_items_to_id = {item["name"]: i + base_id for i, item in enumerate(all_items)}


def progressive_item_to_vanilla(upgrade: str, count: int):
    vanilla_items = {}
    group = progressive_item_map[upgrade]
    for item in group.keys():
        value = group[item]
        value_last_item_count = value["start"] + value["count"]
        if value["start"] > count:
            continue
        elif value["start"] < count and value_last_item_count < count:
            for i in range(value["count"]):
                if item not in vanilla_items:
                    vanilla_items[item] = 1
                else:
                    vanilla_items[item] = vanilla_items[item] + 1
        else:
            for i in range(value["count"]):
                value_w_startcount = value["start"] + i
                if count > value_w_startcount:
                    if item not in vanilla_items:
                        vanilla_items[item] = 1
                    else:
                        vanilla_items[item] = vanilla_items[item] + 1
    return vanilla_items


def get_power_from_progressive_item(upgrade: str, count: int):
    power = 0
    group = progressive_item_map[upgrade]
    for item in group.keys():
        value = group[item]
        value_last_item_count = value["start"] + value["count"]
        if value["start"] > count:
            continue
        elif value["start"] < count and value_last_item_count < count:
            for i in range(value["count"]):
                power = power + value["power"]
        else:
            for i in range(value["count"]):
                value_w_startcount = value["start"] + i
                if count > value_w_startcount:
                    power = power + value["power"]
    return power


def get_power_from_vanilla_items(upgrade: str, count: int):
    """
    Calculate power of single item with a count
    :param upgrade:
    :param count:
    :return:
    """
    power = 0
    for group in progressive_item_map.keys():
        for item in progressive_item_map[group].keys():
            if item != upgrade:
                continue
            value = progressive_item_map[group][item]
            for i in range(value["count"]):
                if count > i:
                    power = power + value["power"]
    return power
