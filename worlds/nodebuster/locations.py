from BaseClasses import Location

base_id = 268000


class NodebusterLocation(Location):
    game: str = "Nodebuster"


def get_upgrade_tree_locations() -> list[str]:
    locations = []
    locations += damage_1_locations
    locations += endurance_locations
    locations += crowding_locations
    locations += firewall_locations
    locations += influence_locations
    locations += boss_guard_locations
    locations += repair_tool_locations
    locations += salvaging_locations
    locations += connection_buster_locations
    locations += giant_slayer_locations
    locations += repeating_locations
    locations += bit_boost_locations
    locations += plundering_locations
    locations += proficiency_locations
    locations += magnet_locations
    locations += repeat_repeating_locations
    locations += swarming_locations
    locations += antivirus_locations
    locations += swarm_defense_system_locations
    locations += bolster_locations
    locations += better_endurance_locations
    locations += self_repair_locations
    locations += big_heart_locations
    locations += node_boost_locations
    locations += node_finder_locations
    locations += infesting_locations
    locations += bit_armor_locations
    locations += domain_expansion_locations
    locations += byte_armor_locations
    locations += colossus_slayer_locations
    locations += big_locations
    locations += focus_armor_locations
    locations += potency_locations
    locations += last_strike_locations
    locations += crit_chance_locations
    locations += nodeblade_locations
    locations += crit_damage_locations
    locations += first_strike_locations
    locations += ambush_locations
    locations += finishing_blow_locations
    locations += pulse_bolts_locations
    locations += bolt_damage_locations
    locations += bolt_count_locations
    locations += bolt_burst_locations
    locations += bolt_barrage_locations
    locations += skilled_salvager_locations
    locations += sapper_locations
    locations += patcher_locations
    locations += scaling_regeneration_locations
    locations += super_armor_locations
    locations += anti_purple_locations
    locations += blood_armor_locations
    locations += auto_collect_locations
    locations += crypto_mine_locations
    locations += milestone_locations
    locations += spawn_exploders_locations
    locations += thundering_locations
    locations += pulser_pursuit_locations
    locations += pulse_thumper_locations
    locations += unending_parasite_locations
    locations += parasite_evolution_locations
    locations += bolt_lethality_locations
    locations += drainer_locations
    locations += blood_visage_locations
    locations += processor_acquisition_locations
    locations += auto_pulser_locations
    locations += netblade_locations
    locations += bloodblade_locations
    locations += big_crit_locations
    locations += overloaded_location
    locations += transplant_locations
    locations += blood_injection_locations
    locations += instant_repair_locations
    locations += insatiable_locations
    locations += indomitable_locations
    locations += beyond_locations
    locations += net_armor_locations
    locations += infinity_locations
    return locations


def get_milestone_locations() -> list[str]:
    milestone_reward_locations = []
    milestone_reward_locations += red_locations
    milestone_reward_locations += blue_locations
    milestone_reward_locations += yellow_locations
    return milestone_reward_locations


def get_boss_locations() -> list[str]:
    return boss_locations


def get_crypto_locations() -> list[str]:
    return crypto_mine_levels


damage_1_locations = [
    "Damage1-1", #1r
    "Damage1-2", #2r
    "Damage1-3", #3r
    "Damage1-4", #3r
    "Damage1-5", #4r
    "Damage1-6", #5r
    "Damage1-7", #7r
    "Damage1-8", #9r
    "Damage1-9", #11r
    "Damage1-10", #13r
    "Damage1-11", #15r
    "Damage1-12", #20r
    "Damage1-13", #25r
    "Damage1-14", #30r
    "Damage1-15", #35r
]

endurance_locations = [
    "Health1-1", #2r
    "Health1-2", #3r
    "Health1-3", #4r
    "Health1-4", #5r
    "Health1-5", #6r
    "Health1-6", #7r
    "Health1-7", #8r
    "Health1-8", #10r
    "Health1-9", #11r
    "Health1-10", #12r
]

crowding_locations = [
    "SpawnRate1-1", #2r
    "SpawnRate1-2", #4r
    "SpawnRate1-3", #6r
    "SpawnRate1-4", #8r
    "SpawnRate1-5", #10r
    "SpawnRate1-6", #14r
    "SpawnRate1-7", #20r
    "SpawnRate1-8", #30r
    "SpawnRate1-9", #50r
    "SpawnRate1-10", #70r
    "SpawnRate1-11", #100r
    "SpawnRate1-12", #130r
    "SpawnRate1-13", #160r
    "SpawnRate1-14", #200r
    "SpawnRate1-15", #250r
]

