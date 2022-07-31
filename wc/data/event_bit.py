from ..constants.objectives import MAX_OBJECTIVES

# NOTE: (address - 1e80) * 0x8 + bit
# e.g. (1eb7 - 1e80) * 0x8 + 0x1 = 1b9 (airship visible) 
#      (1f43 - 1e80) * 0x8 + 0x3 = 61b (characters on narshe battlefield)

DISABLE_SAVE_POINT_TUTORIAL = 0x133
DISABLE_CHOCOBO_TUTORIAL = 0x134

VICKS_BROKE_WHELK_GATE = 0x12c
NARSHE_GUARDS_SAW_TERRA_ON_BRIDGE = 0x12d
TERRA_FELL_HOLE_NARSHE = 0x12e
MET_ARVIS = 0x001 # characters no longer ride mtek armor in mines when set
DEFEATED_WHELK = 0x135
NAMED_EDGAR = 0x004
NAMED_SABIN = 0x005
PRISON_DOOR_OPEN_FIGARO_CASTLE = 0x2b7
MET_KEFKA_FIGARO_CASTLE = 0x006
FIRST_NOISE_FIGARO_CAVE = 0x0ae
SECOND_NOISE_FIGARO_CAVE = 0x0af
THIRD_NOISE_FIGARO_CAVE = 0x0b0
DEFEATED_TUNNEL_ARMOR = 0x0b1 # custom, used to be south figaro cave recovery spring
SAW_SHADOW_WALKING_TO_CAFE_SOUTH_FIGARO = 0x00a
NAMED_SHADOW = 0x00b
SAW_VARGAS_SHADOW1 = 0x00d
SAW_VARGAS_SHADOW2 = 0x00e
SAW_VARGAS_SHADOW3 = 0x00f
DEFEATED_VARGAS = 0x010
MET_BANON = 0x011
GOT_GENJI_GLOVES_OR_GAUNTLET = 0x017
RODE_RAFT_FIRST_TIME_LETE_RIVER = 0x019
FOUGHT_ULTROS_LETE_RIVER = 0x01a
RODE_RAFT_LETE_RIVER = 0x257
WOUND_THE_CLOCK_SOUTH_FIGARO = 0x10d
CELES_LOCKE_ESCAPED_SOUTH_FIGARO = 0x01b
NAMED_CELES = 0x01c
FREED_CELES = 0x01d
FINISHED_LOCKE_SCENARIO = 0x01e
NARSHE_SECRET_ENTRANCE_ACCESS = 0x020
FINISHED_NARSHE_CHECKPOINT = 0x2d8 # custom, used to be narshe checkpoint explanation
FINISHED_TERRA_SCENARIO = 0x021
SAW_SHADOW_DREAM1 = 0x024
SAW_SHADOW_DREAM2 = 0x026
SAW_SHADOW_DREAM3 = 0x027
SAW_SHADOW_DREAM4 = 0x028
RECRUITED_SHADOW_GAU_FATHER_HOUSE = 0x162
CYAN_FOUND_POISONED_KING_DOMA = 0x031
CYAN_FOUND_POISONED_FAMILY_DOMA = 0x032
FINISHED_DOMA_WOB = 0x040 # custom
GENERAL_LEO_IMPERIAL_CAMP = 0x02b
BRIDGE_BLOCKED_IMPERIAL_CAMP = 0x02c
CHASING_KEFKA1_IMPERIAL_CAMP = 0x02d
CHASING_KEFKA2_IMPERIAL_CAMP = 0x02e
CHASING_KEFKA3_IMPERIAL_CAMP = 0x02f
FINISHED_CHASING_KEFKA_IMPERIAL_CAMP = 0x155
FINISHED_IMPERIAL_CAMP = 0x037
LUMP_CHEST_DOOR_GHOST_PHANTOM_TRAIN = 0x180 # used for both door ghost in wob and lump of metal chest in wor
GOT_PHANTOM_TRAIN_REWARD = 0x192 # custom, used to be phantom forest recovery spring
FOUND_PHANTOM_TRAIN = 0x038
STOPPED_PHANTOM_TRAIN = 0x03a
DEFEATED_PHANTOM_TRAIN = 0x03b
NAMED_GAU = 0x03f
FOUND_DIVING_HELMET = 0x041
FINISHED_SABIN_SCENARIO = 0x044
FIGHTING_KEFKA_NARSHE_WOB = 0x132
FINISHED_NARSHE_BATTLE = 0x046
RECRUITED_SHADOW_KOHLINGEN = 0x18e
CAN_LEARN_BUM_RUSH = 0x04b # custom, set when all other blitzes learned or bum rush last disabled
LEARNED_BUM_RUSH = 0x2af
GOT_SERPENT_TRENCH_REWARD = 0x050 # custom
SET_ZOZO_CLOCK = 0x51
GOT_ZOZO_REWARD = 0x052 # custom
SAW_OPERA_OVERTURE = 0x055
READY_CELES_OPERA_SCENE = 0x056
BEGAN_OPERA_DISRUPTION = 0x110
FINISHED_OPERA_PERFORMANCE = 0x111
SAW_OPERA_DUEL_SCENE = 0x2ba
OPERA_MAP_MODIFIED1 = 0x057
FOUND_ULTROS_LETTER_OPERA = 0x58
OPERA_MAP_MODIFIED2 = 0x059
OPERA_MAP_MODIFIED3 = 0x05a
FINISHED_OPERA_DISRUPTION = 0x05b # custom
SETZER_ABDUCTED_CELES = 0x05c
TOSSED_CELES_SETZER_COIN = 0x05d
DEFEATED_NINJA_CAVE_TO_SEALED_GATE = 0x075 # custom
TERRA_AGREED_TO_OPEN_SEALED_GATE = 0x076
DEFEATED_NUMBER_024 = 0x05f # custom, used to be saw kefka throw ifrit/shiva in trash
DEFEATED_IFRIT_SHIVA_MAGITEK_FACTORY = 0x060
GOT_IFRIT_SHIVA = 0x061
TALKED_TO_IFRIT_MAGITEK_FACTORY = 0x272
TALKED_TO_SHIVA_MAGITEK_FACTORY = 0x274
DISABLE_HOOK_MAGITEK_FACTORY = 0x273
RODE_MINE_CART_MAGITEK_FACTORY = 0x069
MET_SETZER_AFTER_MAGITEK_FACTORY = 0x06a # locke/celes not required in airship changing room after set
DEFEATED_CRANES = 0x06b
SAW_MADUIN_DIE = 0x070 # enables lone wolf
ESPERS_CRASHED_AIRSHIP = 0x242 # allows entry to imperial base without terra
FINISHED_GESTAHL_DINNER = 0x07d
MET_STRAGO_RELM = 0x08d
DEFEATED_FLAME_EATER = 0x090
DEFEATED_ULTROS_ESPER_MOUNTAIN = 0x095
ESPER_MOUNTAIN_GATED = 0x097 # custom, if true relm won't appear and ultros battle won't happen, previously used for statues found
ESPER_MOUNTAIN_ACCESSIBLE = 0x098
FOUND_ESPERS_ESPER_MOUNTAIN = 0x099
DEFEATED_KEFKA_THAMASA = 0x09b
LEO_BURIED_THAMASA = 0x09c
FINISHED_THAMASA_KEFKA = 0x09d
CONTINENT_IS_FLOATING = 0x09e
LEARNED_TO_FLY_AIRSHIP = 0x16f
AIRSHIP_VISIBLE = 0x1b9
AIRSHIP_FLYING = 0x246
GOT_FALCON = 0x0cd
WON_AN_AUCTION = 0x166 # custom
AUCTION_BOUGHT_ESPER1 = 0x16c # normally zoneseek
AUCTION_BOUGHT_ESPER2 = 0x16d # normally golem
WON_A_COLISEUM_MATCH = 0x1ef # custom, used to be shadow available at coliseum
BOUGHT_ESPER_TZEN = 0x27c # normally sraphim
RECRUITED_SHADOW_FLOATING_CONTINENT = 0x02a
DEFEATED_ATMAWEAPON = 0x0a1 # custom
DEFEATED_ATMA = 0x0a2 # custom
LEFT_SHADOW_FLOATING_CONTINENT = 0x0a3
IN_WOR = 0x0a4
FINISHED_FLOATING_CONTINENT = 0x0a5 # custom
STARTED_FEEDING_CID = 0x0b2 # custom, previously found cid dead
CID_SURVIVED = 0x0b3
CID_DIED = 0x0b4
FINISHED_FEEDING_CID = 0x0b9 # custom
BOARDED_CRIMSON_ROBBERS_BOAT_NIKEAH = 0x0ac
DEFEATED_TENTACLES_FIGARO = 0x0c6
LIGHT_JUDGEMENT_TZEN = 0x27d
FINISHED_COLLAPSING_HOUSE = 0x28a
HELPED_INJURED_LAD = 0x28d
DOGS_BARKED_MOBLIZ_WOR = 0x28e
MET_TERRA_WOR = 0x28f
SAW_MOBLIZ_LIGHT_OF_JUDGEMENT_SCENE = 0x290
FOUGHT_PHUNBABA1 = 0x291
GOT_FENRIR = 0x2d7
KATARIN_PREGNANT = 0x0be
CHOSE_RAGNAROK_ESPER = 0x0b5 # custom
GOT_RAGNAROK = 0x0b6
GOT_BOTH_REWARDS_WEAPON_SHOP = 0x0b7 # custom
CHASING_LONE_WOLF1 = 0x239
CHASING_LONE_WOLF7 = 0x23f
GOT_BOTH_REWARDS_LONE_WOLF = 0x241
MET_LONE_WOLF_WOR = 0x29b
RECRUITED_MOG_WOB = 0x29f
RECRUITED_UMARO_WOR = 0x07e
DARYL_TOMB_TURTLE1_MOVED = 0x2b4
DARYL_TOMB_TURTLE2_MOVED = 0x2b6
DEFEATED_DULLAHAN = 0x2b2
RUST_RID_FOR_SALE = 0x298
GOT_RUST_RID = 0x1db
FOUND_CYAN_MT_ZOZO = 0x0d1 # custom
FINISHED_MT_ZOZO = 0x0d2
DEFEATED_SR_BEHEMOTH = 0x199
FOUND_DREAM_STOOGE1 = 0x189
FOUND_DREAM_STOOGE2 = 0x18b
FOUND_INTERCEPTOR_VELDT_CAVE_WOR = 0x195
DEFEATED_CHADARNOOK = 0x253
FOUND_EBOTS_ROCK = 0x19a
MET_EBOTS_ROCK_CHEST = 0x19b
DEFEATED_HIDON = 0x19c
RECRUITED_GOGO_WOR = 0x0d4
DEFEATED_STOOGES = 0x0d8
FINISHED_DOMA_WOR = 0x0da
GOT_ALEXANDR = 0x0db
DEFEATED_MAGIMASTER = 0x2db
RECRUITED_STRAGO_FANATICS_TOWER = 0x0ba
DEFEATED_DOOM_GAZE = 0x2a1 # custom
RECRUITED_LOCKE_PHOENIX_CAVE = 0x0d7
RECRUITED_TERRA_MOBLIZ = 0x0bf
GOT_TRITOCH = 0x29e
GOT_RAIDEN = 0x2dd
FOUND_ANCIENT_CASTLE = 0x2df
GOT_ODIN = 0x0c8
SUPLEXED_TRAIN = 0x2b0 # custom, previously unused but set in nikeah entrance event

