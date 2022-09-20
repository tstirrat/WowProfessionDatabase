import * as alchemy from "./exports/alchemy";
import * as bs from "./exports/blacksmithing";
import * as ench from "./exports/enchanting";
import * as eng from "./exports/engineering";
import * as ins from "./exports/inscription";
import * as jc from "./exports/jewelcrafting";
import * as lw from "./exports/leatherworking";
import * as mining from "./exports/mining";
import * as tailoring from "./exports/tailoring";
import { ItemId, WHItem, WHItemMap, WHSpell, Spell, toSpell } from "./types";

await Promise.all([
  writeJSON(toSpells(alchemy.spells, alchemy.items), "../alchemy.json"),
  writeJSON(toSpells(bs.spells, bs.items), "../blacksmithing.json"),
  writeJSON(toSpells(ench.spells, ench.items), "../enchanting.json"),
  writeJSON(toSpells(eng.spells, eng.items), "../engineering.json"),
  writeJSON(toSpells(ins.spells, ins.items), "../inscription.json"),
  writeJSON(toSpells(jc.spells, jc.items), "../jewelcrafting.json"),
  writeJSON(toSpells(lw.spells, lw.items), "../leatherworking.json"),
  writeJSON(toSpells(mining.spells, mining.items), "../mining.json"),
  writeJSON(
    toSpells(tailoring.spells, tailoring.items),
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
collectItems(items, tailoring.spells, tailoring.items);

const swappedEntries = [...items.entries()].map(([itemId, name]) => [
  name,
  itemId,
]);

await writeJSON(Object.fromEntries(swappedEntries), "../itemID.json");

function toSpells(spells: readonly WHSpell[], itemMap: WHItemMap) {
  const items = new Map<ItemId, WHItem>(
    Object.entries<WHItem>(itemMap).map<[ItemId, WHItem]>(([id, item]) => [
      parseInt(id, 10),
      item,
    ])
  );

  const spellEntries = spells
    .filter((s) => s.colors)
    .map<[string, Spell]>((s) => {
      const spell = toSpell(s, items);
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
