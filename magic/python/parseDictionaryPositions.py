# TO DO
# -- add try/catch blocks
# -- add file dialog boxes
# -- clean up code into functions

theOutputFile = open('C:/randy/data-uch/output/dictionary-positions-tabDelim.txt', 'w')
with open('C:/randy/data-uch/dictionary-position.txt', 'r') as theInputFile: # open the formatted Detail Trial Balance file.

    theOutputFile.write('MNEMONIC' + '\t' + 'DESCRIPTION' + '\n')
    theMnemonicCount = 0
        
    for theLine in theInputFile:

        if (len(theLine.strip()) == 0):    # ignore blank lines
            continue

        if (theLine[:19].strip() == 'POSITION #'): # ignore the column header rows
            continue
                
        thePositionNum = theLine[:19].strip()
        theTitle = theLine[23:58].strip()

        if (thePositionNum == '' or theTitle == ''):
            continue
        
        #print(theGlAccount.strip() + '\t' + theGlAccountName.strip() + '\t' + theJournal + '\t' + theDate + '\t' + theBatchNum + '\t' + theEntry + '\t' + theDebitAmount + '\t' + theCreditAmount + '\t' + theDescription)
        theOutputFile.write(thePositionNum + '\t' + theTitle.strip() + '\n')
        theMnemonicCount += 1

print(theMnemonicCount, 'mnemonics parsed.')

theInputFile.close()
theOutputFile.close()


