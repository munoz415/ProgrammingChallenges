import sys
import csv

col_names = []
def main():
    #ensure that there are at least 2 given csv files
    if(len(sys.argv) < 3):
        print("Incorrect number of arguments. \nMust be at least 2 csv files")
        sys.exit()
    
    #create the header for the new csv file
    create_header()

    #fill the new csv file with new contents
    fill_file()


def fill_file():
    #input contents from given files
    for name in sys.argv[1:]:
        #get current file name
        split_name = name.split("/")
        f_name = split_name[-1]
        #read from file
        with open(name, newline='') as f:
            reader = csv.reader(f)
            #set the header aside as it was previously used
            curr_header = next(reader)
            #for every row in the file
            for file_row in reader:
                #create a new row to input in new file
                out_row = file_row
                #append the name of the current file
                out_row.append(f_name)
                #append row to new csv file
                print(out_row)

def create_header():
    #for each file input
    for name in sys.argv[1:]:
        #get columns in file
        with open(name, newline='') as f:
            reader = csv.reader(f)
            #get the header of the current file
            curr_header = next(reader)
            #pass current header to the add header method
            add_header(curr_header)

    #append a new column to header for the file name
    col_names.append("filename")
    print(col_names)

def add_header(curr_header):
    #for every name in the given header
    for name in curr_header:
        #if the name is not in the current header
        if(name not in col_names):
            #append name to header
            col_names.append(name)


if __name__ == '__main__':
    main()