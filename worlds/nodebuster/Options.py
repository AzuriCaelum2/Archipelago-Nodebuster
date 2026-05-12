from dataclasses import dataclass

from Options import Toggle, Choice, DeathLinkMixin, PerGameCommonOptions


class Goal(Choice):
    """
    Defines the goal to accomplish in order to complete the randomizer.

    - Release Virus.
    - Release Virus with all 9 infinity upgrades unlocked.
    """
    display_name = "Goal"
    option_release_virus = 0
    option_release_virus_with_infinity = 1
    default = 0


class ProgressiveItems(Toggle):
    """
    Replaces a large portion of items in the pool with progressive versions for the respective upgrade.
    """
    display_name = "Progressive Items"


class CryptoMine(Toggle):
    """
    Adds the 36 levels of the CryptoMine into the pool.
    When you level up the crypto mine, instead of speeding up the crypto mine it will instead give you a randomized item from the pool.
    """

    display_name = "Crypto Mine"


class Milestones(Toggle):
    """
    Adds the Milestones Rewards and Locations to the item pool.
    """
    display_name = "Milestones"


class BossDrops(Choice):
    """
    Randomize Boss Drops.

    - None - No boss drops will be randomized.
    - Necessary Only - All boss drops are randomized but only 18 cores and 8 filler items.
    - All 26 - All 26 levels of boss drops will be randomized.
    """
    display_name = "Boss Drops"
    option_none = 0
    option_necessary = 1
    option_all_26 = 2
    default = 0


@dataclass
class NodebusterOptions(DeathLinkMixin, PerGameCommonOptions):
    goal: Goal
    crypto: CryptoMine
    milestone: Milestones
    bossdrops: BossDrops
    progressive_items: ProgressiveItems
