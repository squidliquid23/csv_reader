import csv

#class csv_creation:
   # def __init__(self, clinic, amount, conf_code):
       # self.clinic = clinic
       # self.amount = amount
       # self.conf_code = conf_code

#read the data - but dont store it as a list that can be used in other data
def _csv_reader():
    f = open("neely_debt.csv") 
    csv_f = csv.reader(f)
    for row in csv_f:
        clinic, amount, conf_code = row
        print("Institute/Clinic: {: ^115}, Amount: {: <15}, Confirmation #: {}".format(clinic, amount, conf_code))
    f.close()


# create a list from the CSV file that contains the Clinic, Amount and Confirmation Code 
def _csv_store():
    #intializes the variables/lists
    clinic_list = []
    amount_list = []
    conf_codelist = []
    i = 0
    #opens csv file and stores data wisely
    f = open("neely_debt.csv") 
    csv_f = csv.reader(f)
    for row in csv_f:
        clinic, amount, conf_code = row
        #append each variation of clinic, amount and conf_code to the lists
        clinic_list.append(clinic)
        amount_list.append(amount)
        conf_codelist.append(conf_code)
        #dont forget to close her up!
    f.close()
    #while loop -> cycles through the list and is formatted to perfection
    while i < len(clinic_list):
        print("Clinics: {:>45} Amount: {:<15} Confirmation #: {}".format(clinic_list[i], amount_list[i], conf_codelist[i]))
        i += 1
    #return your dictionary, fam!
    return clinic_list, amount_list, conf_codelist
    
    


#def list_clinic(clinic_list):
   # while i < len(clinic_list):
       # print("Clinics: {:>45}".format(clinic_list[i]))
        #i += 1
    
def main():
   # _csv_reader()
    _csv_store()
    #list_clinic(clinic_list)
    
    
main()

