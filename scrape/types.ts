enum Quality {
  JUNK = 0,
  COMMON = 1,
  UNCOMMON = 2,
  RARE = 3,
  EPIC = 4,
  LEGENDARY = 5,
}

enum Standing {
  NEUTRAL = 3,
  FRIENDLY = 4,
  HONORED = 5,
  REVERED = 6,
  EXALTED = 7,
}

export type FactionId = Id<"FactionId">;

export interface WHItem {
  readonly name_enus: string;
  readonly quality: Quality;
  readonly icon: string;
  readonly screenshot: unknown;
  readonly jsonequip: {
    reqfaction?: FactionId;
    reqrep?: Standing;
    [key: string]: any;
  };
  readonly attainable: number;
  readonly flags2: number;
}

export type ItemId = Id<"ItemId">;
export interface WHItemMap {
  [id: string]: WHItem;
}

export type SourceString =
  | "Trainer"
  | "Drop"
  | "Quest"
  | "Vendor"
  | "VendorLimited"
  | "Seasonal"
  | "Fished";

type Id<I, T = number> = T & { __dont_set_this?: I };

type Colors = [number, number, number, number];
type Creates = [number, number, number];
type SkillId = Id<"SkillId">;
type SpecializationId = Id<"SpecializationId">;
type SpellId = Id<"SpellId">;
type Ingredient = [ItemId, number];

enum Source {
  DROP = 2,
  VENDOR = 5,
  TRAINER = 6,
  FISHED = 16,
  PICKPOCKETED = 21,
}

type SourceId = 2 | 5 | 6 | 16 | 21;

export interface WHSpell {
  readonly id: SpellId;
  readonly cat: number;
  readonly colors?: Colors;
  readonly creates?: Creates;
  readonly learnedat: number;
  readonly level: number;
  readonly name: string;
  readonly rank?: string;
  readonly nskillup: number;
  readonly quality: Quality;
  readonly reagents?: readonly Ingredient[];
  readonly schools: number;
  readonly skill: SkillId[];
  readonly source?: SourceId[];
  readonly trainingcost?: number;
  readonly popularity: number;
  readonly specialization?: SpecializationId;
}

export type Output = { [name: string]: Spell };

export interface Spell {
  readonly ID: SpellId;
  readonly Creates: ItemId;
  readonly Learn: number;
  readonly Yellow: number;
  readonly Green: number;
  readonly Grey: number;
  readonly Source: SourceString;
  readonly RecipeID?: ItemId;
  readonly Reagents: ReagentMap;
  readonly Phase: 1;
}

type ReagentMap = { [name: string]: number };

export function toSpell(s: WHSpell, items: Map<ItemId, WHItem>): Spell {
  const [, Yellow, Green, Grey] = s.colors!;

  const reagentsEntries = s.reagents
    ? s.reagents.map(([itemId, count]) => {
        const item = items.get(itemId);
        if (item) {
          return [item.name_enus, count];
        }
        return null;
      })
    : [];

  const Reagents = Object.fromEntries(
    reagentsEntries.filter((r): r is [string, number] => r !== null)
  );

  const Source = toSourceString(minSourceId(s.source));

  return {
    ID: s.id,
    Creates: s.creates ? s.creates[0] : undefined,
    Learn: s.learnedat,
    Phase: 1,
    Reagents,
    Yellow,
    Green,
    Grey,
    RecipeID: Source !== "Trainer" ? 1 : undefined,
    Source,
  };
}

export function toSourceString(source: Source): SourceString {
  switch (source) {
    case Source.TRAINER:
      return "Trainer";
    case Source.VENDOR:
      return "Vendor";
    case Source.DROP:
    case Source.FISHED:
    case Source.PICKPOCKETED:
      return "Drop";
    default:
      return assertNever(source);
  }
}

export function minSourceId(sources?: readonly Source[]): Source {
  if (!sources) return Source.TRAINER;
  if (sources.includes(Source.TRAINER)) return Source.TRAINER;
  if (sources.includes(Source.VENDOR)) return Source.VENDOR;
  return Source.DROP;
}

function assertNever(v: never): never {
  throw new Error(`AssertNever: ${v}`);
}
