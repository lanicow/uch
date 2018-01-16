# TO DO
# -- add try/catch blocks
# -- add file dialog boxes
# -- clean up code into functions

theOutputFile = open('C:/randy/data-uch/output/dictionary-jobCode-tabDelim.txt', 'w')
with open('C:/randy/data-uch/dictionary-jobCode.txt', 'r') as theInputFile: # open the formatted Detail Trial Balance file.

    theOutputFile.write('MNEMONIC' + '\t' + 'DESCRIPTION' + '\n')
    theMnemonicCount = 0
    for theLine in theInputFile:
        if (theLine[:8] == 'MNEMONIC'): # skip over the column headers
            continue
                
        if (len(theLine) > 13):        
            if (theLine[1] != ' ' and theLine[13] != ' '):
                theMnemonic = theLine[:13].strip()
                theDescription = theLine[13:].strip()
                #print(theGlAccount.strip() + '\t' + theGlAccountName.strip() + '\t' + theJournal + '\t' + theDate + '\t' + theBatchNum + '\t' + theEntry + '\t' + theDebitAmount + '\t' + theCreditAmount + '\t' + theDescription)
                theOutputFile.write(theMnemonic + '\t' + theDescription.strip() + '\n')
                theMnemonicCount += 1

print(theMnemonicCount, 'job code mnemonics in file.')

theInputFile.close()
theOutputFile.close()


