import sys
import csv
import filecmp
import unittest

col_names = []
f_names = []
def main():
    #ensure that there are at least 2 given csv files
    if(len(sys.argv) < 3):
        print("Incorrect number of arguments. \nMust be at least 2 csv files")
        sys.exit()

    #get the names of the files from stdin
    for name in sys.argv[1:]:
        f_names.append(name)
    
    #fill the new csv file with new contents
    fill_file(f_names)


def fill_file(file_names):
    #create the header for the new csv file
    create_header(file_names)
    #input contents from given files
    for name in file_names:
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
                with open('combine.csv', 'a') as csvfile:
                    writer = csv.writer(csvfile, doublequote=False, escapechar='\\', quoting=csv.QUOTE_ALL)
                    writer.writerow(out_row)
                    csvfile.close()

def create_header(file_names):
    #for each file input
    for name in file_names:
        #get columns in file
        with open(name, newline='') as f:
            reader = csv.reader(f)
            #get the header of the current file
            curr_header = next(reader)
            #pass current header to the add header method
            add_header(curr_header)

    #append a new column to header for the file name
    col_names.append("filename")
    #write the header to the new combine file
    with open('combine.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, doublequote=False, escapechar='\\', quoting=csv.QUOTE_ALL)
        writer.writerow(col_names)
        csvfile.close()

def add_header(curr_header):
    #for every name in the given header
    for name in curr_header:
        #if the name is not in the current header
        if(name not in col_names):
            #append name to header
            col_names.append(name)

class TestCombine(unittest.TestCase):
    def test_combine(self):
        test_names = ['test1.csv', 'test2.csv']
        fill_file(test_names)
        self.assertTrue(filecmp.cmp('combine.csv', 'testRes.csv', shallow=False), "Files not equal.")


if __name__ == '__main__':
    main()
    #unittest.main()