import { WHItemMap, WHListViewItem } from "../types";

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

interface ListViewParams {
  readonly template: string;
  readonly id: string;
  readonly note: string;
  readonly extraCols: string[];
  readonly sort: string[];
  readonly maxPopularity: number;
  readonly onAfterCreate: string;
  readonly visibleCols: string[];
  readonly hiddenCols: string[];
  readonly customFilter: string;
  readonly data: readonly WHListViewItem[];
}

export class Listview {
  constructor({ data }: ListViewParams) {
    for (const item of data) {
      if (item.sourcemore) {
        const items = Gatherer.items;
        items[item.id].sourcemore = item.sourcemore;
      }
    }
  }
}

export const Page = { Items: { parentItemFilter: "blah" } };

export const Filter = { listview_addUpgradeIndicator: "blah" };