firewall_locations = [
    "Armor1-1", #8r
    "Armor1-2", #10r
    "Armor1-3", #14r
    "Armor1-4", #18r
    "Armor1-5", #22r
    "Armor1-6", #26r
    "Armor1-7", #30r
    "Armor1-8", #30r
    "Armor1-9", #30r
    "Armor1-10", #30r
]

influence_locations = [
    "Size1-1", #10r
    "Size1-2", #20r
    "Size1-3", #30r
    "Size1-4", #40r
    "Size1-5", #50r
    "Size1-6", #60r
    "Size1-7", #70r
    "Size1-8", #80r
    "Size1-9", #90r
    "Size1-10", #100r
]

boss_guard_locations = [
    "BossArmor1-1", #15r
    "BossArmor1-2", #18r
    "BossArmor1-3", #21r
    "BossArmor1-4", #26r
    "BossArmor1-5", #32r
    "BossArmor1-6", #38r
    "BossArmor1-7", #44r
    "BossArmor1-8", #50r
    "BossArmor1-9", #56r
    "BossArmor1-10", #62r
]

repair_tool_locations = [
    "HealthRegen1-1", #25r
    "HealthRegen1-2", #25r
    "HealthRegen1-3", #25r
    "HealthRegen1-4", #30r
    "HealthRegen1-5", #30r
]

salvaging_locations = [
    "Salvaging1-1", #100r
    "Salvaging1-2", #125r
    "Salvaging1-3", #150r
    "Salvaging1-4", #175r
    "Salvaging1-5", #200r
]

connection_buster_locations = [
    "DamagePerEnemy1-1", #50r
    "DamagePerEnemy1-2", #100r
    "DamagePerEnemy1-3", #200r
    "DamagePerEnemy1-4", #500r
    "DamagePerEnemy1-5", #1000r
]

giant_slayer_locations = [
    "BossDamage1-1", #60r
    "BossDamage1-2", #80r
    "BossDamage1-3", #100r
    "BossDamage1-4", #160r
    "BossDamage1-5", #300r
    "BossDamage1-6", #500r
    "BossDamage1-7", #700r
    "BossDamage1-8", #1000r
    "BossDamage1-9", #1300r
    "BossDamage1-10", #1600r
]

repeating_locations = [
    "AttackSpeed1-1", #1sp
]

bit_boost_locations =[
    "BitBoost1-1", #sp1
]

plundering_locations = [
    "BonusDropChance1-1", #150r
    "BonusDropChance1-2", #400r
    "BonusDropChance1-3", #1000r
    "BonusDropChance1-4", #4000r
    "BonusDropChance1-5", #10000r
]

proficiency_locations = [
    "Damage2-1", #200r
    "Damage2-2", #210r
    "Damage2-3", #220r
    "Damage2-4", #230r
    "Damage2-5", #240r
    "Damage2-6", #260r
    "Damage2-7", #280r
    "Damage2-8", #300r
    "Damage2-9", #320r
    "Damage2-10", #340r
]

magnet_locations = [
    "PickupRadius1-1", #300r
    "PickupRadius1-2", #1400r
    "PickupRadius1-3", #4000r
    "PickupRadius1-4", #15000r
    "PickupRadius1-5", #70000r
]

repeat_repeating_locations = [
    "AttackSpeed2-1", #1p
]

swarming_locations = [
    "SpawnRate2-1", #1p
]

antivirus_locations = [
    "Armor2-1", #150r
    "Armor2-2", #170r
    "Armor2-3", #190r
    "Armor2-4", #200r
    "Armor2-5", #210r
]

swarm_defense_system_locations = [
    "ArmorPerEnemy1-1", #300r
    "ArmorPerEnemy1-2", #350r
    "ArmorPerEnemy1-3", #400r
    "ArmorPerEnemy1-4", #450r
    "ArmorPerEnemy1-5", #500r
    "ArmorPerEnemy1-6", #650r
    "ArmorPerEnemy1-7", #800r
    "ArmorPerEnemy1-8", #1000r
    "ArmorPerEnemy1-9", #1200r
    "ArmorPerEnemy1-10", #1600r
]

