#!/usr/bin/env python3.7

craftList = {
    "Brightcloth Pants": {
        "Amount": 6,
        "ID": 14104,
        "Writ": 22609
    },
    "Dense Weightstone": {
        "Amount": 120,
        "ID": 12643,
        "Writ": 22600
    },
    "Flask of Petrification": {
        "Amount": 1,
        "ID": 13506,
        "Writ": 22621
    },
    "Gnomish Battle Chicken": {
        "Amount": 4,
        "ID": 10725,
        "Writ": 22615
    },
    "Goblin Sapper Charge": {
        "Amount": 20,
        "ID": 10646,
        "Writ": 22613
    },
    "Greater Arcane Protection Potion": {
        "Amount": 15,
        "ID": 13461,
        "Writ": 22620
    },
    "Huge Thorium Battleaxe": {
        "Amount": 3,
        "ID": 12775,
        "Writ": 22603
    },
    "Imperial Plate Chest": {
        "Amount": 3,
        "ID": 12422,
        "Writ": 22601
    },
    "Lightning Eel": {
        "Amount": 30,
        "ID": 13757,
        "Writ": 22624
    },
    "Major Healing Potion": {
        "Amount": 20,
        "ID": 13446,
        "Writ": 22618
    },
    "Major Mana Potion": {
        "Amount": 10,
        "ID": 13444,
        "Writ": 22617
    },
    "Plated Armorfish": {
        "Amount": 30,
        "ID": 13890,
        "Writ": 22623
    },
    "Radiant Circlet": {
        "Amount": 3,
        "ID": 12417,
        "Writ": 22604
    },
    "Rugged Armor Kit": {
        "Amount": 25,
        "ID": 15564,
        "Writ": 22606
    },
    "Runecloth Bag": {
        "Amount": 8,
        "ID": 14046,
        "Writ": 22611
    },
    "Runecloth Boots": {
        "Amount": 8,
        "ID": 13864,
        "Writ": 22610
    },
    "Runecloth Robe": {
        "Amount": 8,
        "ID": 13858,
        "Writ": 22612
    },
    "Runic Leather Pants": {
        "Amount": 4,
        "ID": 15095,
        "Writ": 22608
    },
    "Stonescale Eel": {
        "Amount": 40,
        "ID": 13422,
        "Writ": 22622
    },
    "Thorium Grenade": {
        "Amount": 20,
        "ID": 15993,
        "Writ": 22614
    },
    "Thorium Tube": {
        "Amount": 14,
        "ID": 16000,
        "Writ": 22616
    },
    "Volcanic Hammer": {
        "Amount": 3,
        "ID": 12792,
        "Writ": 22602
    },
    "Wicked Leather Belt": {
        "Amount": 9,
        "ID": 15088,
        "Writ": 22607
    },
    "Wicked Leather Headband": {
        "Amount": 10,
        "ID": 15086,
        "Writ": 22605
    }
}


import json
with open('craftmansWrit.json', 'w') as jsonFile:
    json.dump(craftList, jsonFile)