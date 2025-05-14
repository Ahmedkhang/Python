class Hospital:
    def __init__(self,name,location):
        self.name = name
        self.location = location
        self.patients = []
        self.doctors =  []
    def add_patient(self, patient):
        self.patients.append(patient)
    def add_doctor(self,doctor):
        self.doctors.append(doctor)        
class Patient:
    def __init__(self,patient_name,patient_age,patient_id,patient_disease):
        self.patient_name = patient_name
        self.patient_age = patient_age
        self.patient_id = patient_id
        self.patient_disease = patient_disease
    def __str__(self):

        return f"----------- Patient Details -----------\n\nPatient Name: {self.patient_name}\nAge: {self.patient_age}\nID: {self.patient_id}\nDisease: {self.patient_disease}"    

class Doctor:
    def __init__(self,doctor_name,doctor_specialization,doctor_id):
        self.doctor_name = doctor_name
        self.doctor_specialization = doctor_specialization
        self.doctor_id = doctor_id
    def __str__(self):
        
        return f"----------- Doctor Details -----------\n\nDoctor Name: {self.doctor_name}\nSpecialization: {self.doctor_specialization}\nID: {self.doctor_id}"    
    def medicine_from_doctor(self,medicine,patient):
        print(f"Medicine prescribed by {self.doctor_name} ({self.doctor_specialization}): {medicine} to {patient.patient_name}")
            
hospital = Hospital("City Hospital", "Karachi")

print(f"Hospital Name: {hospital.name}\nLocation: {hospital.location}")
def add_new_patient():
    while True:
        patient_name = input("Enter patient name: ")
        patient_age = int(input("Enter patient age: "))
        patient_id = int(input("Enter patient ID: "))
        patient_disease = input("Enter patient disease: ")
        
        patient = Patient(patient_name,patient_age,patient_id,patient_disease)
        hospital.add_patient(patient)
        print(patient)
        
        more_patients = input("Do you want to add more patients? (yes/no): ").lower()
        if more_patients == "no":
            break
        elif more_patients != "yes":
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue
  
def add_new_doctor():
    while True:
        doctor_name = input("Enter doctor name: ")
        doctor_specialization = input("Enter doctor specialization: ")
        doctor_id = int(input("Enter doctor ID: "))
        doctor = Doctor(doctor_name, doctor_specialization, doctor_id)
        
        hospital.add_doctor(doctor)             
        print(doctor)  
        more_doctors = input("Do you want to add more doctors? (yes/no): ").lower()
        if more_doctors == "no":
            break
        elif more_doctors != "yes":
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue
while True:
    print("\n\nWelcome to the Hospital Management System")

    choice = input("\n1-Add New Patient\n2-Add New Doctor\n3-All Patients\n4-All Doctors\n5-Exit\nChoose between 1-5: ")
    if choice == "1":
        add_new_patient()
    elif choice == "2":
        add_new_doctor()    
    elif choice == "3":
        if hospital.patients:
            for hospital.patients in hospital.patients:
                print(hospital.patients)
        else:
            print("No patients found.")        
    elif choice == "4":
        if hospital.doctors:
            for hospital.doctors in hospital.doctors:
                print(hospital.doctors)
        else:
            print("No doctors found.")  
    elif choice == "5":
        print("Exiting the system.")
        break        
    else:
        print("Invalid choice. Please try again.")        