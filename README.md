PolyIcon - iron-iconset-svg generator
=====================================

[![Build Status](https://travis-ci.org/ilikerobots/polyicon.png)](https://travis-ci.org/ilikerobots/polyicon)

website: [polyicon.com](http://polyicon.com/), help: [wiki](https://github.com/ilikerobots/polyicon/wiki/Help)

PolyIcon is a web-based generator of Polymer iron-iconset-svg elements.
Customized iconset can be produced from not only Material Design Icons,
but several popular open source webfonts as well, or by uploading 
your own svg art.

## Contacts
 
Please report all issues on the [GitHub issue tracker](https://github.com/ilikerobots/polyicon/issues)
including request for additional fonts.

## API Mode

To be documented.  

The quick answer is to use [fontello-cli](https://github.com/paulyoung/fontello-cli)
and set the `--host` option to `polyicon.com`.  Example to download a font:

```sh
./fontello-cli --config ~/Downloads/config.json  --host polyicon.com install
```

## Authors

- Mike Hoolehan ([ilikerobots](https://github.com/ilikerobots))

## Fontello

This project is a fork of Fontello, an great product for producing 
webfonts.  The authors of that project declined a Merge Request to 
support generation of polymer iconsets directly in Fontello, so 
PolyIcon was spun off to handle that task exclusively.

Many thanks to the authors of Fontello for their excellent work.

-- Roman Shmelev ([shmelev](https://github.com/shmelev))
-- Vitaly Puzrin ([puzrin](https://github.com/puzrin)).
-- Aleksey Zapparov ([ixti](https://github.com/ixti)).
-- Evgeny Shkuropat ([shkuropat](https://github.com/shkuropat)).
-- Vladimir Zapparov ([dervus](https://github.com/dervus)).

## License

PolyIcon's code (all files, except fonts) is distributed under MIT license. See
[LICENSE](https://github.com/ilikerobots/polyicon/blob/master/LICENSE) file for details.

Embedded fonts are distributed under their primary licenses (SIL OFL / CC BY / CC BY-SA, Apache 2.0).
See fonts info on PolyIcon.com for credits & links to homepages. This info is also
included in generated font archives for your convenience (see LICENSE.txt file).

Generated fonts are intended for web usage, and should not be
considered/distributed as independent artwork. 

Crediting PolyIcon is not required.