better_endurance_locations = [
    "Health2-1", #60r
    "Health2-2", #65r
    "Health2-3", #70r
    "Health2-4", #75r
    "Health2-5", #80r
    "Health2-6", #85r
    "Health2-7", #90r
    "Health2-8", #95r
]

self_repair_locations = [
    "HealthRegen2-1" #1sp
]

big_heart_locations = [
    "Health3-1", #500r
    "Health3-2", #500r
    "Health3-3", #525r
    "Health3-4", #525r
    "Health3-5", #550r
    "Health3-6", #550r
    "Health3-7", #600r
    "Health3-8", #600r
    "Health3-9", #600r
    "Health3-10", #600r
]

bolster_locations = [
    "Armor3-1", #450r
    "Armor3-2", #460r
    "Armor3-3", #480r
    "Armor3-4", #500r
    "Armor3-5", #500r
    "Armor3-6", #510r
    "Armor3-7", #520r
    "Armor3-8", #530r
    "Armor3-9", #540r
    "Armor3-10", #550r
]

super_armor_locations = [
    "Armor4-1", #700r
    "Armor4-2", #700r
    "Armor4-3", #725r
    "Armor4-4", #750r
    "Armor4-5", #750r
    "Armor4-6", #775r
    "Armor4-7", #775r
    "Armor4-8", #800r
    "Armor4-9", #800r
    "Armor4-10", #800r
]

node_finder_locations = [
    "NodeFinder1-1", #400r
    "NodeFinder1-2", #1500r
    "NodeFinder1-3", #3000r
    "NodeFinder1-4", #5000r
    "NodeFinder1-5", #10000r
]

node_boost_locations = [
    "NodeBoost1-1", #1sp
]

milestone_locations = [
    "Milestones-1" #1b
]

infesting_locations = [
    "SpawnRate3-1", #2000r
    "SpawnRate3-2", #2200r
    "SpawnRate3-3", #2400r
    "SpawnRate3-4", #3000r
    "SpawnRate3-5", #6000r
]

bit_armor_locations = [
    "Armor5-1", #300r
    "Armor5-2", #300r
    "Armor5-3", #300r
    "Armor5-4", #300r
    "Armor5-5", #300r
    "Armor5-6", #300r
    "Armor5-7", #300r
    "Armor5-8", #300r
    "Armor5-9", #300r
    "Armor5-10", #300r
    "Armor5-11", #300r
    "Armor5-12", #300r
    "Armor5-13", #300r
    "Armor5-14", #300r
    "Armor5-15", #300r
    "Armor5-16", #300r
    "Armor5-17", #300r
    "Armor5-18", #300r
    "Armor5-19", #300r
    "Armor5-20", #300r
]

domain_expansion_locations = [
    "Size2-1", #1p
]

byte_armor_locations = [
    "Armor6-1", #700r
    "Armor6-2", #700r
    "Armor6-3", #700r
    "Armor6-4", #700r
    "Armor6-5", #700r
    "Armor6-6", #700r
    "Armor6-7", #700r
    "Armor6-8", #700r
    "Armor6-9", #700r
    "Armor6-10", #700r
    "Armor6-11", #700r
    "Armor6-12", #700r
    "Armor6-13", #700r
    "Armor6-14", #700r
    "Armor6-15", #700r
    "Armor6-16", #700r
    "Armor6-17", #700r
    "Armor6-18", #700r
    "Armor6-19", #700r
    "Armor6-20", #700r
    "Armor6-21", #700r
    "Armor6-22", #700r
    "Armor6-23", #700r
    "Armor6-24", #700r
    "Armor6-25", #700r
    "Armor6-26", #700r
    "Armor6-27", #700r
    "Armor6-28", #700r
    "Armor6-29", #700r
    "Armor6-30", #700r
]

colossus_slayer_locations = [
    "BossDamage2-1", #5000r
    "BossDamage2-2", #6000r
    "BossDamage2-3", #7000r
    "BossDamage2-4", #8000r
    "BossDamage2-5", #9000r
    "BossDamage2-6", #10000r
    "BossDamage2-7", #11000r
    "BossDamage2-8", #12000r
    "BossDamage2-9", #13000r
    "BossDamage2-10", #14000r
]

