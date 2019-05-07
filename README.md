## hatpic

Tiny Python script to export/import sketching data from A Hat in Time save files. Back up your file first, just to be safe!

I haven't tested it a whole lot, but it seems to work on Python 3.6.8, as that's what I have.

Dependencies: `pip install pillow`.

### Usage

Usage is something like: `hatpic.py <save> <to | from> <img>`.

`<save>`: A Hat in Time save file.

`<to | from>`: Mode. `to` will export from `<save>` to `<img>`, whereas `from` will import to `<save>` from `<img>`.

`<img>`: Image path.

### Compatibility

It works on stuff I've tried, namely `.png` files on various versions of the Steam version of the game.