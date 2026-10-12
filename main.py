
import img_maker
import img_reader
import terminal_utils


#Color codes
CRED = '\033[31m'
CGREEN = '\033[32m'
CYELLOW = '\033[33m'
CBLUE = '\033[34m'
CEND = '\033[0m'

def boot_sector():
    while True:
        action = input("Select Partition boot sector ([1]Partition 1 [2]Partition 2 [3]Partition 3 [4]Partition 4 " + CRED + "[Q]back): "+ CEND)
        if action == "1":
            terminal_utils.clear_terminal()
            print(img_reader.select_boot_sector(1))
        elif action == "2":
            terminal_utils.clear_terminal()
            print(img_reader.select_boot_sector(2))
        elif action == "3":
            terminal_utils.clear_terminal()
            print(img_reader.select_boot_sector(3))
        elif action == "4":
            terminal_utils.clear_terminal()
            print(img_reader.select_boot_sector(4))
        elif action == "Q" or action == "q":
            terminal_utils.clear_terminal()
            return

while True:
    terminal_utils.clear_terminal()
    action = input("Enter action ([1]decode MBR [2]write "  + CRED + "[Q]exit): " + CEND)
    if action == "2":
        terminal_utils.clear_terminal()
        img_maker.create_image()
    elif action == "1":
        terminal_utils.clear_terminal()
        img_reader.decode_MBR()
        boot_sector()
    elif action == "Q" or action == "q":
        terminal_utils.clear_terminal()
        break
            