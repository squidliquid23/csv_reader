import csv
import os

#class for the CSV reader
class CSV_ReadingMachine():
    #read the data - but store it as a list that can be used in other data
    def __init__(self, clinic_list = [], amount_list = [], conf_codelist = []):
        self.clinic_list = clinic_list
        self.amount_list = amount_list
        self.conf_codelist = conf_codelist



    def _csv_reader(self, csv_file):
        f = open(csv_file) 
        csv_f = csv.reader(f)
        for row in csv_f:
            clinic, amount, conf_code = row

            #feel free to change these formatting rules here, was for personal data
            #centers the Institute category and separates by 115 spaces
            #pushes amount to the left with 15 spaces open on the right
            print("Institute/Clinic: {: ^115}, Amount: {: <15}, Confirmation #: {}".format(clinic, amount, conf_code))
        f.close()


    # create a list from the CSV file that contains the Clinic, Amount and Confirmation Code 
    def _csv_store(self, csv_file):
        #initializes i variable for the loop
        i = 0
        #opens csv file and stores data wisely
        f = open(csv_file) 
        csv_f = csv.reader(f)
        for row in csv_f:
            #initializing
            clinic, amount, conf_code = row
            #append each variation of clinic, amount and conf_code to the lists
            self.clinic_list.append(clinic)
            self.amount_list.append(amount)
            self.conf_codelist.append(conf_code)
            #dont forget to close her up!
        f.close()
        #while loop -> cycles through the list and is formatted to perfection
        while i < len(self.clinic_list):
            print("Clinics: {:>45} Amount: {:<15} Confirmation #: {}".format(self.clinic_list[i],self.amount_list[i], self.conf_codelist[i]))
            i += 1
        
#assigns value to 'csv_file' based on user input
csv_file = input("Enter the csv file: ")
#return the file name and the file extension as a list (for example: "somethingcsv", ".csv")
csv_fileext = os.path.splitext(csv_file)
#checks that what you entered has a '.csv' extension, if not keep trying again!
if not csv_fileext[1] == ".csv":
    print("Heyyo! Wake up! That is not a csv file :( ")
    csv_file = input("Pwetty please re-enter the csv file name: ")
else: pass


    
u = CSV_ReadingMachine()
u._csv_reader(csv_file)
u._csv_store(csv_file)

