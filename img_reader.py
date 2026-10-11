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

class Partition:
    def __init__(self, bootable, system_type, start_head, start_sector, start_cylinder, end_head, end_sector, end_cylinder, relative_sector, total_sectors):
        self.bootable = bootable
        self.system_type = system_type
        self.start_head = start_head
        self.start_sector = start_sector
        self.start_cylinder = start_cylinder
        self.end_head = end_head
        self.end_sector = end_sector
        self.end_cylinder = end_cylinder
        self.relative_sector = relative_sector
        self.total_sectors = total_sectors



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


def get_data(data, partition_offset, offset, length):
    
    value = data[int(partition_offset + offset):int(partition_offset + offset) + length]
                    
    value = bytes.fromhex(value)
    
    value = int.from_bytes(value, byteorder='little')
    
    return str(value)
            
    

def decode_MBR():
    with open("test.img", "rb") as image:
        data = image.read()
    data = bytearray(data)
    print("total size: ", SIZE)

    partition = {}
    

    for partition_number, partition_offset in enumerate(PARTITION_OFFSET, start=1):

        partition[partition_number] = Partition(None, None, None, None, None, None, None, None, None, None)

        print(CBLUE + "-----------------------------PARTITION " + str(partition_number) + " INFO-----------------------------" + CEND)
    
        if data[int(partition_offset + BOOTABLE_OFFSET):int(partition_offset + BOOTABLE_OFFSET)+2] == b"80":
            print(CGREEN + "Partition is bootable." + CEND)
            partition[partition_number].bootable = True
        else:
            partition[partition_number].bootable = False
            print(CRED + "Partition is not bootable." + CEND)

        
        system_ID = data[int(partition_offset + SYSTEMID_OFFSET):int(partition_offset + SYSTEMID_OFFSET)+2]

        match system_ID:
            case b"01":
                partition[partition_number].system_type = "FAT12"
                system_type = "FAT12"
            case b"04":
                partition[partition_number].system_type = "FAT16"
                system_type = "FAT16"
            case b"05":
                partition[partition_number].system_type = "Extended partition"
                system_type = "Extended partition"
            case b"06":
                partition[partition_number].system_type = "BIGDOS FAT"
                system_type = "BIGDOS FAT"
            case b"07":
                partition[partition_number].system_type = "NTFS"
                system_type = "NTFS"
            case _:
                partition[partition_number].system_type = "TYPE UNKNOWN"
                system_type = "TYPE UNKNOWN"

        if system_ID == "TYPE UNKNOWN":
            print(CRED + "TYPE UNKNOWN" + CEND)
        else:
            print(CYELLOW + "SYSTEM TYPE:  " + CEND + system_type)
            
            
            
        #start head
        partition[partition_number].start_head = get_data(data, partition_offset, START_HEAD_OFFSET, 2)
        print(CYELLOW + "START HEAD:  " + CEND + partition[partition_number].start_head)
        
        
        #start sector and cyl
        start_sector_byte = data[partition_offset + START_SECTOR_OFFSET : partition_offset + START_SECTOR_OFFSET + 2]
        start_cylinder_byte = data[partition_offset + START_CYLINDER_OFFSET : partition_offset + START_CYLINDER_OFFSET + 2]
        
        start_sector_byte = int(start_sector_byte, 16)
        start_cylinder_byte = int(start_cylinder_byte, 16)
        start_cylinder_sector_byte = int(data[partition_offset + START_SECTOR_OFFSET : partition_offset + START_SECTOR_OFFSET + 2], 16,)

        start_sector = start_sector_byte & 0x3F
        start_cylinder = ((start_cylinder_sector_byte & 0xC0) << 2) | start_cylinder_byte
        
        partition[partition_number].start_sector = start_sector
        partition[partition_number].start_cylinder = start_cylinder

        print(CYELLOW + "START SECTOR: "  + CEND , start_sector)
        print(CYELLOW + "START CYLINDER: "+ CEND , start_cylinder)
        
        
        end_sector_byte = data[partition_offset + END_SECTOR_OFFSET : partition_offset + END_SECTOR_OFFSET + 2]
        end_cylinder_byte = data[partition_offset + END_CYLINDER_OFFSET : partition_offset + END_CYLINDER_OFFSET + 2]
        
        end_sector_byte = int(end_sector_byte, 16)
        end_cylinder_byte = int(end_cylinder_byte, 16)
        end_cylinder_sector_byte = int(data[partition_offset + END_SECTOR_OFFSET : partition_offset + END_SECTOR_OFFSET + 2], 16,)

        end_sector = end_sector_byte & 0x3F
        end_cylinder = ((end_cylinder_sector_byte & 0xC0) << 2) | end_cylinder_byte
        
        partition[partition_number].end_sector = end_sector
        partition[partition_number].end_cylinder = end_cylinder

        print(CYELLOW + "END SECTOR: " + CEND, end_sector)
        print(CYELLOW + "END CYLINDER:" + CEND, end_cylinder)
        
        #relative sector
        partition[partition_number].relative_sector = get_data(data, partition_offset, RELATIVE_SECTOR_OFFSET, DWORD)
        print(CYELLOW + "RELATIVE SECTOR:  " + CEND + partition[partition_number].relative_sector)
        
        #total sectors
        partition[partition_number].total_sectors = get_data(data, partition_offset, TOTAL_SECTOR_OFFSET, DWORD)
        print(CYELLOW + "TOTAL SECTORS:  " + CEND + partition[partition_number].total_sectors)
        
        
        
        
def select_boot_sector(partition_number):
    if partition_number < 1 or partition_number > 4:
        print("Invalid partition number. Please select a number between 1 and 4.")
        return None
    return PARTITION_OFFSET[partition_number - 1]

        