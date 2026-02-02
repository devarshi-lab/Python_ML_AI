import os

class SearchFIleWithExtension:

    def __init__(self,directory,extension):
        self.directory  = directory
        self.extension = extension
    
    def validateDirectory(self):
        if(os.path.exists(self.directory) and os.path.isdir(self.directory)):
            return True
        return False
    
    def getFilesWithExtension(self):
        if(self.validateDirectory()):
            for folders,subfolder,files in os.walk(self.directory):
                for file in files:
                    print(os.path.splitext(file))
                    ext = file.split(".")
                    if len(ext) > 1 :
                        if ext[-1:][0] == self.extension:
                            print(file)


def main():
    """1.Design automation script which accept directory name and file extension from user. Display all files with that extension.
Usage : DirectoryFileSearch.py “Demo” “.txt”
Demo is name of directory and .txt is the extension that we want to search."""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    fileName = input("Enter the name of directory : ")
    ext = input("Enter the extension :  ")
    dobj = SearchFIleWithExtension(fileName,ext)
    dobj.getFilesWithExtension()


if __name__ == "__main__":
    main()