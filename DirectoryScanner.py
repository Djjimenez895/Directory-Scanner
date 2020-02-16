import os

def traverse_directories(dir):
    print("traversing directories")
    for root, dirs, files in os.walk(dir):
        path = root.split(os.sep)
        
        for file in files:
            print(file)

        for dir in dirs:
            print(dir)

def main():
    print("Please enter a directory:")
    directory = input()
    print(directory)
    traverse_directories(directory)

main()