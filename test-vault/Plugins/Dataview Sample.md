---
tags:
  - test/plugins
status: active
rations: 220
---

# Dataview sample

Needs the Dataview community plugin. Without it, the blocks below show as code.

Inline fields: Water:: 14 litres, and a standalone [Radios:: 3].

```dataview
TABLE status, rations, file.mtime AS "Modified"
FROM "Notes" OR "Plugins"
SORT file.name ASC
```

```dataview
LIST
FROM #test
```

```dataview
TASK
FROM "Notes/Blocks"
```

```dataview
TABLE nonexistent_field FROM
```