big_locations = [
    "Size3-1", #1p
    "Size3-2", #1p
    "Size3-3", #1p
]

focus_armor_locations = [
    "FocusArmor1-1", #8000r
    "FocusArmor1-2", #9000r
    "FocusArmor1-3", #10000r
    "FocusArmor1-4", #11000r
    "FocusArmor1-5"  #12000r
]

potency_locations = [
    "Damage3-1", #5b
    "Damage3-2", #6b
    "Damage3-3", #7b
    "Damage3-4", #8b
    "Damage3-5", #9b
    "Damage3-6", #10b
    "Damage3-7", #10b
    "Damage3-8", #10b
    "Damage3-9", #10b
    "Damage3-10", #10b
]

first_strike_locations = [
    "Undamaged1-1", #1000r
    "Undamaged1-2", #1200r
    "Undamaged1-3", #1400r
    "Undamaged1-4", #1600r
    "Undamaged1-5", #1800r
    "Undamaged1-6", #2000r
]

last_strike_locations = [
    "Execute1-1", #1000r
    "Execute1-2", #1200r
    "Execute1-3", #1400r
    "Execute1-4", #1600r
    "Execute1-5", #1800r
    "Execute1-6", #2000r
]

crit_chance_locations = [
    "CritChance1-1", #1000r
    "CritChance1-2", #2000r
    "CritChance1-3", #3000r
    "CritChance1-4", #4000r
    "CritChance1-5", #6000r
    "CritChance1-6", #8000r
    "CritChance1-7", #12000r
    "CritChance1-8", #16000r
    "CritChance1-9", #20000r
    "CritChance1-10", #24000r
]

nodeblade_locations = [
    "Damage4-1", #50b
    "Damage4-2", #50b
    "Damage4-3", #50b
]

crit_damage_locations = [
    "CritDamage1-1", #6000r
    "CritDamage1-2", #8000r
    "CritDamage1-3", #10000r
    "CritDamage1-4", #12000r
    "CritDamage1-5", #14000r
    "CritDamage1-6", #16000r
    "CritDamage1-7", #18000r
    "CritDamage1-8", #20000r
    "CritDamage1-9", #22000r
    "CritDamage1-10", #24000r
]

ambush_locations = [
    "Undamaged2-1", #10000r
    "Undamaged2-2", #12000r
    "Undamaged2-3", #15000r
    "Undamaged2-4", #20000r
]

finishing_blow_locations = [
    "Execute2-1", #10000r
    "Execute2-2", #12000r
    "Execute2-3", #15000r
    "Execute2-4" #20000r
]

pulse_bolts_locations = [
    "PulseBolts-1", #12b
]

bolt_damage_locations = [
    "PulseBoltDamage1-1", #400r
    "PulseBoltDamage1-2", #500r
    "PulseBoltDamage1-3", #600r
    "PulseBoltDamage1-4", #800r
    "PulseBoltDamage1-5", #1000r
    "PulseBoltDamage1-6", #1200r
    "PulseBoltDamage1-7", #1400r
    "PulseBoltDamage1-8", #1600r
    "PulseBoltDamage1-9", #1800r
    "PulseBoltDamage1-10", #2000r
]

bolt_count_locations = [
    "PulseBoltCount1-1", #1sp
    "PulseBoltCount1-2", #1sp
    "PulseBoltCount1-3", #1sp
    "PulseBoltCount1-4", #1sp
    "PulseBoltCount1-5", #1sp
]

bolt_burst_locations = [
    "PulseBoltExplode-1", #300b
]

bolt_barrage_locations = [
    "PulseBoltCount2-1", #1p
]

skilled_salvager_locations = [
    "Salvaging2-1" #12b
]

sapper_locations = [
    "Lifesteal1-1", #2b
    "Lifesteal1-2", #3b
    "Lifesteal1-3", #4b
    "Lifesteal1-4", #5b
    "Lifesteal1-5", #6b
]

patcher_locations = [
    "DropHeal1-1", #1p
]

scaling_regeneration_locations = [
    "MaxHealthHeal1-1", #8b
    "MaxHealthHeal1-2", #10b
    "MaxHealthHeal1-3", #12b
    "MaxHealthHeal1-4", #14b
    "MaxHealthHeal1-5", #18b
    "MaxHealthHeal1-6", #22b
    "MaxHealthHeal1-7", #26b
    "MaxHealthHeal1-8", #30b
    "MaxHealthHeal1-9", #36b
    "MaxHealthHeal1-10", #45b
]

