import csv
"""Sebastian Garcia, August 2018
    Made for the Professional Lifeguard Association
    to parse and anonymize applications."""

csv_file = 'plf.csv'
txt_file = 'parsed_app.txt'
#hard coded csv and .txt file


candidateCounter = -1 
first_row = True
with open(txt_file, "w") as my_output_file:
    with open(csv_file, "r") as my_input_file:
         for row in csv.reader(my_input_file):
         	candidateCounter+=1
         	my_output_file.write ('\n')
         	my_output_file.write("Candidate " + str(candidateCounter) + '\n')
         	if first_row == False:
         		for x in range (0,len(topics)):
         			#x is index within the row[], acessing each individual cell
         			#formats it
         			my_output_file.write (topics[x] + ": " + '\n')
         			#indents the essy questions
         			if((x == len(topics)-1) or (x == (len(topics)-2))): my_output_file.write (" 	")
         			my_output_file.write ( row[x] + '\n' + '\n')
         	if first_row == True:
         		#sentinel clause that watches for first row to populate topics[]
         		topics = row
         		first_row = False	
         		continue
         	continue
    my_output_file.close()
