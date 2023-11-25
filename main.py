from PIL import Image

infile = "image.jpeg"
outfile = "output.gif"
outfile2 = "output2.thumnail.gif"
size = (128, 128)


with Image.open(infile) as im:
    im.save(outfile)
    print("Dosya Oluştu\n")
    im.thumbnail(size)
    im.save(outfile2, "JPEG")
    print("Thumbnail oluştu...")