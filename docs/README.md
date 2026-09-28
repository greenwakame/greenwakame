# Greenwakame Lab

This folder is the GitHub Pages source for the Showcase at
`https://greenwakame.github.io/greenwakame/`. The profile `README.md` at the
repository root is separate.

## Add a work

1. Add `docs/_works/<slug>.md`. Copy the front matter shape from
   `hyperframes-profile-pv.md`, then write the short project story below it.
2. Add a 16:9 poster to `docs/assets/works/<slug>/`. Set `thumbnail` and
   `thumbnail_alt` in the work file. An optimized JPEG or WebP is suitable.
3. If the work has a video, put the MP4 alongside the poster and set
   `media.type: video` and `media.src`. For an image-led work, use
   `media.type: image`, `media.src`, and `media.alt`.
4. Give the file a stable `slug`; it becomes `/works/<slug>/`. Set `featured:
   true` only for work that should be eligible for the Home feature.
5. Preview the Home page, `/works/`, and the new detail page at desktop and
   mobile widths. The two lists and detail page come from the same work file.

Leave `github` or `demo` empty if the destination is unavailable. Use
`published: false` in front matter for a draft you do not want Jekyll to
generate. Keep source assets reasonably small; for a much larger video,
evaluate a GitHub Release asset before adding it to the repository.

## Local preview

Run Jekyll from the repository root:

```sh
jekyll serve --source docs
```

The `baseurl` is `/greenwakame`, so the preview URL is
`http://localhost:4000/greenwakame/`.

GitHub Pages is configured to publish from `main` / `docs`. The existing
`gh-pages` branch is reserved for the contribution snake and is not used as
the Showcase source.
