

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
            my_bytes = my_bytes.split(",")
            my_bytes = [int(x) for x in my_bytes]
            print((int(my_bytes[0])).to_bytes(2, byteorder='big') + b" to " + (int(my_bytes[1])).to_bytes(2, byteorder='big'))
    
            if my_bytes == "x":
                break
            with open("test.img", "rb") as image:
                data = image.read()
            data = bytearray(data)
            print(data[int(my_bytes[0]):int(my_bytes[1])].decode("utf-8", errors="ignore"))  # Print the first 10 bytes as a sample