anti_purple_locations = [
    "BossArmor2-1", #8b
    "BossArmor2-2", #10b
    "BossArmor2-3", #12b
    "BossArmor2-4", #14b
    "BossArmor2-5", #16b
    "BossArmor2-6", #20b
    "BossArmor2-7", #30b
    "BossArmor2-8", #45b
]

blood_armor_locations = [
    "MaxHealthToArmor1-1", #100b
    "MaxHealthToArmor1-2", #150b
    "MaxHealthToArmor1-3", #200b
    "MaxHealthToArmor1-4", #250b
    "MaxHealthToArmor1-5", #300b
]

auto_collect_locations = [
    "AutoCollect-1", #300b
    "AutoCollect-2", #500b
    "AutoCollect-3", #1000b
    "AutoCollect-4", #2000b
    "AutoCollect-5", #4000b
    "AutoCollect-6", #6000b
    "AutoCollect-7", #8000b
    "AutoCollect-8", #10000b
]

crypto_mine_locations = [
    "CryptoMine-1" #50b
]

spawn_exploders_locations = [
    "ExplodersChance-1", #3b
    "ExplodersSize-1", #1sp
    "ExplodersSize-2", #1sp
    "ExplodersSize-3", #1sp
    "ExplodersSize-4", #1sp
    "ExplodersSize-5", #1sp
]

thundering_locations = [
    "LightningDamage1-1", #500b
    "LightningDamage1-2", #600b
    "LightningDamage1-3", #700b
    "LightningDamage1-4", #800b
    "LightningDamage1-5", #900b
    "LightningDamage1-6", #1000b
    "LightningDamage1-7", #1100b
    "LightningDamage1-8", #1200b
]

pulser_pursuit_locations = [
    "MovingPulserSpeed1-1", #100b
    "MovingPulserSpeed1-2", #125b
    "MovingPulserSpeed1-3", #150b
    "MovingPulserSpeed1-4", #175b
    "MovingPulserSpeed1-5", #200b
]

pulse_thumper_locations = [
    "MovingPulserSize1-1", #50b
    "MovingPulserSize1-2", #100b
    "MovingPulserSize1-3", #150b
    "MovingPulserSize1-4", #200b
    "MovingPulserSize1-5", #300b
    "MovingPulserSize1-6", #400b

    "MovingPulserSize2-1", #1sp

    "MovingPulserAttackSpeed1-1", #1sp
    "MovingPulserAttackSpeed1-2", #1sp
    "MovingPulserAttackSpeed1-3", #1sp
    "MovingPulserAttackSpeed1-4", #1sp
    "MovingPulserAttackSpeed1-5", #1sp
]

unending_parasite_locations = [
    "StealMaxHealth1-1", #300b
]

parasite_evolution_locations = [
    "StealMaxHealth2-1", #600b
]

insatiable_locations = [
    "StealMaxHealth3-1", #0.6g (60000r)
]

indomitable_locations = [
    "Health6-1", #600b
    "Health6-2", #600b
    "Health6-3", #600b
    "Health6-4", #600b
    "Health6-5", #600b
]

beyond_locations = [
    "Health7-1", #80000r
    "Health7-2", #80000r
    "Health7-3", #80000r
    "Health7-4", #80000r
    "Health7-5", #80000r
]

infinity_locations = [
    "Infinity1-1", #1p
    "Infinity2-1", #1p
    "Infinity3-1", #1p
    "Infinity4-1", #1p
    "Infinity5-1", #1p
    "Infinity6-1", #1p
    "Infinity7-1", #1p
    "Infinity8-1", #1p
    "Infinity9-1", #1p

    "Laboratory-1", #1r

    "YellowSpawn2-1", #1000b
]

bolt_lethality_locations = [
    "PulseBoltDamage2-1", #0.2g (20000r)
    "PulseBoltDamage2-2", #0.25g (25000r)
    "PulseBoltDamage2-3", #0.3g (30000r)

    "EnemyDeathPulseBolts-1", #10000r
    "EnemyDeathPulseBolts-2", #11000r
    "EnemyDeathPulseBolts-3", #12000r
    "EnemyDeathPulseBolts-4", #13000r
    "EnemyDeathPulseBolts-5", #14000r
    "EnemyDeathPulseBolts-6", #15000r
]

