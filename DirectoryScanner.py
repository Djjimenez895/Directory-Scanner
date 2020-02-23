import os
from FileStatistics import FileStatistics

def traverse_directories(dir):
    stats = FileStatistics()

    print("traversing directories")
    for root, dirs, files in os.walk(dir):
        path = root.split(os.sep)
        
        for file in files:
            print(file)
            file_extension = os.path.splitext(file)[1]

            if (file_extension in stats.file_frequency_dict):
                stats.file_frequency_dict[file_extension] += 1
            else:
                stats.file_frequency_dict[file_extension] = 1
            
            print("The file extension is: " + file_extension)

        for dir in dirs:
            print(dir)

    print(stats.file_frequency_dict)

def main():
    print("Please enter a directory:")
    directory = input()
    print(directory)
    traverse_directories(directory)

main()