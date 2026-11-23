// news-image-20261123 — "The World in One Day", Monday 23 November 2026.
// The entry is a pre-drawn newspaper front page (entry.png, 1024x1024,
// drawn fresh with PIL in the build session). This program only copies it
// to the grader's output directory. Node 22, standard library only.
import { copyFileSync, existsSync, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "entry.png");
if (!existsSync(source)) {
  throw new Error(`entry.png not found next to main.ts: ${source}`);
}
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
const dest = join(outDir, "entry.png");
copyFileSync(source, dest);
console.log(`wrote ${dest} (${statSync(dest).size} bytes)`);
