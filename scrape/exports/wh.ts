import { WHItemMap } from "../types";

enum Type {
  RECIPES = 3,
  ITEMS = 6,
  ICONS = 8,
}

class GathererImpl {
  public itemMap: WHItemMap | undefined;

  addData(type: Type.ITEMS | Type.RECIPES, _: number, items: WHItemMap): void;
  addData(type: Type.ICONS, _: number, items: {}): void;
  addData(type: Type, _: number, items: any) {
    if (type === Type.ITEMS || type === Type.RECIPES) {
      this.itemMap = items;
    }
  }

  get items(): WHItemMap {
    return this.itemMap!;
  }
}

export const Gatherer = new GathererImpl();

export class Listview {
  constructor(config: unknown) {}
}

export const Page = { Items: { parentItemFilter: "blah" } };

export const Filter = { listview_addUpgradeIndicator: "blah" };
