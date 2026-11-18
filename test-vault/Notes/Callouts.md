---
tags:
  - test/callouts
---

# Callouts

Every built-in type, then each alias.

> [!note]
> Note callout with **bold**, `code` and a [[Blocks|link]].

> [!abstract]
> Abstract callout.

> [!info]
> Info callout.

> [!todo]
> Todo callout.

> [!tip]
> Tip callout.

> [!success]
> Success callout.

> [!question]
> Question callout.

> [!warning]
> Warning callout.

> [!failure]
> Failure callout.

> [!danger]
> Danger callout.

> [!bug]
> Bug callout.

> [!example]
> Example callout.

> [!quote]
> Quote callout.

## Custom titles, folding, nesting

> [!info] A custom title
> Body text.

> [!tip]- Folded by default
> Hidden until opened.

> [!warning]+ Foldable, open by default
> Visible, can be folded.

> [!question] Title only

> [!note] Outer callout
> Outer body.
> > [!danger] Inner callout
> > Inner body.

## Aliases

> [!summary]
> summary → abstract

> [!tldr]
> tldr → abstract

> [!hint]
> hint → tip

> [!important]
> important → tip

> [!check]
> check → success

> [!done]
> done → success

> [!help]
> help → question

> [!faq]
> faq → question

> [!caution]
> caution → warning

> [!attention]
> attention → warning

> [!fail]
> fail → failure

> [!missing]
> missing → failure

> [!error]
> error → danger

> [!cite]
> cite → quote

## Terminal

> [!terminal]
> Default title. The header line and blinking cursor come from the theme.

> [!terminal] Maintenance log
> Pump 2 pressure nominal.
> Filter change due in 6 days.
> Awaiting input.

> [!terminal]- Folded terminal
> Opens on click.
