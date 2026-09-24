SECTOR_SIZE = 512

def create_image():
    with open("test.img", "wb") as image:
        image.write(b"\x00" * SECTOR_SIZE * 100)  # Create a 100-sector image filled with zeros

        image.seek(0)  #Move to the 1st sector

        #image.write(b"")
        with open("MBR.bmp", "rb") as bmp:
            image.write(bmp.read())