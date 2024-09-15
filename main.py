import os
import shutil

def move_items_to_parent_and_cleanup():
    root_path = input("Please enter path to folder: ")
    if not os.path.isdir(root_path):
        raise NotADirectoryError(f"{root_path} is not a directory")
    for item in os.listdir(root_path):
        if os.path.isdir(os.path.join(root_path, item)):
            parent_folder_path = os.path.join(root_path, item)

            sub_folders = os.listdir(parent_folder_path)
            print("Total subfolders found : ", len(sub_folders))

            for sub_folder in sub_folders:
                folder_path = os.path.join(parent_folder_path, sub_folder)
                if os.path.isdir(folder_path):
                    for item_name in os.listdir(folder_path):
                        item_path = os.path.join(folder_path, item_name)
                        shutil.move(item_path, os.path.join(parent_folder_path, item_name))
                        print(f"Moved {item_name} to {parent_folder_path}")
                    os.rmdir(folder_path)
                    print(f"Removed {folder_path}")

def main():
    move_items_to_parent_and_cleanup()

if __name__ == '__main__':
    main()