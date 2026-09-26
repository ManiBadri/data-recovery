
import img_maker
import img_reader
import terminal_utils


#Color codes
CRED = '\033[31m'
CGREEN = '\033[32m'
CYELLOW = '\033[33m'
CBLUE = '\033[34m'
CEND = '\033[0m'


while True:
    terminal_utils.clear_terminal()
    action = input("Enter action ([1]read [2]write "  + CRED + "[3]exit): " + CEND)

    if action == "2":
        terminal_utils.clear_terminal()
        img_maker.create_image()
    elif action == "1":
        terminal_utils.clear_terminal()
        img_reader.read_partition_info()
        action = input("Enter read action ([1]MBR [2]sector [3]hex "  + CRED + "[4]back): "+ CEND)
        if action == "1":
            terminal_utils.clear_terminal()
            img_reader.read_MBR()
        elif action == "2":
            terminal_utils.clear_terminal()
            img_reader.read_sector()
        elif action == "3":
            terminal_utils.clear_terminal()
            img_reader.read_bytes()
        elif action == "4":
            continue
    else:
        terminal_utils.clear_terminal()
        break
            