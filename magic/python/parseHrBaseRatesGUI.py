
# TO DO
# -- run date/time, run duration
import time
from tkinter import *
from tkinter import filedialog
import os

theRoot = Tk()

the_input_files_list = []   # list[] of files to parse
the_output_file_name = ''
the_output_file_name_path = ''

# ***** FUNCTIONS *****


def input_file_button_click():
    theRoot.filename = filedialog.askopenfilename(initialdir="C:\\rsuinn\\projects\\meditechMagic\\data\\HR",
                                                     filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                                                     title="Choose a HR Audit Trail file"
                                                     )
    the_input_file_entry.delete(0,99)
    the_input_file_entry.insert(0, theRoot.filename) # display filename path in edit box
    the_input_file = the_input_file_entry.get()     # full path and filename
    print(the_input_file)

    global the_output_file_name
    the_output_file_name = 'tabDelim_baserate_' + os.path.basename(the_input_file)

    global the_error_file_name
    the_error_file_name = 'errors_baserate_' + os.path.basename(the_input_file)
    print(the_output_file_name)
    print(the_error_file_name)

# def input_folder_button_click():
#     the_folder = filedialog.askdirectory()  # no slash at end of path
#     print(the_folder)
#     the_input_folder_entry.insert(0, the_folder)


def output_folder_button_click():
    # the_folder = tkFileDialog.askopenfilename('C:\\rsuinn\\projects\\meditechMagic\\output\\HR')
    the_folder = filedialog.askdirectory(parent=theRoot, initialdir='C:\\rsuinn\\projects\\meditechMagic\\output\\HR', title='Please select a directory')

    # the_folder = filedialog.askdirectory()
    the_output_folder_entry.delete(0,99)
    the_output_folder_entry.insert(0, the_folder)

    global the_error_file_name_path
    the_error_file_name_path = the_output_folder_entry.get() + '/' + the_error_file_name
    print(the_error_file_name_path)

    global the_output_file_name_path
    the_output_file_name_path = the_output_folder_entry.get() + '/' + the_output_file_name
    print(the_output_file_name_path)


def quit_button_click():
    theRoot.quit()


# def get_input_files():
#     # returns a list[file1, file2, ...] of .txt files
#     the_files_list = os.listdir(the_input_folder_entry.get())
#     for the_file in the_files_list:
#         if the_file.endswith(".txt"):
#             the_input_files_list.append(the_file)
#     print(the_input_files_list)


def parse():
    error_file = open(the_error_file_name_path, 'w')
    output_file = open(the_output_file_name_path, 'w')

    print(the_error_file_name_path)
    print(the_output_file_name_path)

    with open(the_input_file_entry.get(),
              'r') as input_file:  # open the formatted Detail Trial Balance file.

        theEmplCount = 0
        thePayroll = ''
        theSSN = ''
        theName = ''
        theEmplNum = ''
        theEmplType = ''
        thePosition = ''
        theJobCode = ''
        theDep = ''
        theHireDate = ''

        output_file.write('EMPLOYEE_NUMBER' + '\t' + 'CURRENT_AMOUNT' + '\t' + 'CURRENT_DATE' + '\t' + 'CURRENT_REASON' + '\t' + 'PREVIOUS_AMOUNT' + '\t' + 'PREVIOUS_DATE' + '\t' + 'PREVIOUS_REASON' + '\n')

        for theLine in input_file:
            theField = theLine[:14]

            # %%%% STOP if empl # found more than once for same employee
            if (theField.find('EMPL #:') != -1):
                #if (theEmplNum and (theEmplNum == theLine[16:46].strip() ) ):
                #    raise ValueError
                theEmplNum = theLine[16:46].strip()
                theEmplCount += 1
                continue

            if ( (theField.find('BASE RATE:') != -1) and (len(theLine) > 49)):
                theDataList1 = theLine[16:46].strip().split('  ')
                theDataList2 = theLine[48:].strip().split('  ')

                if (theDataList1 and theDataList2):
                    if (len(theDataList1) >= 2):
                        theDate1 = theDataList1[1]
                    else:
                        theDate1 = ''

                    theAmount1 = theDataList1[0]

                    if (len(theDataList1) == 3):
                        theReason1 = theDataList1[2]
                    else:
                        theReason1 = ''

                    if (len(theDataList2) >= 2):
                        theDate2 = theDataList2[1]
                    else:
                        theDate2 = ''

                    theAmount2 = theDataList2[0]

                    if (len(theDataList2) == 3):
                        theReason2 = theDataList2[2]
                    else:
                        theReason2 = ''

                    if (theDate1 and theDate2):
                        try:
                            if (time.strptime(theDate1,'%m/%d/%y') and time.strptime(theDate2,'%m/%d/%y')): # use a try() block
                                #print(theEmplNum + '\t' + theAmount1 + '\t' + theDate1 + '\t' + theReason1 + '\t' + theAmount2 + '\t' + theDate2 + '\t' + theReason2)
                                output_file.write(theEmplNum + '\t' + theAmount1 + '\t' + theDate1 + '\t' + theReason1 + '\t' + theAmount2 + '\t' + theDate2 + '\t' + theReason2 + '\n')
                        except ValueError:
                            error_file.write('Exception caught|ValueError|' + theEmplNum + '|' + theDate1 + '|' + theDate2 +  '\n')


    print('Done parsing')
    print(theEmplCount, 'employees in file.')

    input_file.close()
    output_file.close()
    error_file.close()


# ***** MAIN CODE STARTS HERE *****


# create GUI controls
the_input_file_label = Label(theRoot, text='HR Employee Audit Report file to Parse:')
the_input_file_entry = Entry(theRoot)
the_input_file_button = Button(theRoot, text='Browse...', command=input_file_button_click)

# the_input_folder_label = Label(theRoot, text='Folder for Input Files:')
# the_input_folder_entry = Entry(theRoot)
# the_input_folder_button = Button(theRoot, text='Browse...', command=input_folder_button_click)

the_output_folder_label = Label(theRoot, text='Folder for Output Files:')
the_output_folder_entry = Entry(theRoot)
the_output_folder_button = Button(theRoot, text='Browse...', command=output_folder_button_click)

run_button = Button(theRoot, text='Parse Files', command=parse)
quit_button = Button(theRoot, text='Quit', command=quit_button_click)

# align controls using a grid
the_input_file_label.grid(row=0, column=0, sticky=E)   # sticky=E is left justify (East) the text.
the_input_file_entry.grid(row=0, column=1)
the_input_file_button.grid(row=0, column=2)

# the_input_folder_label.grid(row=0, column=0, sticky=E)   # sticky=E is left justify (East) the text.
# the_input_folder_entry.grid(row=0, column=1)
# the_input_folder_button.grid(row=0, column=2)

the_output_folder_label.grid(row=1, column=0, sticky=E)
the_output_folder_entry.grid(row=1, column=1)
the_output_folder_button.grid(row=1, column=2)

run_button.grid(row=3, column=1)
quit_button.grid(row=3, column=2)

theRoot.mainloop()  # display GUI until user closes dialog box or clicks Quit button