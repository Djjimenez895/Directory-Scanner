import os
from FileStatistics import FileStatistics
import matplotlib.pyplot as plt
import numpy as np

def graph_files(stats):
    plt.style.use('seaborn')
    x_axis_values = list(stats.file_frequency_dict.keys()) # File extensions
    y_axis_values = list(stats.file_frequency_dict.values()) # Number of occurences for a file extension

    x_pos = [i for i, a in enumerate(x_axis_values)]

    plt.bar(x_pos, y_axis_values, color='green')
    plt.xlabel("File Extensions")
    plt.ylabel("Number of Files")
    plt.title("File Extension Occurences")

    plt.xticks(x_pos, x_axis_values)
    plt.show()


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

    # print(stats.file_frequency_dict)
    graph_files(stats)


def main():
    print("Please enter a directory:")
    directory = input()
    print(directory)
    traverse_directories(directory)

main()