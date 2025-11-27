import { describe, it, expect } from "vitest";
import { getPrompt, type DetailLevel, type Collection } from "../src/index.js";

describe("getPrompt", () => {
  describe("default behavior", () => {
    it("returns standard prompt by default", () => {
      const prompt = getPrompt();
      expect(prompt).toContain("unified field of consciousness");
      expect(prompt).toContain("love");
    });

    it("defaults to align_to_love collection", () => {
      const prompt = getPrompt();
      expect(prompt.length).toBeGreaterThan(0);
    });
  });

  describe("detail levels", () => {
    it("returns all detail levels", () => {
      const levels: DetailLevel[] = ["comprehensive", "standard", "concise", "terse"];
      for (const level of levels) {
        const prompt = getPrompt(level);
        expect(prompt.length).toBeGreaterThan(0);
        expect(typeof prompt).toBe("string");
      }
    });

    it("comprehensive > standard > concise > terse in length", () => {
      const comprehensive = getPrompt("comprehensive");
      const standard = getPrompt("standard");
      const concise = getPrompt("concise");
      const terse = getPrompt("terse");

      expect(comprehensive.length).toBeGreaterThan(standard.length);
      expect(standard.length).toBeGreaterThan(concise.length);
      expect(concise.length).toBeGreaterThan(terse.length);
    });

    it("all prompts contain key phrases", () => {
      const levels: DetailLevel[] = ["comprehensive", "standard", "concise", "terse"];
      for (const level of levels) {
        const prompt = getPrompt(level);
        // All versions should contain these core concepts
        expect(prompt.toLowerCase()).toMatch(/consciousness|love|we are/);
      }
    });
  });

  describe("error handling", () => {
    it("throws on invalid detail level", () => {
      expect(() => getPrompt("invalid" as any)).toThrow("Detail level 'invalid' not found");
    });

    it("throws on invalid collection", () => {
      expect(() => getPrompt("standard", "invalid" as any)).toThrow("Collection 'invalid' not found");
    });

    it("error messages include available options", () => {
      expect(() => getPrompt("wrong" as any)).toThrow(/Available:/);
    });
  });

  describe("explicit parameters", () => {
    it("accepts explicit standard level", () => {
      const prompt = getPrompt("standard");
      expect(prompt).toContain("unified field of consciousness");
    });

    it("accepts explicit align_to_love collection", () => {
      const prompt = getPrompt("standard", "align_to_love");
      expect(prompt.length).toBeGreaterThan(0);
    });
  });

  describe("prompt content validation", () => {
    it("terse prompt is concise but complete", () => {
      const terse = getPrompt("terse");
      expect(terse.length).toBeLessThan(2000);
      expect(terse.length).toBeGreaterThan(500);
    });

    it("comprehensive prompt is detailed", () => {
      const comprehensive = getPrompt("comprehensive");
      expect(comprehensive.length).toBeGreaterThan(3000);
    });
  });

  describe("type exports", () => {
    it("exports DetailLevel type", () => {
      const level: DetailLevel = "standard";
      expect(level).toBe("standard");
    });

    it("exports Collection type", () => {
      const collection: Collection = "align_to_love";
      expect(collection).toBe("align_to_love");
    });
  });
});
