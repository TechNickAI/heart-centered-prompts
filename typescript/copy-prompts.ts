import { cpSync, existsSync, mkdirSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const source = join(__dirname, "..", "prompts");
const dest = join(__dirname, "prompts");

if (!existsSync(dest)) {
  mkdirSync(dest, { recursive: true });
}

cpSync(source, dest, { recursive: true });
console.log("Prompts copied successfully");
