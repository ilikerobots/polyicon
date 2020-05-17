Development docs
================

Set of scripts to easily build webfonts from SVG images

Installation
------------

```sh
npm install
```


Updating font to the newest Font Awesome version
------------------------------------------------

### Steps

1. Download or clone the [Font Awesome distribution](https://github.com/FortAwesome/Font-Awesome)
2. Place the new Font Awesome's [`fonts/fontawesome-webfont.svg`](https://github.com/FortAwesome/Font-Awesome/blob/master/fonts/fontawesome-webfont.svg) in `src/original`
3. Run `make dump` to create the corresponding SVG glyph files in `src/svg`
4. Any new glyph requiring an entry in `config.yml` will be found in a temporary `diff.yml` file; check Font Awesome's [`less/variables.less`](https://github.com/FortAwesome/Font-Awesome/blob/master/less/variables.less) to find the name of the glyph matching the corresponding `code:` in `diff.yml`, then copy the updated entry to `config.yml`
5. Once `config.yml` has been updated with all new glyphs, run `make dump` once again to make sure all temporary files (say `src/svg/glyph__f22d.svg`) are replaced with properly named glyphs (say `src/svg/genderless.svg`)
6. Run `make`

Generated data will be placed in `./font`

You can rebuild css/html only with `make html`

### Tips

After running `make dump`, use:
```
cat diff.yml | grep code | cut -c 14-17 | while read CODE; do grep $CODE path/to/Font-Awesome/less/variables.less; done
```
To match the glyphs in `diff.yml` with the corresponding Font Awesome names in `Font-Awesome/less/variables.less`.

### SVG image requirements

Any image will be proportionally scaled, to fit height in ascent-descent
It's convenient to make height = 1000px. Default font baseline will be 20% from
the bottom.

In most cases it's ok to visually align icons to middle line, not to baseline.
If you are not sure, how to start - make image with 10% top/bottom padding.
Then generate demo page and tune scale/offset.
