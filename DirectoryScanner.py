import os

def traverse_directories(dir):
    print("traversing directories")
    for root, dirs, files in os.walk(dir):
        path = root.split(os.sep)
        
        for file in files:
            print(file)
            file_extension = os.path.splitext(file)
            print("The file extension is: " + file_extension[1])

        for dir in dirs:
            print(dir)

def main():
    print("Please enter a directory:")
    directory = input()
    print(directory)
    traverse_directories(directory)

main()