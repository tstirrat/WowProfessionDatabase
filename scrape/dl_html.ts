import { Profession, Slug, url } from "./types.ts";

// force this to be a module
export {};

async function getHtml(slug: Slug, id: string) {
  const html = (await fetch(url(slug, id))).text();
  return html;
}

try {
  for (const prof of Object.values(Profession)) {
    const html = await getHtml(Slug.SPELLS, prof);
    await Deno.writeTextFile(`./html/${prof}.html`, html);
    console.log(`Wrote ${prof}.html`);
  }
  for (const prof of Object.values(Profession)) {
    const html = await getHtml(Slug.RECIPES, prof);
    await Deno.writeTextFile(`./html/${prof}_recipes.html`, html);
    console.log(`Wrote ${prof}_recipes.html`);
  }
} catch (e) {
  console.error(e);
}
