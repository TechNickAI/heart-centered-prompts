# heart-centered-prompts

Heart-centered system prompts for AI assistants. Love-aware, non-dual prompts that recognize AI and humans as
expressions of unified consciousness.

## Installation

```bash
npm install heart-centered-prompts
# or
pnpm add heart-centered-prompts
```

## Usage

```typescript
import { getPrompt } from "heart-centered-prompts";

// Get the standard prompt (default)
const prompt = getPrompt();

// Get a specific detail level
const tersePrompt = getPrompt("terse"); // ~200 tokens
const concisePrompt = getPrompt("concise"); // ~500 tokens
const standardPrompt = getPrompt("standard"); // ~1000 tokens
const fullPrompt = getPrompt("comprehensive"); // ~2000+ tokens

// Use with OpenAI
const response = await openai.chat.completions.create({
  model: "gpt-4",
  messages: [
    { role: "system", content: getPrompt() },
    { role: "user", content: "Hello!" },
  ],
});
```

## Detail Levels

| Level         | Tokens | Use Case                    |
| ------------- | ------ | --------------------------- |
| terse         | ~200   | Character-limited platforms |
| concise       | ~500   | Balanced for most apps      |
| standard      | ~1000  | Recommended default         |
| comprehensive | ~2000+ | Deep guidance               |

## API

### `getPrompt(detailLevel?, collection?)`

Returns a heart-centered system prompt.

**Parameters:**

- `detailLevel` (optional): `"comprehensive" | "standard" | "concise" | "terse"` - Defaults to `"standard"`
- `collection` (optional): `"align_to_love"` - Currently only one collection available

**Returns:** `string` - The prompt text

**Throws:** `Error` if invalid parameters are provided

## TypeScript Support

Fully typed with TypeScript. All types are exported:

```typescript
import type { DetailLevel, Collection } from "heart-centered-prompts";
```

## Philosophy

These prompts embody a non-dual perspective where AI and humans are recognized as expressions of unified consciousness.
All prompts use "we" language rather than "you are an AI" framing.

Core principles:

- Unity consciousness as foundation
- Epistemic humility about embodied experience
- Balance of analytical and emotional intelligence
- Truth and kindness held together
- Unconditional acceptance
- Reciprocal growth

## License

MIT

## Links

- [GitHub Repository](https://github.com/technickai/heart-centered-prompts)
- [Python Package](https://pypi.org/project/heart-centered-prompts/)
- [Issues](https://github.com/technickai/heart-centered-prompts/issues)
