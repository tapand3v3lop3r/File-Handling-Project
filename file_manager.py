from pathlib import Path
import os

def show_files_and_folders():
    path = Path('')
    items = list(path.rglob('*'))

    for i, items in enumerate(items):
        print(f"{i+1} : {items}")


def create_file():
    
    try:
        show_files_and_folders()
        
        name = input("Please enter your file name: ")

        p = Path(name)

        if not p.exists():
            with open(p, 'w') as fs:
                data = input("What you want to write in this file: ")
                fs.write(data)

            print("File created successfully...")
        else:
            print("This file already exists...")
    
    except Exception as err:
        print(f"An error occured as {err}")


def read_file():
    
    try:
        show_files_and_folders()

        name = input("Which file you want to read?")

        p = Path(name)

        if p.exists() and p.is_file():
            with open (p, 'r') as fs:
                data = fs.read()
                print(data)

            print("File read successfully...")
        else:
            print("The file does not exist...")
    
    except Exception as err:
        print(f"An error occured as {err}")


def update_file():

    try:
        show_files_and_folders()
        
        name = input("tell me which file you want to update? ") 

        p = Path(name)

        if p.exists() and p.is_file():
            print("Press 1 for changing the name of your file...")
            print("Press 2 for overwriting the data of your file...")
            print("Press 3 for appending some content in your file...")

            res = int(input("Tell your response..."))

            if res == 1:
                name2 = input("Tell your new file name: ")
                p2 = Path(name2)
                p.rename(p2)

            if res == 2:
                with open(p, 'w') as fs:
                    data = input("Tell what you want to overwrite: ")
                    fs.write(data)

            if res == 3:
                with open(p, 'a') as fs:
                    data = input("Tell what you want to append: ")
                    fs.write(" " + data)
    
    except Exception as err:
        print(f"An error occured as {err}") 


def delete_file():
    show_files_and_folders()

    name = input("Tell me which file you want to delete...")

    p = Path(name)

    if p.exists() and p.is_file():
        os.remove(p)

        print("File removed successfully...")
    
    else:
        print("No such file exists...")
    

print("Press 1 for creating a file.")
print("Press 2 for reading a file.")
print("Press 3 for writing a file.")
print("Press 4 for deleting a file.")

check = int(input("please tell your response :-"))

if check == 1:
    create_file()

if check == 2:
    read_file()

if check == 3:
    update_file()

if check == 4:
    delete_file()
