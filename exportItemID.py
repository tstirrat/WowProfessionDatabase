#!/usr/bin/env python3.7

items = {
    "Accurate Scope": 4407,
    "Adamantite Bar": 23446,
    "Adamantite Frame": 23784,
    "Adamantite Rod": 25844,
    "Ancient Lichen": 22790,
    "Aquamarine": 7909,
    "Arcane Dust": 22445,
    "Arcanite Bar": 12360,
    "Arcanite Rod": 16206,
    "Arthas Tears": 8836,
    "Azerothian Diamond": 12800,
    "Azure Moonstone": 23117,
    "Barbed Gill Trout": 27422,
    "Bat Flesh": 27669,
    "Bear Flank": 35562,
    "Bear Meat": 3173,
    "Big Bear Meat": 3730,
    "Big Iron Bomb": 4394,
    "Black Diamond": 11754,
    "Black Dragonscale": 15416,
    "Black Dye": 2325,
    "Black Lotus": 13468,
    "Black Mageweave Boots": 10026,
    "Black Pearl": 7971,
    "Black Whelp Scale": 7286,
    "Blackmouth Oil": 6370,
    "Blank Parchment": 10648,
    "Bleach": 2324,
    "Blindweed": 8839,
    "Blood Garnet": 23077,
    "Blood of the Mountain": 11382,
    "Bloodfin Catfish": 33823,
    "Bloodvine": 19726,
    "Blue Dragonscale": 15415,
    "Blue Dye": 6260,
    "Blue Pearl": 4611,
    "Blue Power Crystal": 11184,
    "Blue Sapphire": 12361,
    "Boar Intestines": 3172,
    "Boar Ribs": 2677,
    "Bolt of Imbued Netherweave": 21842,
    "Bolt of Linen Cloth": 2996,
    "Bolt of Mageweave": 4339,
    "Bolt of Netherweave": 21840,
    "Bolt of Runecloth": 14048,
    "Bolt of Silk Cloth": 4305,
    "Bolt of Soulcloth": 21844,
    "Bolt of Woolen Cloth": 2997,
    "Breath of Wind": 7081,
    "Briarthorn": 2450,
    "Brilliant Chromatic Scale": 12607,
    "Bronze Bar": 2841,
    "Bronze Framework": 4382,
    "Bronze Setting": 20817,
    "Bronze Tube": 4371,
    "Bruiseweed": 2453,
    "Buzzard Meat": 27671,
    "Buzzard Wing": 3404,
    "Catseye Elixir": 10592,
    "Chimera Leather": 15423,
    "Chunk o Basilisk": 27677,
    "Chunk of Boar Meat": 769,
    "Cindercloth Cloak": 14044,
    "Citrine": 3864,
    "Clam Meat": 5503,
    "Clefthoof Meat": 27678,
    "Coarse Blasting Powder": 4364,
    "Coarse Gorilla Hair": 4096,
    "Coarse Grinding Stone": 3478,
    "Coarse Stone": 2836,
    "Coarse Thread": 2320,
    "Cobra Scales": 29539,
    "Copper Bar": 2840,
    "Copper Modulator": 4363,
    "Copper Rod": 6217,
    "Copper Tube": 4361,
    "Core Leather": 17012,
    "Core of Earth": 7075,
    "Coyote Meat": 2673,
    "Crag Boar Rib": 2886,
    "Crawler Claw": 2675,
    "Crawler Meat": 2674,
    "Crescent-Tail Skullfish": 33824,
    "Crimson Spinel": 32227,
    "Crisp Spider Meat": 1081,
    "Crocolisk Meat": 2924,
    "Crunchy Spider Leg": 22644,
    "Crystal Infused Leather": 25699,
    "Crystal Vial": 8925,
    "Cured Heavy Hide": 4236,
    "Cured Light Hide": 4231,
    "Cured Medium Hide": 4233,
    "Cured Rugged Hide": 19047,
    "Cured Thick Hide": 8172,
    "Dark Iron Bar": 11371,
    "Dark Rune": 20520,
    "Darkclaw Lobster": 13888,
    "Dawnstone": 23440,
    "Deadly Scope": 10546,
    "Deep Peridot": 23079,
    "Deeprock Salt": 8150,
    "Delicate Arcanite Converter": 16006,
    "Delicate Copper Wire": 20816,
    "Dense Blasting Powder": 15992,
    "Dense Grinding Stone": 12644,
    "Dense Stone": 12365,
    "Deviate Fish": 6522,
    "Deviate Scale": 6470,
    "Devilsaur Leather": 15417,
    "Dig Rat": 5051,
    "Discolored Worg Heart": 3164,
    "Dream Dust": 11176,
    "Dreamfoil": 13463,
    "Dreaming Glory": 22786,
    "Dreamscale": 20381,
    "Dusky Belt": 7387,
    "Earthroot": 2449,
    "Earthstorm Diamond": 25867,
    "Elemental Air": 7069,
    "Elemental Blasting Powder": 23781,
    "Elemental Earth": 7067,
    "Elemental Fire": 7068,
    "Elemental Water": 7070,
    "Elixir of Agility": 8949,
    "Elixir of Defense": 3389,
    "Elixir of Demonslaying": 9224,
    "Elixir of Greater Defense": 8951,
    "Elixir of Lesser Agility": 3390,
    "Elixir of Major Agility": 22831,
    "Elixir of Major Strength": 22824,
    "Elixir of Minor Agility": 2457,
    "Elixir of Ogres Strength": 3391,
    "Elixir of Wisdom": 3383,
    "Empty Vial": 3371,
    "Empyrean Sapphire": 32228,
    "Enchanted Leather": 12810,
    "Enchanted Thorium Bar": 12655,
    "Engineers Ink": 10647,
    "Enormous Barbed Gill Trout": 27516,
    "Essence of Air": 7082,
    "Essence of Earth": 7076,
    "Essence of Fire": 7078,
    "Essence of Undeath": 12808,
    "Essence of Water": 7080,
    "Eternium Bar": 23447,
    "Eternium Ore": 23427,
    "Eternium Rod": 25745,
    "Fadeleaf": 3818,
    "Fel Hide": 25707,
    "Fel Iron Bar": 23445,
    "Fel Iron Casing": 23782,
    "Fel Iron Rod": 25843,
    "Fel Scales": 25700,
    "Felcloth": 14256,
    "Felsteel Bar": 23448,
    "Felsteel Stabilizer": 23787,
    "Felweed": 22785,
    "Fiery Core": 17010,
    "Figluster Midfish": 27435,
    "Fine Leather Belt": 4246,
    "Fine Leather Gloves": 2312,
    "Fine Leather Tunic": 4243,
    "Fine Thread": 2321,
    "Fire Goggles": 10500,
    "Fire Oil": 6371,
    "Firebloom": 4625,
    "Firefin Snapper": 6359,
    "Flagon of Dwarven Honeymead": 2594,
    "Flame Spessarite": 21929,
    "Flask of Big Mojo": 8152,
    "Flask of Mojo": 8151,
    "Flask of Oil": 814,
    "Flask of Stormwind Tawny": 2593,
    "Flying Tiger Goggles": 4368,
    "Frost Oil": 3829,
    "Frostsaber Leather": 15422,
    "Frozen Rune": 22682,
    "Furious Crawdad": 27439,
    "Fused Wiring": 7191,
    "Giant Clam Meat": 4655,
    "Giant Egg": 12207,
    "Ghost Dye": 9210,
    "Ghost Mushroom": 8845,
    "Globe of Water": 7079,
    "Goblin Construction Helmet": 10543,
    "Goblin Rocket Fuel": 9061,
    "Gold Bar": 3577,
    "Gold Power Core": 10558,
    "Golden Darter": 27438,
    "Golden Draenite": 23112,
    "Golden Pearl": 13926,
    "Golden Rod": 11128,
    "Golden Sansam": 13464,
    "Goldenbark Apple": 4539,
    "Goldthorn": 3821,
    "Gooey Spider Leg": 2251,
    "Goretusk Liver": 723,
    "Goretusk Snout": 731,
    "Grave Moss": 3369,
    "Gray Dye": 4340,
    "Great Rage Potion": 5633,
    "Greater Astral Essence": 11082,
    "Greater Eternal Essence": 16203,
    "Greater Magic Essence": 10939,
    "Greater Mana Potion": 6149,
    "Greater Mystic Essence": 11135,
    "Greater Nether Essence": 11175,
    "Greater Planar Essence": 22446,
    "Green Dragonscale": 15412,
    "Green Dye": 2605,
    "Green Leather Armor": 4255,
    "Green Power Crystal": 11185,
    "Green Tinted Googles": 4385,
    "Green Whelp Scale": 7392,
    "Gromsblood": 8846,
    "Guardian Gloves": 5966,
    "Guardian Stone": 12809,
    "Gyrochronatom": 4389,
    "Handful of Copper Bolts": 4359,
    "Handful of Fel Iron Bolts": 23783,
    "Hardened Adamantite Bar": 23573,
    "Hardened Adamantite Tube": 23785,
    "Healing Potion": 929,
    "Heart of Fire": 7077,
    "Heart of the Wild": 10286,
    "Heavy Blasting Powder": 4377,
    "Heavy Grinding Stone": 3486,
    "Heavy Hide": 4235,
    "Heavy Knothide Leather": 23793,
    "Heavy Kodo Meat": 12204,
    "Heavy Leather": 4234,
    "Heavy Scorpid Scale": 15408,
    "Heavy Silithid Carapace": 20501,
    "Heavy Silken Thread": 8343,
    "Heavy Stock": 4400,
    "Heavy Stone": 2838,
    "Holiday Spices": 17194,
    "Holiday Spirits": 17196,
    "Hot Spices": 2692,
    "Huge Emerald": 12364,
    "Huge Spotted Feltail": 27515,
    "Ice Cold Milk": 1179,
    "Icecap": 13467,
    "Icefin Bluefish": 27437,
    "Ichor of Undeath": 7972,
    "Icy Blasting Primers": 32423,
    "Illusion Dust": 16204,
    "Imbued Vial": 18256,
    "Inlaid Mithril Cylinder": 9060,
    "Iridescent Pearl": 5500,
    "Iron Bar": 3575,
    "Iron Buckle": 7071,
    "Iron Ore": 2772,
    "Iron Strut": 4387,
    "Ironfeather": 15420,
    "Ironweb Spider Silk": 14227,
    "Jade": 1529,
    "Jaggal Clam Meat": 24477,
    "Jaggal Pearl": 24478,
    "Jet Black Feather": 8168,
    "Khadgars Whisker": 3358,
    "Khorium Bar": 23449,
    "Khorium Power Core": 23786,
    "Kingsblood": 3356,
    "Knothide Leather": 21887,
    "Kodo Meat": 5467,
    "Large Brilliant Shard": 14344,
    "Large Fang": 5637,
    "Large Glimmering Shard": 11084,
    "Large Glowing Shard": 11139,
    "Large Obsidian Shard": 22203,
    "Large Opal": 12799,
    "Large Prismatic Shard": 22449,
    "Large Radiant Shard": 11178,
    "Large Raw Mightfish":  13893,
    "Large Venom Sac": 1288,
    "Larval Acid": 18512,
    "Lava Core": 17011,
    "Leaded Vial": 3372,
    "Lean Wolf Flank": 1015,
    "Lesser Astral Essence": 10998,
    "Lesser Eternal Essence": 16202,
    "Lesser Invisibility Potion": 3823,
    "Lesser Magic Essence": 10938,
    "Lesser Moonstone": 1705,
    "Lesser Mystic Essence": 11134,
    "Lesser Nether Essence": 11174,
    "Lesser Planar Essence": 22447,
    "Liferoot": 3357,
    "Light Hide": 783,
    "Light Leather": 2318,
    "Light Silithid Carapace": 20500,
    "Lightning Eel": 13757,
    "Linen Cloth": 2589,
    "Lion Meat": 3731,
    "Living Essence": 12803,
    "Living Ruby": 23436,
    "Long Elegant Feather": 4589,
    "Long Tail Feather": 5116,
    "Lucky Charm": 5373,
    "Lynx Meat": 27668,
    "Mageroyal": 785,
    "Mageweave Cloth": 4338,
    "Major Healing Potion": 13446,
    "Major Mana Potion": 13444,
    "Malachite": 774,
    "Mana Potion": 3827,
    "Mana Thistle": 22793,
    "Maple Seed": 17034,
    "Meaty Bat Wing": 12223,
    "Medium Hide": 4232,
    "Medium Leather": 2319,
    "Mercurial Adamantite": 31079,
    "Mild Spices": 2678,
    "Minor Healing Potion": 118,
    "Mithril Bar": 3860,
    "Mithril Casing": 10561,
    "Mithril Filigree": 20963,
    "Mithril Ore": 3858,
    "Mithril Tube": 10559,
    "Mooncloth": 14342,
    "Moongraze Stag Tenderloin": 23676,
    "Morrowgrain": 11040,
    "Moss Agate": 1206,
    "Mote of Air": 22572,
    "Mote of Earth": 22573,
    "Mote of Fire": 22574,
    "Mote of Water": 22578,
    "Mountain Silversage": 13465,
    "Murloc Eye": 730,
    "Murloc Fin": 1468,
    "Mystery Meat": 12037,
    "Naga Scale": 7072,
    "Nether Dragonscale": 29548,
    "Netherbloom": 22791,
    "Netherweave Cloth": 21877,
    "Netherweb Spider Silk": 21881,
    "Nexus Crystal": 20725,
    "Nightcrawlers": 6530,
    "Nightmare Vine": 22792,
    "Nightseye": 23441,
    "Oily Blackmouth": 6358,
    "Orange Dye": 6261,
    "Peacebloom": 2447,
    "Perfect Deviate Scale": 6471,
    "Pink Dye": 10290,
    "Plaguebloom": 13466,
    "Powerful Mojo": 12804,
    "Primal Air": 22451,
    "Primal Bat Leather": 19767,
    "Primal Earth": 22452,
    "Primal Fire": 21884,
    "Primal Life": 21886,
    "Primal Mana": 22457,
    "Primal Might": 23571,
    "Primal Shadow": 22456,
    "Primal Tiger Leather": 19768,
    "Primal Water": 21885,
    "Pristine Black Diamond": 18335,
    "Purple Dye": 4342,
    "Purple Lotus": 8831,
    "Ragveil": 22787,
    "Raptor Egg": 3685,
    "Raptor Flesh": 12184,
    "Raptor Hide": 4461,
    "Raptor Ribs": 31670,
    "Ravager Flesh": 27674,
    "Raw Brilliant Smallfish": 6291,
    "Raw Bristle Whisker Catfish": 6308,
    "Raw Glossy Mightfish": 13754,
    "Raw Greater Sagefish": 21153,
    "Raw Loch Frenzy": 6317,
    "Raw Longjaw Mud Snapper": 6289,
    "Raw Mithril Head Trout": 8365,
    "Raw Nightfin Snapper": 13759,
    "Raw Rainbow Fin Albacore": 6361,
    "Raw Redgill": 13758,
    "Raw Rockscale Cod": 6362,
    "Raw Sagefish": 21071,
    "Raw Slitherskin Mackerel": 6303,
    "Raw Spotted Yellowtail": 4603,
    "Raw Summer Bass": 13756,
    "Raw Sunscale Salmon": 13760,
    "Raw Whitescale Salmon": 13889,
    "Red Dragonscale": 15414,
    "Red Dye": 2604,
    "Red Power Crystal": 11186,
    "Red Whelp Scale": 7287,
    "Red Wolf Meat": 12203,
    "Refined Deeprock Salt": 15409,
    "Refreshing Spring Water": 159,
    "Rhapsody Malt": 2894,
    "Righteous Orb": 12811,
    "Rough Blasting Powder": 4357,
    "Rough Grinding Stone": 3470,
    "Rough Stone": 2835,
    "Rugged Hide": 8171,
    "Rugged Leather": 8170,
    "Ruined Leather Scraps": 2934,
    "Rune Thread":14341,
    "Runecloth": 14047,
    "Runn Tum Tuber": 18255,
    "Salt": 4289,
    "Sandworm Meat": 20424,
    "Scale of Onyxia": 15410,
    "Scorpid Scale": 8154,
    "Scorpid Stinger": 5466,
    "Scroll of Strength V": 27503,
    "Seaspray Emerald": 32249,
    "Serpent Flesh": 31671,
    "Shadow Oil": 3824,
    "Shadow Pearl": 24479,
    "Shadow Protection Potion": 6048,
    "Shadow Silk": 10258,
    "Shadowcat Hide": 7428,
    "Shadowgem": 1210,
    "Sharp Claw": 5635,
    "Shiny Red Apple": 4536,
    "Silithid Chitin": 20498,
    "Silk Cloth": 4306,
    "Silken Thread": 4291,
    "Silver Bar": 2842,
    "Silver Contact": 4404,
    "Silver Rod": 6338,
    "Silverleaf": 765,
    "Simple Flour": 30817,
    "Simple Wood": 4470,
    "Skin of Dwarven Stout": 2596,
    "Skyfire Diamond": 25868,
    "Slimy Murloc Scale": 5784,
    "Small Brilliant Shard": 14343,
    "Small Egg": 6889,
    "Small Flame Sac": 4402,
    "Small Glimmering Shard": 10978,
    "Small Glowing Shard": 11138,
    "Small Lustrous Pearl": 5498,
    "Small Obsidian Shard": 22202,
    "Small Prismatic Shard": 22448,
    "Small Spider Leg": 5465,
    "Small Radiant Shard": 11177,
    "Snowball": 17202,
    "Soft Frenzy Fish": 5468,
    "Solid Blasting Powder": 10505,
    "Solid Dynamite": 10507,
    "Solid Grinding Stone": 7966,
    "Solid Stone": 7912,
    "Soothing Spices": 3713,
    "Soul Dust": 11083,
    "Souldarite": 19774,
    "Sparkling Apple Cider": 34412,
    "Spellpower Goggles Xtreme": 10502,
    "Spider Ichor": 3174,
    "Spiders Silk": 3182,
    "Spotted Feltail": 27425,
    "Stag Meat": 5471,
    "Star of Elune": 23438,
    "Star Ruby": 7910,
    "Star Wood": 11291,
    "Steel Bar": 3859,
    "Stonescale Eel": 13422,
    "Stonescale Oil": 13423,
    "Stormwind Seasoning Herbs": 2665,
    "Strange Dust": 10940,
    "Strange Spores": 27676,
    "Stranglekelp": 3820,
    "Stranglethorn Seed": 17035,
    "Strider Meat": 5469,
    "Stringy Vulture Meat": 729,
    "Stringy Wolf Meat": 2672,
    "Strong Flux": 3466,
    "Sungrass": 8838,
    "Swiftness Potion": 2459,
    "Swiftthistle": 2452,
    "Talasite": 23437,
    "Talbuk Venison": 27682,
    "Tangy Clam Meat": 5504,
    "Tender Crab Meat": 12206,
    "Tender Crocolisk Meat": 3667,
    "Tender Wolf Meat": 12208,
    "Terocone": 22789,
    "The Big One": 10586,
    "Thick Clefthoof Leather": 25708,
    "Thick Hide": 8169,
    "Thick Leather": 4304,
    "Thick Murloc Scale": 5785,
    "Thick Spiders Silk": 4337,
    "Thick Wolfhide": 8368,
    "Thin Kodo Leather": 8368,
    "Thorium Bar": 12359,
    "Thorium Ore": 10620,
    "Thorium Setting": 21752,
    "Thorium Tube": 16000,
    "Thorium Widget": 15994,
    "Thunder Lizard Tail": 5470,
    "Tiger Meat": 12202,
    "Tigerseye": 818,
    "Tough Condor Meat": 1080,
    "Truesilver Bar": 6037,
    "Truesilver Rod": 11144,
    "Truesilver Transformer": 18631,
    "Turtle Meat": 3712,
    "Turtle Scale": 8167,
    "Unstable Trigger": 10560,
    "Vision Dust": 11137,
    "Void Crystal": 22450,
    "Volatile Rum": 9260,
    "Warbear Leather": 15419,
    "Warped Flesh": 27681,
    "Weak Flux": 2880,
    "Whirring Bronze Gizmo": 4375,
    "White Spider Meat": 12205,
    "Wicked Claw": 8146,
    "Wild Steelbloom": 3355,
    "Wildvine": 8153,
    "Wind Scales": 29547,
    "Winter Squid": 13755,
    "Wintersbite": 3819,
    "Wooden Stock": 4399,
    "Wool Cloth": 2592,
    "Worn Dragonscale": 8165,
    "Yellow Dye": 4341,
    "Yellow Power Crystal": 11188,
    "Zangarian Sporefish": 27429,
    "Zesty Clam Meat": 7974
}

import json

with open("itemID.json", 'w') as jsonFile:
    json.dump(items, jsonFile)