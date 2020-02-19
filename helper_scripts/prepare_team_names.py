
with open('../Kwaliteitskader deelnemers.txt', 'r') as reader:

    with open('../teamnamen.txt', 'w') as writer:

        for line in reader:
            leftside_corrected = line.replace('_', ';', 2)
            last_semicolon = leftside_corrected.rfind(';')
            rightside = leftside_corrected[last_semicolon: ]
            rightside_corrected = rightside.replace('_', ';')
            full_line_corrected = leftside_corrected[:last_semicolon] + rightside_corrected

            writer.write(full_line_corrected)
