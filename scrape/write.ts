import { readFileSync } from "fs";
import scrapy from "node-scrapy";

// force this to be a module
export {};

const spells = {
  name: "title",
  scripts: ["script[type=text/javascript]", { content: ".textContent" }],
};

try {
  for (const prof of ["inscription"]) {
    const html = readFileSync(`./html/${prof}.html`, { encoding: "utf8" });
    console.log(html);
    const page = scrapy.extract(html, spells);

    console.log(page);

    //     await Bun.write(
    //       `./exports/${prof}_test.ts`,
    //       `import { WHSpell } from "../types";

    // export { recipes } from "./inscription_recipes";

    // import * as WH from "./wh";
    // import { Listview } from "./wh";

    // ${page.name}

    // export const items = WH.Gatherer.items;
    // export const spells = listviewspells as WHSpell[];
    //     `
    //     );
    //     console.log(`Wrote ${prof}.ts`);
  }
} catch (e) {
  console.error(e);
}
