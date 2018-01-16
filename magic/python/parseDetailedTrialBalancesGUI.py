from tkinter import *
from tkinter import filedialog
import os



theRoot = Tk()

the_input_files_list = []   # list[] of files to parse
the_output_file_name = ''
the_output_file_name_path = ''

# ***** FUNCTIONS *****


def input_file_button_click():
    theRoot.filename = filedialog.askopenfilename(initialdir="C:\\rsuinn\\projects\\meditechMagic\\data\\GL",
                                                     filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                                                     title="Choose a GL Audit Trail file"
                                                     )
    print(theRoot.filename)
    the_input_file_entry.delete(0,99)
    the_input_file_entry.insert(0, theRoot.filename) # display filename path in edit box
    the_input_file = the_input_file_entry.get()     # full path and filename
    print(the_input_file)

    global the_output_file_name
    the_output_file_name = 'tabDelim_' + os.path.basename(the_input_file)
    print(the_output_file_name)

# def input_folder_button_click():
#     the_folder = filedialog.askdirectory()  # no slash at end of path
#     print(the_folder)
#     the_input_folder_entry.insert(0, the_folder)


def output_folder_button_click():
    # the_folder = tkFileDialog.askopenfilename('C:\\rsuinn\\projects\\meditechMagic\\output\\GL')
    the_folder = filedialog.askdirectory(parent=theRoot, initialdir='C:\\rsuinn\\projects\\meditechMagic\\output\\GL', title='Please select a directory')

    # the_folder = filedialog.askdirectory()
    print(the_folder)
    the_output_folder_entry.delete(0,99)
    the_output_folder_entry.insert(0, the_folder)
    print(the_folder)
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
    the_output_file_name_path = the_output_folder_entry.get() + '/' + the_output_file_name
    theOutputFile = open(the_output_file_name_path, 'w')
    print(the_output_file_name_path)
    #theRoot.quit()

    with open(the_input_file_entry.get(),
              'r') as theInputFile:  # open the formatted Detail Trial Balance file.

        theGlAccountCount = 0
        theJournalLineCount = 0
        theDashedLine = True
        theGlAccount = ''
        theGlAccountName = ''
        theDelimiter = '\t'  # tab

        for theLine in theInputFile:
            if (theLine.find('GRAND TOTALS') != -1):
                break  # quit
            if (theLine.find('RUN DATE') != -1):  # ignore the run date so it's not confused with a journal date
                continue
            if (theLine.find('-------------------------------') != -1):
                theDashedLine = True  # reached end of an account
                theGlAccount = ''
                theGlAccountName = ''
                continue

            if (theDashedLine == True):
                theCorpNum = theLine[0:1]
                if (theCorpNum.isdigit()):
                    if (theLine[2] == '-'):
                        theLineList = theLine.split(' - ', 1)
                        theGlAccount = theLineList[0]
                        theGlAccountName = theLineList[1]
                        theGlAccountCount += 1
                        theDashedLine = False
                        continue

            # if the line has a date with slashes assume it's the detail journal lines
            if (len(theLine) > 32):
                if (theLine[25] == '/' and theLine[28] == '/'):
                    theJournal = theLine[12:22].strip()
                    theDate = theLine[22:31].strip()
                    theBatchNum = theLine[32:35].strip()
                    theEntry = theLine[36:41].strip()
                    theDebitAmount = theLine[44:56].strip().replace(',', '')
                    theCreditAmount = theLine[58:70].strip().replace(',', '')
                    theDescription = theLine[72:].strip()
                    # print(theGlAccount.strip() + '\t' + theGlAccountName.strip() + '\t' + theJournal + '\t' + theDate + '\t' + theBatchNum + '\t' + theEntry + '\t' + theDebitAmount + '\t' + theCreditAmount + '\t' + theDescription)
                    theOutputFile.write(
                        theGlAccount.strip() + '\t' + theGlAccountName.strip() + '\t' + theJournal + '\t' + theDate + '\t' + theBatchNum + '\t' + theEntry + '\t' + theDebitAmount + '\t' + theCreditAmount + '\t' + theDescription + '\n')
                    theJournalLineCount += 1

    print('Done parsing')
    print(theGlAccountCount, 'GL accounts in file including duplicates')

    theInputFile.close()
    theOutputFile.close()

# ***** MAIN CODE STARTS HERE *****


# create GUI controls
the_input_file_label = Label(theRoot, text='GL Detailed Audit Report file to Parse:')
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
