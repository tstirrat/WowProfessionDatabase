import * as alchemy from "./exports/alchemy";
import * as bs from "./exports/blacksmithing";
import * as cook from "./exports/cooking";
import * as ench from "./exports/enchanting";
import * as eng from "./exports/engineering";
import * as ins from "./exports/inscription";
import * as jc from "./exports/jewelcrafting";
import * as lw from "./exports/leatherworking";
import * as mining from "./exports/mining";
import * as tail from "./exports/tailoring";
import {
  ItemId,
  WHItem,
  WHItemMap,
  WHSpell,
  Spell,
  toSpell,
  stripRecipePrefix,
  WHItemWithID,
} from "./types";

await Promise.all([
  writeJSON(
    toSpells(alchemy.spells, alchemy.items, alchemy.recipes),
    "../alchemy.json"
  ),
  writeJSON(toSpells(bs.spells, bs.items, bs.recipes), "../blacksmithing.json"),
  writeJSON(toSpells(cook.spells, cook.items, cook.recipes), "../cooking.json"),
  writeJSON(
    toSpells(ench.spells, ench.items, ench.recipes),
    "../enchanting.json"
  ),
  writeJSON(
    toSpells(eng.spells, eng.items, eng.recipes),
    "../engineering.json"
  ),
  writeJSON(
    toSpells(ins.spells, ins.items, ins.recipes),
    "../inscription.json"
  ),
  writeJSON(toSpells(jc.spells, jc.items, jc.recipes), "../jewelcrafting.json"),
  writeJSON(
    toSpells(lw.spells, lw.items, lw.recipes),
    "../leatherworking.json"
  ),
  writeJSON(toSpells(mining.spells, mining.items), "../mining.json"),
  writeJSON(
    toSpells(tail.spells, tail.items, tail.recipes),
    "../tailoring.json"
  ),
]);

const items = new Map<ItemId, string>();

collectItems(items, alchemy.spells, alchemy.items);
collectItems(items, bs.spells, bs.items);
collectItems(items, ench.spells, ench.items);
collectItems(items, eng.spells, eng.items);
collectItems(items, ins.spells, ins.items);
collectItems(items, jc.spells, jc.items);
collectItems(items, lw.spells, lw.items);
collectItems(items, mining.spells, mining.items);
collectItems(items, tail.spells, tail.items);

const swappedEntries = [...items.entries()].map(([itemId, name]) => [
  name,
  itemId,
]);

await writeJSON(Object.fromEntries(swappedEntries), "../itemID.json");

function toSpells(
  spells: readonly WHSpell[],
  materialMap: WHItemMap,
  recipeMap: WHItemMap = {}
) {
  const mats = new Map<ItemId, WHItem>(
    Object.entries<WHItem>(materialMap).map<[ItemId, WHItem]>(([id, item]) => [
      parseInt(id),
      item,
    ])
  );

  const recipes = new Map<string, WHItemWithID>(
    Object.entries<WHItem>(recipeMap).map<[string, WHItemWithID]>(
      ([id, recipe]) => [
        stripRecipePrefix(recipe.name_enus),
        { ...recipe, id: parseInt(id) },
      ]
    )
  );

  const spellEntries = spells
    .filter((s) => s.colors)
    .map<[string, Spell]>((s) => {
      const spell = toSpell(s, mats, recipes);
      return [s.name, spell];
    });

  return Object.fromEntries(spellEntries);
}

function collectItems(
  outputItems: Map<ItemId, string>,
  spells: readonly WHSpell[],
  itemMap: WHItemMap
) {
  const items = new Map<ItemId, WHItem>(
    Object.entries<WHItem>(itemMap).map<[ItemId, WHItem]>(([id, item]) => [
      parseInt(id, 10),
      item,
    ])
  );

  const usedItems = spells.flatMap((s) => s.reagents || []);

  usedItems.forEach(([itemId]) => {
    const item = items.get(itemId);
    if (item) {
      outputItems.set(itemId, item.name_enus);
    }
  });
}

async function writeJSON(output: any, filename: string) {
  await Bun.write(filename, JSON.stringify(output, null, 2));
}
