import { WHItemMap } from "../types";

enum Type {
  ITEMS = 6,
  ICONS = 8,
}

class GathererImpl {
  public items: WHItemMap;

  addData(type: Type.ICONS, _: number, items: {});
  addData(type: Type.ITEMS, _: number, items: WHItemMap);
  addData(type: Type, _: number, items: any) {
    if (type === Type.ITEMS) {
      this.items = items;
    }
  }
}

export const Gatherer = new GathererImpl();

export class Listview {
  constructor(config: unknown) {}
}
