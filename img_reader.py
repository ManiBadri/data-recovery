#Color codes
CRED = '\033[31m'
CGREEN = '\033[32m'
CYELLOW = '\033[33m'
CBLUE = '\033[34m'
CEND = '\033[0m'

def read_MBR():
    with open("test.img", "rb") as image:
        image.seek(0) 
        mbr_data = image.read(512)  
        mbr_data.find(b"00 55 AA")
    print("ok")


def read_sector():
    while True:

        sector = input("Enter sector number: or x to exit: ")
        if sector == "x":
            break
        sector = int(sector)
        with open("test.img", "rb") as image:
            image.seek(sector * 512)
            data = image.read(512)  #Each sector is 512 bytes.
        print(type(data))
        print(data.decode("utf-8"))


def read_bytes():
    while True:
    
            my_bytes = input("Enter byte number: or x to exit: ")
            if my_bytes == "x":
                break
            with open("test.img", "rb") as image:
                data = image.read()
            data = bytearray(data)
            my_bytes = int(my_bytes)
            print(data[int(my_bytes*2):int(my_bytes*2)+2].decode("utf-8", errors="ignore")) 


def read_boot_sector():
    with open("test.img", "rb") as image:
        data = image.read()
    data = bytearray(data)
    print(data[int(446*2):int(446*2)+2].decode("utf-8", errors="ignore"))
    print(data[int(446*2):int(446*2)+2])
    
    print(CBLUE + "-----------------------------PARTITION 1 INFO-----------------------------" + CEND)
    
    if data[int(446*2):int(446*2)+2] == b"80":
        print(CGREEN + "Partition is bootable." + CEND)
    else:
        print(CRED + "Partition is not bootable." + CEND)