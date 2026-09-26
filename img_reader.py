import img_utils

#Color codes
CRED = '\033[31m'
CGREEN = '\033[32m'
CYELLOW = '\033[33m'
CBLUE = '\033[34m'
CEND = '\033[0m'

SIZE = img_utils.get_size()

PARTITION_1_OFFSET = 446 * 2
PARTITION_2_OFFSET = 462 * 2
PARTITION_3_OFFSET = 478 * 2
PARTITION_4_OFFSET = 494 * 2

BOOTABLE_OFFSET = 0

SYSTEMID_OFFSET = 4*2



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


def read_partition_info():
    with open("test.img", "rb") as image:
        data = image.read()
    data = bytearray(data)
    print(SIZE)
    print(CBLUE + "-----------------------------PARTITION 1 INFO-----------------------------" + CEND)
    
    if data[int(PARTITION_1_OFFSET + BOOTABLE_OFFSET):int(PARTITION_1_OFFSET + BOOTABLE_OFFSET)+2] == b"80":
        print(CGREEN + "Partition is bootable." + CEND)
    else:
        print(CRED + "Partition is not bootable." + CEND)
        
    system_ID = data[int(PARTITION_1_OFFSET + SYSTEMID_OFFSET):int(PARTITION_1_OFFSET + SYSTEMID_OFFSET)+2]
    
    match system_ID:
        case b"01":
            system_type = "FAT12"
        case b"04":
            system_type = "FAT16"
        case b"05":
            system_type = "Extended partition"
        case b"06":
            system_type = "BIGDOS FAT"
        case b"07":
            system_type = "NTFS"
        case _:
            system_type = "TYPE UKNMOWN"
    
    if system_ID == "TYPE UNKNOWN":
        print(CRED + "TYPE UNKNOWN" + CEND)
    else:
        print(CYELLOW + "SYSTEM TYPE:  " + CEND + system_type)
        
    print(CBLUE + "-----------------------------PARTITION 2 INFO-----------------------------" + CEND)
        
    if data[int(PARTITION_2_OFFSET + BOOTABLE_OFFSET):int(PARTITION_2_OFFSET + BOOTABLE_OFFSET)+2] == b"80":
        print(CGREEN + "Partition is bootable." + CEND)
    else:
        print(CRED + "Partition is not bootable." + CEND)
        
    system_ID = data[int(PARTITION_2_OFFSET + SYSTEMID_OFFSET):int(PARTITION_2_OFFSET + SYSTEMID_OFFSET)+2]
    
    match system_ID:
        case b"01":
            system_type = "FAT12"
        case b"04":
            system_type = "FAT16"
        case b"05":
            system_type = "Extended partition"
        case b"06":
            system_type = "BIGDOS FAT"
        case b"07":
            system_type = "NTFS"
        case _:
            system_type = "TYPE UKNMOWN"
    
    if system_ID == "TYPE UNKNOWN":
        print(CRED + "TYPE UNKNOWN" + CEND)
    else:
        print(CYELLOW + "SYSTEM TYPE:  " + CEND + system_type)
    
            
    print(CBLUE + "-----------------------------PARTITION 3 INFO-----------------------------" + CEND)
            
    if data[int(PARTITION_3_OFFSET + BOOTABLE_OFFSET):int(PARTITION_3_OFFSET + BOOTABLE_OFFSET)+2] == b"80":
        print(CGREEN + "Partition is bootable." + CEND)
    else:
        print(CRED + "Partition is not bootable." + CEND)
        
    system_ID = data[int(PARTITION_3_OFFSET + SYSTEMID_OFFSET):int(PARTITION_3_OFFSET + SYSTEMID_OFFSET)+2]
    
    match system_ID:
        case b"01":
            system_type = "FAT12"
        case b"04":
            system_type = "FAT16"
        case b"05":
            system_type = "Extended partition"
        case b"06":
            system_type = "BIGDOS FAT"
        case b"07":
            system_type = "NTFS"
        case _:
            system_type = "TYPE UKNMOWN"
    
    if system_ID == "TYPE UNKNOWN":
        print(CRED + "TYPE UNKNOWN" + CEND)
    else:
        print(CYELLOW + "SYSTEM TYPE:  " + CEND + system_type)
    
    print(CBLUE + "-----------------------------PARTITION 2 INFO-----------------------------" + CEND)
            
    if data[int(PARTITION_4_OFFSET + BOOTABLE_OFFSET):int(PARTITION_4_OFFSET + BOOTABLE_OFFSET)+2] == b"80":
        print(CGREEN + "Partition is bootable." + CEND)
    else:
        print(CRED + "Partition is not bootable." + CEND)
        
    system_ID = data[int(PARTITION_4_OFFSET + SYSTEMID_OFFSET):int(PARTITION_4_OFFSET + SYSTEMID_OFFSET)+2]
    
    match system_ID:
        case b"01":
            system_type = "FAT12"
        case b"04":
            system_type = "FAT16"
        case b"05":
            system_type = "Extended partition"
        case b"06":
            system_type = "BIGDOS FAT"
        case b"07":
            system_type = "NTFS"
        case _:
            system_type = "TYPE UKNMOWN"
    
    if system_ID == "TYPE UNKNOWN":
        print(CRED + "TYPE UNKNOWN" + CEND)
    else:
        print(CYELLOW + "SYSTEM TYPE:  " + CEND + system_type)
