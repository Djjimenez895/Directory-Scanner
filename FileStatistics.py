class FileStatistics:
    """
    This class defines an object that keeps track
    of the frequency of different file types in the directories
    traversed. 

    TODO: Add a method that finds the most commonly occurring file type and saves it into a variable. 
    """
    def __init__(self):
        print("Creating Statistics object")
        self.file_frequency_dict = {} # Dictionary for storing file extensions and their number of occurences
        self.total_files = 0 # total number of files in the directories traversed
        self.most_common_ext = "" # stores the most common file extension from the directories scanned


    """ 
        Description: This method is for printing all the file types and how many times they occur
        Input: N/A
        Return value: N/A
    """
    def print_file_frequences():
        for key,value in self.file_frequency_dict.items():
            print(key + " => " + value)

    """ 
        Description: This method is for printing the most common file extension
        Input: N/A
        Return value: A tuple containing the key, value pair for the most commonly occurring file extension
    """
    def find_most_common_ext():
        self.most_common_ext = max(self.file_frequency_dict.items(), key=lambda k: k[1])
        return self.most_common_ext


