# TO DO
# -- add try/catch blocks
# -- add file dialog boxes
# -- clean up code into functions

theOutputFile = open('C:/rsuinn/projects/uch/magic/data/output/trialBalance-JAN 86-DEC 86-tabDelim.txt', 'w')
with open('C:/rsuinn/projects/uch/magic/data/trialBalance-JAN 86-DEC 86.txt', 'r') as theInputFile: # open the formatted Detail Trial Balance file.

    theGlAccountCount = 0
    theJournalLineCount = 0
    theDashedLine = True
    theGlAccount = ''
    theGlAccountName = ''
    theDelimiter = '\t' # tab
    
    for theLine in theInputFile:
        if (theLine.find('GRAND TOTALS') != -1):
            break # quit
        if (theLine.find('RUN DATE') != -1): # ignore the run date so it's not confused with a journal date
            continue
        if (theLine.find('-------------------------------') != -1):
            theDashedLine = True # reached end of an account
            theGlAccount = ''
            theGlAccountName = ''
            continue


        if (theDashedLine == True): 
            theCorpNum = theLine[0:1]
            if (theCorpNum.isdigit()):
                if(theLine[2] == '-'):
                    theLineList = theLine.split(' - ',1)
                    theGlAccount = theLineList[0]
                    theGlAccountName = theLineList[1]
                    theGlAccountCount += 1
                    theDashedLine = False
                    continue

        # if the line has a date with slashes assume it's the detail journal lines
        if (len(theLine) > 32):
            if (theLine[25] == '/' and theLine[28] == '/'):
                theJournal = theLine[12:19].strip()
                theDate = theLine[22:31].strip()
                theBatchNum = theLine[32:35].strip()
                theEntry = theLine[36:41].strip()
                theDebitAmount = theLine[44:56].strip()
                theCreditAmount = theLine[58:70].strip()
                theDescription = theLine[72:].strip()
                #print(theGlAccount.strip() + '\t' + theGlAccountName.strip() + '\t' + theJournal + '\t' + theDate + '\t' + theBatchNum + '\t' + theEntry + '\t' + theDebitAmount + '\t' + theCreditAmount + '\t' + theDescription)
                theOutputFile.write(theGlAccount.strip() + '\t' + theGlAccountName.strip() + '\t' + theJournal + '\t' + theDate + '\t' + theBatchNum + '\t' + theEntry + '\t' + theDebitAmount + '\t' + theCreditAmount + '\t' + theDescription + '\n')
                theJournalLineCount += 1


print(theGlAccountCount, 'GL accounts in file including duplicates')

theInputFile.close()
theOutputFile.close()
