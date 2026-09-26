
import img_maker
import img_reader


while True:
    action = input("Enter action (read/write): ")

    if action == "write":
        img_maker.create_image()
    elif action == "read":
        img_reader.read_boot_sector()
        action = input("Enter read action [(1)MBR] [(2)sector] [(3)hex] [(4)back]: ")
        if action == "1":
            img_reader.read_MBR()
        elif action == "2":
            img_reader.read_sector()
        elif action == "3":
            img_reader.read_bytes()
        elif action == "4":
            continue
            