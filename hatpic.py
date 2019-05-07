from PIL import Image
from struct import pack, unpack
from sys import argv, exit

if len(argv) <= 3:
    print("Not enough arguments!")
    print("Usage: python hatpic.py <save> <to | from> <png>")
    exit()

save = open(argv[1], "r+b")

savedata = save.read()
bmpstart = savedata.find(b"SketchingData") + 0x2B

# save -> png
if argv[2] == "to":
    img = Image.new("RGBA", (512, 512), "white")
    pixels = img.load()

    for col in range(512):
        for row in range(512):
            # lengthy way of getting 4 bytes
            pixel = unpack("BBBB", savedata[bmpstart + (col * 4) + (row * 4 * 512) : bmpstart + (col * 4) + (row * 4 * 512) + 4])
            pixels[col, row] = (pixel[1], pixel[2], pixel[3], pixel[0])

    img.save(argv[3])

# png -> save
elif argv[2] == "from":
    img = Image.open(argv[3])
    img = img.convert("RGBA")
    pixels = img.load()
    save.seek(bmpstart, 0)

    for row in range(512):
        for col in range(512):
            pixel = pixels[col, row]

            # transparent is special
            if pixel[0] == 0xFF and pixel[1] == 0xFF and pixel[2] == 0xFF and pixel[3] == 0x00:
                pixel = (0x00, 0xFF, 0x00, 0xFF)
            else:
                pixel = (pixel[3], pixel[0], pixel[1], pixel[2])

            save.write(pack("BBBB", pixel[0], pixel[1], pixel[2], pixel[3]))

save.close()