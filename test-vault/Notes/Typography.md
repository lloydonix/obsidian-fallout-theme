---
tags:
  - test/typography
author: Test Unit
word-count: 412
---

# Heading level one

Body paragraph under H1. Stores: water purifier parts, 14; ration packs, 220; working radios, 3. The quick brown fox jumps over the lazy dog. 0123456789 — Il1| O0 and the symbols `{}[]() <> => != ===`

## Heading level two

Body paragraph under H2, long enough to wrap so line height and measure can be judged at a normal reading width without leaning on short test lines that never reach the edge of the column.

### Heading level three

#### Heading level four

##### Heading level five

###### Heading level six

## Inline styles

Plain text, **bold text**, *italic text*, ***bold italic text***, ~~strikethrough text~~, ==highlighted text==, and `inline code` in a sentence.

A **bold phrase with `code` inside** and an *italic phrase with a [[Blocks|link]] inside*.

## Links

- Internal link: [[Blocks]]
- Internal link with alias: [[Callouts|the callout sampler]]
- Link to a heading: [[Blocks#Tables]]
- Unresolved link: [[Reactor Maintenance Schedule]]
- Unresolved link with alias: [[Not Written Yet|a note that is not written]]
- External link: [Obsidian help](https://help.obsidian.md)
- Bare URL: https://obsidian.md

## Tags

Inline tags: #status/online #inventory #test-tag #nested/deeper/tag

## Code

Inline: run `obsidian --version`, then press `Ctrl` + `P`.

```js
// Ration distribution, one pack per resident per day
function rations(residents, days) {
  const perDay = residents.length;
  return { total: perDay * days, note: `for ${days} days` };
}
```

```python
def water_ok(litres: float, residents: int) -> bool:
    """Two litres per resident per day."""
    return litres >= residents * 2  # comment
```

```
Plain code block, no language.
    Indented line.
```

## Footnotes

Water chip output is checked weekly.[^1] Radio logs are kept for ninety days.[^long]

Inline footnote here.^[An inline footnote, written in the sentence itself.]

[^1]: A short footnote.
[^long]: A longer footnote that runs on for more than one line so the wrapping inside the footnote list can be checked against the body measure.
