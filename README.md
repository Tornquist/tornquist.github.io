# tornquist.github.io

This is the personal website of Nathan Tornquist.

Built with [Jekyll](https://jekyllrb.com/docs/posts/).
Hosted on [GitHub Pages](https://pages.github.com/).
Available at [NathanTornquist.com](https://nathantornquist.com)

All thoughts and opinions expressed here are my own.

## Image generation

Images can be either embedded dynamically using `_includes/photos` or can be
generated using `make images`. Make images relies on ImageMagick, and will
scan the contents of `_posts/` and `_projects/` for patterns like:

```
!@ generate_image <output name>
  <input image>
  <input image>
!@ end_generate
```

At this time the `make images` command requires that all images used as input
for a given output image are the same size. This tool is primarily used for lining
up screenshots.