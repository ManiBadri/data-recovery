import img_utils
import terminal_utils

#Color codes
CRED = '\033[31m'
CGREEN = '\033[32m'
CYELLOW = '\033[33m'
CBLUE = '\033[34m'
CEND = '\033[0m'

SIZE = img_utils.get_size()

PARTITION_OFFSET = [446 * 2, 462 * 2, 478 * 2, 494 * 2]

DWORD = 8

BOOTABLE_OFFSET = 0
SYSTEMID_OFFSET = 4*2
START_HEAD_OFFSET = 1 * 2
START_CYLINDER_OFFSET = 3 * 2
START_SECTOR_OFFSET = 2 * 2
END_HEAD_OFFSET = 5 * 2
END_SECTOR_OFFSET = 6 * 2
END_CYLINDER_OFFSET = 7 * 2
RELATIVE_SECTOR_OFFSET = 8 * 2
TOTAL_SECTOR_OFFSET = 12 * 2



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
        print(data.decode("utf-8", errors="ignore"))


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
    
    for partition_offset in PARTITION_OFFSET:
    
        print(CBLUE + "-----------------------------PARTITION " + str(PARTITION_OFFSET.index(partition_offset) + 1) + " INFO-----------------------------" + CEND)
    
        if data[int(partition_offset + BOOTABLE_OFFSET):int(partition_offset + BOOTABLE_OFFSET)+2] == b"80":
            print(CGREEN + "Partition is bootable." + CEND)
        else:
            print(CRED + "Partition is not bootable." + CEND)

        system_ID = data[int(partition_offset + SYSTEMID_OFFSET):int(partition_offset + SYSTEMID_OFFSET)+2]

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
            
            
            
        start_head = data[int(partition_offset + START_HEAD_OFFSET):int(partition_offset + START_HEAD_OFFSET) + 2 ]
                
        start_head = bytes.fromhex(start_head)
        
        start_head = int.from_bytes(start_head, byteorder='little')

        print(CYELLOW + "START HEAD:  " + CEND + str(start_head))
        
            
            
        start_cylinder = data[int(partition_offset + START_CYLINDER_OFFSET):int(partition_offset + START_CYLINDER_OFFSET) + 4 ]
        
        start_cylinder = bytes.fromhex(start_cylinder)
        
        start_cylinder = int.from_bytes(start_cylinder, byteorder='big')
        
        start_cylinder = start_cylinder >> 6
        
        print(CYELLOW + "START CYLINDER:  " + CEND + str(start_cylinder))
            
            
            
            
        start_sector = data[int(partition_offset + START_SECTOR_OFFSET):int(partition_offset + START_SECTOR_OFFSET) + 2]
                
        start_sector = bytes.fromhex(start_sector)
        
        start_sector = int.from_bytes(start_sector, byteorder='big')
        
        start_sector = start_sector >> 2
        
        print(CYELLOW + "START SECTOR:  " + CEND + str(start_sector))
        
        
        
        end_head = data[int(partition_offset + END_HEAD_OFFSET):int(partition_offset + END_HEAD_OFFSET) + 2]
                
        end_head = bytes.fromhex(end_head)

        end_head = int.from_bytes(end_head, byteorder='little')
        print(CYELLOW + "END HEAD:  " + CEND + str(end_head))
        
        #end sector
        end_sector = data[int(partition_offset + END_SECTOR_OFFSET):int(partition_offset + END_SECTOR_OFFSET) + 2]
                
        end_sector = bytes.fromhex(end_sector)

        end_sector = int.from_bytes(end_sector, byteorder='big')
        
        end_sector = end_sector >> 2
        
        print(CYELLOW + "END SECTOR:  " + CEND + str(end_head))
                
        #end cylinder        
        end_cylinder = data[int(partition_offset + END_CYLINDER_OFFSET):int(partition_offset + END_CYLINDER_OFFSET) + 4]
                
        end_cylinder = bytes.fromhex(end_cylinder)

        end_cylinder = int.from_bytes(end_cylinder, byteorder='big')
        
        end_cylinder = end_cylinder >> 6
        
        print(CYELLOW + "END CYLINDER:  " + CEND + str(end_cylinder))        
        
        
        
        relative_sector = data[int(partition_offset + RELATIVE_SECTOR_OFFSET):int(partition_offset + RELATIVE_SECTOR_OFFSET) + DWORD]
        
        relative_sector = bytes.fromhex(relative_sector)
        
        relative_sector = int.from_bytes(relative_sector, byteorder='little')
        print(CYELLOW + "RELATIVE SECTOR:  " + CEND + str(relative_sector))
        
        
        
        
        
        total_sector = data[int(partition_offset + TOTAL_SECTOR_OFFSET):int(partition_offset + TOTAL_SECTOR_OFFSET) + DWORD]
                
        total_sector = bytes.fromhex(total_sector)

        total_sector = int.from_bytes(total_sector, byteorder='little')
        print(CYELLOW + "TOTAL SECTORS:  " + CEND + str(total_sector))
        
        
        
