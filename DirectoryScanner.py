import os
from FileStatistics import FileStatistics
import matplotlib.pyplot as plt
import numpy as np

'''
    Description: Uses matplob lib to graph the data passed in as input

    Input: stats - a FileStatistics object that contains a dictionary with the file extensions (the key) and the number of files with that extension (the value). 
    Return value: N/A
'''
def graph_files(stats):
    # TODO: Add a label to each individual bar in the graph
    # TODO: Document the methods
    # TODO: Add feature that will keep asking for a directory if the one entered isn't a directory. 
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


'''
    Description: Traverses the directory passed in as an argument and creates a FileStatistics 
    object that uses a dictionary to keep track of the file extensions (keys) found in the directory given (and all subdirectories) 
    and the number of times that file extension occurs (values).

    Input: A string that contains the directory to traverse. The algorithm will also traverse subdirectories of the given directory. 
    Return value: N/A
'''
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

'''
    Description: This is the main function for running the program; use this function for running the application. 

    Input: N/A
    Return: N/A
'''
def main():
    print("Please enter a directory:")
    directory = input()
    print(directory)
    traverse_directories(directory)

main()