drainer_locations = [
    "Lifesteal2-1", #0.02g (2000r)
    "Lifesteal2-2", #0.02g (2000r)
    "Lifesteal2-3", #0.02g (2000r)
    "Lifesteal3-1", #10000r
    "Lifesteal3-2", #50000r
]

blood_visage_locations = [
    "MaxHealthToArmor2-1", #0.5g (50000r)

    "RampingArmor1-1", #50000r
    "RampingArmor1-2", #100000r
    "RampingArmor1-3", #120000r
    "RampingArmor1-4", #140000r
    "RampingArmor1-5", #200000r
]

processor_acquisition_locations = [
    "YellowSpawn1-1", #0.01g (1000r)
]

auto_pulser_locations = [
    "MovingPulser1-1", #0.05g (5000r)
    "MovingPulser1-2", #0.15g (15000r)
    "MovingPulser1-3", #0.4g (40000r)
    "MovingPulser1-4", #0.8g (80000r)
    "MovingPulser1-5", #2g (200000r)
]

netblade_locations = [
    "Damage5-1", #0.05g (5000r)
    "Damage5-2", #0.06g (6000r)
    "Damage5-3", #0.07g (7000r)
    "Damage5-4", #0.08g (8000r)
    "Damage5-5", #0.09g (9000r)

    "RampingDamage1-1", #20000r
    "RampingDamage1-2", #100000r
    "RampingDamage1-3", #200000r

    "LightningChance1-1", #0.7g (70000r)
    "LightningChance1-2", #1g (100000r)
    "LightningChance1-3", #1.3g (130000r)
    "LightningChance1-4", #2g (200000r)
    "LightningChance1-5", #3g (300000r)

    "LightningChainCount1-1", #1sp
    "LightningChainCount1-2", #1sp
    "LightningChainCount1-3", #1sp
    "LightningChainCount1-4", #1sp
    "LightningChainCount1-5", #1sp
    "LightningChainCount1-6", #1sp
    "LightningChainCount1-7", #1sp
    "LightningChainCount1-8", #1sp
]

bloodblade_locations = [
    "MaxHealthToDamage1-1", #100000r
]

big_crit_locations = [
    "CritDamage2-1", #0.8g (80000r)
    "CritDamage2-2", #1g (100000r)
    "CritDamage2-3", #1.2g (120000r)
    "CritDamage2-4", #1.4g (140000r)
    "CritDamage2-5", #1.6g (160000r)
    "CritDamage2-6", #1.8g (180000r)
    "CritDamage2-7", #2g (200000r)
    "CritDamage2-8", #2g (200000r)
]

overloaded_location = [
    "SpawnRate4-1", #0.1g (10000r)
    "SpawnRate4-2", #0.1g (10000r)
    "SpawnRate4-3", #0.1g (10000r)
    "SpawnRate4-4", #0.1g (10000r)
    "SpawnRate4-5", #0.12g (12000r)
]

transplant_locations = [
    "Health4-1", #0.01g (1000r)
    "Health4-2", #0.01g (1000r)
    "Health4-3", #0.01g (1000r)
    "Health4-4", #0.01g (1000r)
    "Health4-5", #0.01g (1000r)
    "Health4-6", #0.012g (1200r)
    "Health4-7", #0.01g (1000r)
    "Health4-8", #0.01g (1000r)
    "Health4-9", #0.01g (1000r)
    "Health4-10", #0.01g (1000r)
]

blood_injection_locations = [
    "Health5-1", #0.06g (6000r)
    "Health5-2", #0.07g (7000r)
    "Health5-3", #0.08g (8000r)
]

instant_repair_locations = [
    "MaxHealthHeal2-1", #0.08g (8000r)
    "MaxHealthHeal2-2", #0.08g (8000r)
    "MaxHealthHeal2-3", #0.08g (8000r)
    "MaxHealthHeal2-4", #0.08g (8000r)
    "MaxHealthHeal2-5", #0.08g (8000r)
]

