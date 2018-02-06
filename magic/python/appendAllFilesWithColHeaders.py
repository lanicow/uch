# Purpose: reads all .txt files in a folder to create a single data file to be imported into a SQL table.
# Author: randy suinn
# python: v3.x
# Notes:
# -- assumes the 1st line (ie line 1) of each input file is the column header.
# -- only .txt files will be read.

import os

the_input_file_list = []
the_folder_path = r'C:\rsuinn\projects\meditechMagic\output\HR' # the full path to the folder containing the .txt files to be read.


def get_file_list():
    the_file_list = os.listdir(the_folder_path)  # get a list of files and folder names
    for the_file in the_file_list:
        the_full_path = os.path.join(the_folder_path, the_file)
        if os.path.isdir(the_full_path):
            continue  # ignore the folders
        if the_file.endswith('.txt'):
            the_input_file_list.append(the_full_path)

    return the_input_file_list
# end function


the_input_file_list = get_file_list()

if len(the_input_file_list) > 0:

    # the full  path to a .txt file which will contain all the data from the input files.
    with open(r'C:\rsuinn\projects\meditechMagic\output\HR-sqlImportFile\sqlImport.txt', 'w') as the_output_file:    # append all file's data to this single file.
        the_num_files_read = 0
        the_have_column_header = False

        for the_full_path in the_input_file_list:
            the_num_files_read += 1
            # the_full_path = os.path.join(the_folder_path, the_file)

            with open(the_full_path, 'r') as the_input_file:

                the_line_count = 0
                for the_line in the_input_file:
                    the_line_count += 1
                    # ignore the 1st line (the column headers) if it's already been written to the output file.
                    if the_have_column_header and the_line_count == 1:  # assumes the 1st line is the column header in every file.
                        continue
                    the_have_column_header = True
                    the_output_file.write( the_line )
            print('FILE:', the_full_path, '| LINES READ:', the_line_count)

print ('TOTAL FILES READ:', the_num_files_read)