DEFEATED_NARSHE_DRAGON = 0x11a # custom
DEFEATED_MT_ZOZO_DRAGON = 0x11b # custom
DEFEATED_OPERA_HOUSE_DRAGON = 0x11c # custom
DEFEATED_KEFKA_TOWER_DRAGON_G = 0x11d # custom, gold dragon location
DEFEATED_KEFKA_TOWER_DRAGON_S = 0x11e # custom, skull dragon location
DEFEATED_ANCIENT_CASTLE_DRAGON = 0x11f # custom
DEFEATED_PHOENIX_CAVE_DRAGON = 0x120 # custom
DEFEATED_FANATICS_TOWER_DRAGON = 0x121 # custom

LEFT_WEIGHT_PUSHED_KEFKA_TOWER = 0x063
RIGHT_WEIGHT_PUSHED_KEFKA_TOWER = 0x064
WEST_PATH_BLOCKED_KEFKA_TOWER = 0x065   # path to doom in switch room
EAST_PATH_BLOCKED_KEFKA_TOWER = 0x066   # path to goddess in switch room
NORTH_PATH_OPEN_KEFKA_TOWER = 0x067     # path to guardian in switch room
SOUTH_PATH_OPEN_KEFKA_TOWER = 0x071     # path to balcony in switch room
CENTER_DOOR_KEFKA_TOWER = 0x080         # center door in weights room
LEFT_RIGHT_DOORS_KEFKA_TOWER = 0x0d0    # doors to doom/goddess opened on balcony
UNLOCKED_KT_SKIP = 0x093 # custom
UNLOCKED_FINAL_KEFKA = 0x094 # custom