net_armor_locations = [
    "Armor7-1", #0.06g (6000r)
    "Armor7-2", #0.06g (6000r)
    "Armor7-3", #0.06g (6000r)
    "Armor7-4", #0.06g (6000r)
    "Armor7-5" #0.06g (6000r)
]

blue_locations = [
    "Blues10", #Number indicated blue enemies
    "Blues100", 
    "Blues200", 
    "Blues300", 
    "Blues500", 
    "Blues800",
    "Blues1.2k", 
    "Blues1.6k", 
    "Blues2k", 
    "Blues4k", 
    "Blues8k",
]

yellow_locations = [
    "Yellows5", 
    "Yellows10", 
    "Yellows15",
]

red_locations = [
    "Reds500", #Number indicated red enemies
    "Reds2k",
    "Reds4k",
    "Reds6k",
    "Reds8k",
    "Reds10k",
    "Reds15k",
    "Reds20k",
    "Reds30k",
    "Reds50k",
    "Reds100k",
]

boss_locations = [
    "Boss-0",
    "Boss-1", 
    "Boss-2", 
    "Boss-3", 
    "Boss-4", 
    "Boss-5",
    "Boss-6", 
    "Boss-7", 
    "Boss-8", 
    "Boss-9", 
    "Boss-10",
    "Boss-11", 
    "Boss-12", 
    "Boss-13", 
    "Boss-14", 
    "Boss-15",
    "Boss-16", 
    "Boss-17", 
    "Boss-18", 
    "Boss-19", 
    "Boss-20",
    "Boss-21", 
    "Boss-22", 
    "Boss-23", 
    "Boss-24", 
    "Boss-25"
]

crypto_mine_levels = [
    "CryptoLevel-1", 
    "CryptoLevel-2", 
    "CryptoLevel-3",
    "CryptoLevel-4", 
    "CryptoLevel-5", 
    "CryptoLevel-6",
    "CryptoLevel-7", 
    "CryptoLevel-8", 
    "CryptoLevel-9",
    "CryptoLevel-10", 
    "CryptoLevel-11", 
    "CryptoLevel-12",
    "CryptoLevel-13", 
    "CryptoLevel-14", 
    "CryptoLevel-15",
    "CryptoLevel-16", 
    "CryptoLevel-17", 
    "CryptoLevel-18",
    "CryptoLevel-19", 
    "CryptoLevel-20", 
    "CryptoLevel-21",
    "CryptoLevel-22", 
    "CryptoLevel-23", 
    "CryptoLevel-24",
    "CryptoLevel-25", 
    "CryptoLevel-26", 
    "CryptoLevel-27",
    "CryptoLevel-28", 
    "CryptoLevel-29", 
    "CryptoLevel-30",
    "CryptoLevel-31", 
    "CryptoLevel-32", 
    "CryptoLevel-33",
    "CryptoLevel-34", 
    "CryptoLevel-35", 
    "CryptoLevel-36"
]

goal_locations = [
    "Virus Released"
]

