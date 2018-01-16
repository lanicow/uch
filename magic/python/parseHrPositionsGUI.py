
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
    the_output_file_name = 'tabDelim_position_' + os.path.basename(the_input_file)
    print(the_output_file_name)

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

    global the_output_file_name_path
    the_output_file_name_path = the_output_folder_entry.get() + '/' + the_output_file_name
    print(the_output_file_name_path)
    # global the_output_file_name_path
    # print(the_output_file_name_path)

def error_folder_button_click():
    the_folder = filedialog.askdirectory()
    print(the_folder)
    the_error_folder_entry.delete(0,99)
    the_error_folder_entry.insert(0, the_folder)


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
    # theErrorFile = open(theDataRoot + 'output/hrAuditTrail-errors.txt', 'w')
    theOutputFile = open(the_output_file_name_path, 'w')
    print(the_output_file_name_path)

    with open(the_input_file_entry.get(),
              'r') as theInputFile:  # open the formatted Detail Trial Balance file.

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

        theOutputFile.write('EMPLOYEE_NUMBER' + '\t' + 'CURRENT_POSITION' + '\t' + 'CURRENT_POSITION_DATE' + '\t' + 'PREVIOUS_POSITION' + '\t' + 'PREVIOUS_POSITION_DATE' + '\t' + 'EDIT_DATE' + '\t' + 'EDIT_TIME' + '\t' + 'EDIT_USER' + '\n')
        #             print('EMPLOYEE_NUMBER' + '\t' + 'CURRENT_POSITION' + '\t' + 'CURRENT_POSITION_DATE' + '\t' + 'PREVIOUS_POSITION' + '\t' + 'PREVIOUS_POSITION_DATE' + '\t' + 'EDIT_DATE' + '\t' + 'EDIT_TIME' + '\t' + 'EDIT_USER')

        for theLine in theInputFile:

            if (theLine.strip() == ''):
                continue

            theField = theLine[:14]
            # %%%% STOP if empl # found more than once for same employee
            if (theField.find('EMPL #:') != -1):
                #if (theEmplNum and (theEmplNum == theLine[16:46].strip() ) ):
                #    raise ValueError
                theEmplNum = theLine[16:46].strip()
                theEmplCount += 1
                continue

            if (theEmplNum == ''):
                continue

            if ( (theLine.find('DATE:') != -1) and (theLine.find('TIME:') != -1) and (theLine.find('USER:') != -1) ):
                theEditDate = theLine[6:14]
                theEditTime = theLine[23:27]
                theEditUser = theLine[36:].strip()

                for theLine in theInputFile:
                    if (theLine.strip() == ''):
                        continue

                    # the dashes signify the end of an employees audit history and the start of the next employee.
                    if (theLine.find('---------------------------------------------------------------------------') != -1):
                        theEmplNum = ''
                        break;

                    if ( (theLine.find('DATE:') != -1) and (theLine.find('TIME:') != -1) and (theLine.find('USER:') != -1) ):
                        theEditDate = theLine[6:14]
                        theEditTime = theLine[23:27]
                        theEditUser = theLine[36:].strip()
                        continue

                    theField = theLine[:14]
                    if ( (theField.find('JOB CODE:') != -1) and (len(theLine) > 49) ):
                        theCurJobCode = theLine[16:46].strip()
                        thePrevJobCode = theLine[48:].strip()
                        #print(theEmplNum + '\t' + theCurJobCode + '\t' + thePrevJobCode)

                    if ( (theField.find('POSITION:') != -1) and (len(theLine) > 49) ):
                        theDataList1 = theLine[16:46].strip().split('  ')
                        theDataList2 = theLine[48:].strip().split('  ')
                        theCurPosition = ''
                        theCurPositionDate = ''
                        thePrevPosition = ''
                        thePrevPositionDate = ''

                        if (theDataList1):
                            theCurPosition = theDataList1[0]
                            if (len(theDataList1) == 2):
                                theCurPositionDate = theDataList1[1]

                        if (theDataList2):
                            thePrevPosition = theDataList2[0]
                            if(len(theDataList2) == 2):
                                thePrevPositionDate = theDataList2[1]

                        #             print(theEmplNum + '\t' + theCurPosition + '\t' + theCurPositionDate + '\t' + thePrevPosition + '\t' + thePrevPositionDate + '\t' + theEditDate + '\t' + theEditTime + '\t' + theEditUser)
                        theOutputFile.write(theEmplNum + '\t' + theCurPosition + '\t' + theCurPositionDate + '\t' + thePrevPosition + '\t' + thePrevPositionDate + '\t' + theEditDate + '\t' + theEditTime + '\t' + theEditUser + '\n')

    print('Done parsing')
    print(theEmplCount, 'employees in file.')

    theInputFile.close()
    theOutputFile.close()
    # theErrorFile.close()


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

the_error_folder_label = Label(theRoot, text='Folder for Error Files:')
the_error_folder_entry = Entry(theRoot)
the_error_folder_button = Button(theRoot, text='Browse...', command=error_folder_button_click)

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

the_error_folder_label.grid(row=2, column=0, sticky=E)
the_error_folder_entry.grid(row=2, column=1)
the_error_folder_button.grid(row=2, column=2)

run_button.grid(row=3, column=1)
quit_button.grid(row=3, column=2)

theRoot.mainloop()  # display GUI until user closes dialog box or clicks Quit button