
the_output_file = open(r'C:\rsuinn\projects\meditechMagic\output\AP\dictionaries\tabDelim_dictionary-vendors-summary.txt', 'w')
with open(r'C:\rsuinn\projects\meditechMagic\output\AP\dictionaries\dictionary-vendors-summary.txt', 'r') as the_input_file: # open the formatted Detail Trial Balance file.

    the_output_file.write('NAME' + '\t' + 'ACTIVE' + '\t' + 'NUMBER' + '\t' + 'MNEMONIC' + '\t' + 'BANK_ACC' + '\t' + 'TERMS' + '\n')
    the_mnemonic_count = 0
    for the_line in the_input_file:
        if (the_line[:10].strip() == 'NAME'): # skip over the column headers
            continue
        if the_line.strip().find('All Accounts') != -1: # skip over the report title
            continue
        if len(the_line.strip() ) == "":   # skip over blank lines
            continue

        if len(the_line) > 10:
            the_name = the_line[:34].strip()
            the_active = the_line[39].strip()
            the_number = the_line[45:55].strip()
            the_mnemonic = the_line[59:68].strip()
            the_bank_acc = the_line[72:81].strip()
            the_terms = the_line[85:].strip()
            the_output_file.write(the_name + '\t' + the_active + '\t' + the_number + '\t' + the_mnemonic + '\t' + the_bank_acc + '\t' + the_terms + '\n')
            the_mnemonic_count += 1

print(the_mnemonic_count, 'mnemonics in file.')

the_input_file.close()
the_output_file.close()
