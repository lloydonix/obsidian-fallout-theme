# Submitting Fallout to the Obsidian community themes

## Entry for `community-css-themes.json`

Add this object at the end of the array in [obsidianmd/obsidian-releases](https://github.com/obsidianmd/obsidian-releases/blob/master/community-css-themes.json). It assumes the repository will be `lloydonix/obsidian-fallout-theme`; change `repo` if you publish it under another name.

```json
{
  "name": "Fallout",
  "author": "leolloydc",
  "repo": "lloydonix/obsidian-fallout-theme",
  "screenshot": "screenshot.png",
  "modes": ["dark"]
}
```

- `name` must match `manifest.json` exactly ("Fallout").
- `screenshot` is the 512×288 gallery thumbnail at the repository root.
- `modes` is `["dark"]` only, because v1 is dark mode only.

## Note for the PR description

> Fallout is an unofficial fan-made theme. It is not affiliated with, endorsed by, or associated with Bethesda Softworks, ZeniMax Media, or Microsoft. Fallout is a trademark of Bethesda Softworks LLC.

## Before opening the PR

1. Create the public repository `lloydonix/obsidian-fallout-theme` and push `main`.
2. Make sure these are on `main` at the repository root:
   - `theme.css`
   - `manifest.json`
   - `README.md`
   - `LICENSE`
   - `screenshot.png` (512×288, theme only, no game images)
3. Push the tag `0.1.0`. The release workflow publishes a GitHub release with `theme.css` and `manifest.json`.
4. Install the theme by hand in a clean vault from the release files and check that it loads.

## Opening the PR

1. Fork `obsidianmd/obsidian-releases`.
2. Edit `community-css-themes.json` and add the entry above as the last item. Mind the comma after the previous item.
3. Commit with the message `Add theme: Fallout`.
4. Open a pull request against `master`. Choose the **theme** template from the "Preview" tab of the PR form, or paste it from the repository's `.github/PULL_REQUEST_TEMPLATE/` folder.
5. Fill in the checklist, and put the disclaimer above in the description.
6. Wait for the automated validation bot. Fix anything it flags in your repository, not in the PR, unless the problem is in the JSON entry itself.
7. A reviewer may ask for changes. Once the PR is merged, the theme shows up in Settings → Appearance → Themes → Manage.

## Watch out for

- **The name.** "Fallout" is a trademark. Reviewers may ask for a name that doesn't use it, such as "Phosphor Terminal". If they do, the name has to change in `manifest.json`, the JSON entry, the folder name in the install steps, and the `@settings` block's `name`. The `id` can stay.
- **Screenshots.** Use only Obsidian windows showing the theme. No in-game images, logos or mascots.
