FlutterIcon - Flutter icon font creator
=======================================

[![Build Status](https://travis-ci.org/ilikerobots/polyicon.png)](https://travis-ci.org/ilikerobots/polyicon)

website: [fluttericon.com](http://fluttericon.com/), help: [wiki](https://github.com/ilikerobots/polyicon/wiki/Help)

FlutterIcon is a web-based generator of Flutter icon font elements.
Customized icon fonts can be produced from not only Material Design Icons,
but several popular open source webfonts as well, or by uploading 
your own svg art.

## Contacts
 
Please report all issues on the [GitHub issue tracker](https://github.com/ilikerobots/fluttericon/issues)
including request for additional fonts.

## API Mode

To be documented.  

The quick answer is to use [fontello-cli](https://github.com/paulyoung/fontello-cli)
and set the `--host` option to `fluttericon.com`.  Example to download a font:

```sh
./fontello-cli --config ~/Downloads/config.json  --host https://fluttericon.com install
```

## Authors

- Mike Hoolehan ([ilikerobots](https://github.com/ilikerobots))

## Fontello

This project is a fork of Fontello, a great product for producing 
webfonts.  The authors of that project declined a Merge Request to 
support generation of polymer iconsets directly in Fontello, so 
PolyIcon was spun off to handle that task exclusively.  I didn't 
bother asking about Flutter icons. ;)

Many thanks to the authors of Fontello for their excellent work.
 * Roman Shmelev ([shmelev](https://github.com/shmelev))
 * Vitaly Puzrin ([puzrin](https://github.com/puzrin)).
 * Aleksey Zapparov ([ixti](https://github.com/ixti)).
 * Evgeny Shkuropat ([shkuropat](https://github.com/shkuropat)).
 * Vladimir Zapparov ([dervus](https://github.com/dervus)).

## License

FlutterIcon's code (all files, except fonts) is distributed under MIT license. See
[LICENSE](https://github.com/ilikerobots/polyicon/blob/master/LICENSE) file for details.

Embedded fonts are distributed under their primary licenses (SIL OFL / CC BY / CC BY-SA, Apache 2.0).
See fonts info on FlutterIcon.com for credits & links to homepages. This info is also
included in generated font archives for your convenience (see LICENSE.txt file).

Generated fonts are intended for web or app usage, and should not be
considered/distributed as independent artwork. 

Crediting FlutterIcon is not required.
