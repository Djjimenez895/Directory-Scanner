import os
from FileStatistics import FileStatistics
import matplotlib.pyplot as plt
import numpy

def graph_files(stats):
    graph_fig = plt.figure()
    graph_axes = graph_fig.add_axes([0, 0, 1, 1])
    file_exts = list(stats.file_frequency_dict.keys())
    extension_freq = list(stats.file_frequency_dict.values())
    graph_axes.bar(file_exts, extension_freq)
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

    print(stats.file_frequency_dict)
    graph_files(stats)

def main():
    print("Please enter a directory:")
    directory = input()
    print(directory)
    traverse_directories(directory)

main()