SIEGFRIED_LUMP_OF_METAL_CHESTS = 0x187 # set after siegfried chest in phantom train and lump of metal chest in cyan's dream
VELDT_WORLD_MUSIC = 0x1bb
VELDT_REWARD_OBTAINED = 0x1bc # custom
DISABLE_SPRINT = 0x1c1
DISABLE_MENU_ACCESS = 0x1c2
TEMP_SONG_OVERRIDE = 0x1cc
ENABLE_Y_PARTY_SWITCHING = 0x1ce
ALWAYS_CLEAR = 0x176 # this event_bit is always clear, used for branching

for index in range(MAX_OBJECTIVES):
    globals()["OBJECTIVE" + str(index)] = 0xe0 + index

def byte(event_bit):
    return event_bit // 8

def bit(event_bit):
    return event_bit % 8

def address(event_bit):
    return 0x1e80 + byte(event_bit)

def character_recruited(char):
    # char in shops, items, gogo menu
    return 0x2e0 + char

def character_available(char):
    # char can be chosen in party select menus
    return 0x2f0 + char

def multipurpose(index):
    assert index >= 0 and index <= 15
    return 0x1a0 + index

def multipurpose_map(index):
    # cleared on map load
    assert index >= 0 and index <= 15
    return 0x1f0 + index

def multipurpose_party1_step(index):
    # cleared on each step by party1
    assert index >= 0 and index <= 3
    return 0x2c4 + index

def multipurpose_party2_step(index):
    # cleared on each step by party2
    assert index >= 0 and index <= 3
    return 0x2c8 + index

def multipurpose_party3_step(index):
    # cleared on each step by party3
    assert index >= 0 and index <= 3
    return 0x2cc + index

def objective(index):
    assert index >= 0 and index <= MAX_OBJECTIVES
    return 0xe0 + index