regions_to_locations: dict[str, list[str]] = {
    "Menu": [],
    "Upgrade Tree": [],
    "Milestone Page": [],
    "Damage1Root": damage_1_locations,
    "Endurance": endurance_locations,
    "Crowding": crowding_locations,
    "Firewall": firewall_locations,
    "Influence": influence_locations,
    "Boss Guard": boss_guard_locations,
    "Repair Tool": repair_tool_locations,
    "Salvaging": salvaging_locations,
    "Connection Buster": connection_buster_locations,
    "Giant Slayer": giant_slayer_locations,
    "Repeating": repeating_locations,
    "Bit Boost": bit_boost_locations,
    "Plundering": plundering_locations,
    "Proficiency": proficiency_locations,
    "Magnet": magnet_locations,
    "Repeat-Repeating": repeat_repeating_locations,
    "Swarming": swarming_locations,
    "Antivirus": antivirus_locations,
    "Swarm Defense System": swarm_defense_system_locations,
    "Bolster": bolster_locations,
    "Better Endurance": better_endurance_locations,
    "Self-Repair": self_repair_locations,
    "Big Heart": big_heart_locations,
    "Node Finder": node_finder_locations,
    "Node Boost": node_boost_locations,
    "Focus Armor": focus_armor_locations,
    "Potency": potency_locations,
    "Last Strike": last_strike_locations,
    "Crit Chance": crit_chance_locations,
    "Nodeblade": nodeblade_locations,
    "Crit Damage": crit_damage_locations,
    "First Strike": first_strike_locations,
    "Ambush": ambush_locations,
    "Finishing Blow": finishing_blow_locations,
    "Pulse Bolts": pulse_bolts_locations,
    "Bolt Damage": bolt_damage_locations,
    "Bolt Count": bolt_count_locations,
    "Bolt Burst": bolt_burst_locations,
    "Bolt Barrage": bolt_barrage_locations,
    "Skilled Salvager": skilled_salvager_locations,
    "Sapper": sapper_locations,
    "Patcher": patcher_locations,
    "Scaling Regeneration": scaling_regeneration_locations,
    "Anti-Purple": anti_purple_locations,
    "Blood Armor": blood_armor_locations,
    "Domain Expansion": domain_expansion_locations,
    "Infesting": infesting_locations,
    "Super Armor": super_armor_locations,
    "Bit Armor": bit_armor_locations,
    "Byte Armor": byte_armor_locations,
    "Colossus Slayer": colossus_slayer_locations,
    "B.I.G.": big_locations,
    "Auto-Collect": auto_collect_locations,
    "Crypto Mine": crypto_mine_locations,
    "Milestones": milestone_locations,
    "Spawn Exploders": spawn_exploders_locations,

    # Node Regions off of netcoin
    "Thundering": thundering_locations,
    "Pulser Pursuit": pulser_pursuit_locations,
    "Pulse Thumper": pulse_thumper_locations,
    "Unending Parasite": unending_parasite_locations,
    "Parasite Evolution": parasite_evolution_locations,
    "Insatiable": insatiable_locations,
    "Indomitable": indomitable_locations,
    "Beyond": beyond_locations,
    "Infinity": infinity_locations,

    # Netcoin Regions
    "Bolt Lethality": bolt_lethality_locations,
    "Drainer": drainer_locations,
    "Blood Visage": blood_visage_locations,
    "Processor Acquisition": processor_acquisition_locations,
    "Auto Pulser": auto_pulser_locations,
    "Netblade": netblade_locations,
    "Bloodblade": bloodblade_locations,
    "Big Crit": big_crit_locations,
    "Overloaded": overloaded_location,

    # Netcoin Regions off of main.
    "Transplant": transplant_locations,
    "Blood Injection": blood_injection_locations,
    "Instant Repair": instant_repair_locations,
    "Net Armor": net_armor_locations,

    # Milestone Regions
    "Red Milestones": red_locations,
    "Blue Milestones": blue_locations,
    "Yellow Milestones": yellow_locations,

    # Boss Regions
    # "Boss Drops": boss_locations,
    "Boss Drops": [],
    "Prestige 0":  ["Boss-0"],
    "Prestige 1":  ["Boss-1"],
    "Prestige 2":  ["Boss-2"],
    "Prestige 3":  ["Boss-3"],
    "Prestige 4":  ["Boss-4"],
    "Prestige 5":  ["Boss-5"],
    "Prestige 6":  ["Boss-6"],
    "Prestige 7":  ["Boss-7"],
    "Prestige 8":  ["Boss-8"],
    "Prestige 9":  ["Boss-9"],
    "Prestige 10": ["Boss-10"],
    "Prestige 11": ["Boss-11"],
    "Prestige 12": ["Boss-12"],
    "Prestige 13": ["Boss-13"],
    "Prestige 14": ["Boss-14"],
    "Prestige 15": ["Boss-15"],
    "Prestige 16": ["Boss-16"],
    "Prestige 17": ["Boss-17"],
    "Prestige 18": ["Boss-18"],
    "Prestige 19": ["Boss-19"],
    "Prestige 20": ["Boss-20"],
    "Prestige 21": ["Boss-21"],
    "Prestige 22": ["Boss-22"],
    "Prestige 23": ["Boss-23"],
    "Prestige 24": ["Boss-24"],
    "Prestige 25": ["Boss-25"],

    # Crypto Mine Levels
    "Crypto Levels": crypto_mine_levels,
    "Epilogue": goal_locations
}

all_locations = get_upgrade_tree_locations() + get_milestone_locations() + get_crypto_locations() + get_boss_locations() + goal_locations
all_locations_to_id = {location: i + base_id for i, location in enumerate(all_locations)}
