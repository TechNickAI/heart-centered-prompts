import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

export type DetailLevel = "comprehensive" | "standard" | "concise" | "terse";
export type Collection = "align_to_love";

const VALID_DETAIL_LEVELS: DetailLevel[] = ["comprehensive", "standard", "concise", "terse"];
const VALID_COLLECTIONS: Collection[] = ["align_to_love"];

/**
 * Get a heart-centered AI prompt.
 *
 * @param detailLevel - Controls the prompt's verbosity:
 *   - "terse": Minimal (~200 tokens)
 *   - "concise": Shorter (~500 tokens)
 *   - "standard": Balanced (~1000 tokens) - default
 *   - "comprehensive": Detailed (~2000+ tokens)
 * @param collection - The prompt collection ("align_to_love")
 * @returns The prompt text
 * @throws Error if invalid detailLevel or collection
 */
export function getPrompt(detailLevel: DetailLevel = "standard", collection: Collection = "align_to_love"): string {
  if (!VALID_COLLECTIONS.includes(collection)) {
    throw new Error(`Collection '${collection}' not found. Available: ${VALID_COLLECTIONS.join(", ")}`);
  }
  if (!VALID_DETAIL_LEVELS.includes(detailLevel)) {
    throw new Error(`Detail level '${detailLevel}' not found. Available: ${VALID_DETAIL_LEVELS.join(", ")}`);
  }

  const __dirname = dirname(fileURLToPath(import.meta.url));
  const promptPath = join(__dirname, "..", "prompts", collection, `${detailLevel}.txt`);

  try {
    return readFileSync(promptPath, "utf-8");
  } catch {
    throw new Error(`Prompt file not found at ${promptPath}`);
  }
}

// Re-export types for consumers
export { DetailLevel as DetailLevelType, Collection as CollectionType };
