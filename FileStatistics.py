class FileStatistics:
    """This class defines an object that keeps track
       of the frequency of different file types in the directories
       traversed. 
    """
    def __init__(self):
        print("Creating Statistics object")
        self.file_frequency_dict = {} # Dictionary for storing file extensions and their number of occurences
        self.total_files = 0 # total number of files in the directories traversed

    """ This method is for printing all the file types and how many times they occur
    """
    def print_file_frequences():
        for key,value in self.file_frequency_dict.items():
            print(key + " => " + value)


