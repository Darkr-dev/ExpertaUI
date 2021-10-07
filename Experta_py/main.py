# Autor principal: ronak-07
# Adaptado por: Jorge E. Hernández
from experta import *
import tkinter as tk

diseases_list = []  # Lista enfermedades
diseases_symptoms = []  # Sintomas de enfermedades
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}


def preprocess():
    global diseases_list, diseases_symptoms, symptom_map, d_desc_map, d_treatment_map
    diseases = open("diseases.txt")
    diseases_t = diseases.read()
    diseases_list = diseases_t.split("\n")
    diseases.close()
    for disease in diseases_list:
        disease_s_file = open("Disease symptoms/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        s_list = disease_s_data.split("\n")
        diseases_symptoms.append(s_list)
        symptom_map[str(s_list)] = disease
        disease_s_file.close()
        disease_s_file = open("Disease descriptions/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_desc_map[disease] = disease_s_data
        disease_s_file.close()
        disease_s_file = open("Disease treatments/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_treatment_map[disease] = disease_s_data
        disease_s_file.close()


def identify_disease(*arguments):
    symptom_list = []
    for symptom in arguments:
        symptom_list.append(symptom)
    # Handle key error
    return symptom_map[str(symptom_list)]


def get_details(disease):
    return d_desc_map[disease]


def get_treatments(disease):
    return d_treatment_map[disease]


def if_not_matched(disease):
    print("")
    id_disease = disease
    disease_details = get_details(id_disease)
    treatments = get_treatments(id_disease)
    print("")
    print("The most probable disease that you have is %s\n" % (id_disease))
    print("A short description of the disease is given below :\n")
    print(disease_details + "\n")
    print("The common medications and procedures suggested by other real doctors are: \n")
    print(treatments + "\n")


class Greetings(KnowledgeEngine):
    # Pantalla de inicio
    @DefFacts()
    def _initial_action(self):
        self.ventana = tk.Tk()
        self.ventana.rowconfigure(0, minsize=800, weight=1)
        self.ventana.columnconfigure(1, minsize=800, weight=1)
        self.txt_edit = tk.Text(self.ventana)
        self.fr_buttons = tk.Frame(self.ventana, relief=tk.RAISED, bd=2)
        self.label1 = tk.Label(self.fr_buttons,
                               text="Hi! I am Dr.Yar, I am here to help you make your health better. For that "
                                    "you'll have to answer a few questions about your conditions. Do you feel "
                                    "any of the following symptoms:")
        # sympthom 1
        self.labelheadache = tk.Label(self.fr_buttons, text="Headache:")
        self.labelheadache.grid(column=0, row=1, sticky="ew")
        self.dato1 = tk.StringVar()
        self.entry1 = tk.Entry(self.fr_buttons, textvariable=self.dato1)
        self.entry1.grid(column=1, row=1)

        # sympthom 2
        self.labelbackpain = tk.Label(self.fr_buttons, text="back pain:")
        self.labelbackpain.grid(column=0, row=2, sticky="ew")
        self.dato2 = tk.StringVar()
        self.entry2 = tk.Entry(self.fr_buttons, textvariable=self.dato2)
        self.entry2.grid(column=1, row=2)

        # sympthom 3
        self.labelchestpain = tk.Label(self.fr_buttons, text="Chest Pain:")
        self.labelchestpain.grid(column=0, row=3, sticky="ew")
        self.dato3 = tk.StringVar()
        self.entry3 = tk.Entry(self.fr_buttons, width=20, textvariable=self.dato3)
        self.entry3.grid(column=1, row=3)

        # sympthom 4
        self.labelcough = tk.Label(self.fr_buttons, text="Cough:")
        self.labelcough.grid(column=0, row=4, sticky="ew")
        self.dato4 = tk.StringVar()
        self.entry4 = tk.Entry(self.fr_buttons, width=20, textvariable=self.dato4)
        self.entry4.grid(column=1, row=4)

        # sympthom 5
        self.labelfainting = tk.Label(self.fr_buttons, text="Fainting:")
        self.labelfainting.grid(column=0, row=5, sticky="ew")
        self.dato5 = tk.StringVar()
        self.entry5 = tk.Entry(self.fr_buttons, width=20, textvariable=self.dato5)
        self.entry5.grid(column=1, row=5)

        # sympthom 6
        self.labelfatigue = tk.Label(self.fr_buttons, text="Fatigue:")
        self.labelfatigue.grid(column=0, row=6, sticky="ew")
        self.dato6 = tk.StringVar()
        self.entry6 = tk.Entry(self.fr_buttons, width=20, textvariable=self.dato6)
        self.entry6.grid(column=1, row=6)

        # sympthom 7
        self.labelsunkeneyes = tk.Label(self.fr_buttons, text="Sunken Eyes:")
        self.labelsunkeneyes.grid(column=0, row=7, sticky="ew")
        self.dato7 = tk.StringVar()
        self.entry7 = tk.Entry(self.fr_buttons, width=20, textvariable=self.dato7)
        self.entry7.grid(column=1, row=7)

        # sympthom 8
        self.labellbt = tk.Label(self.fr_buttons, text="Low Body Temp:")
        self.labellbt.grid(column=0, row=8, sticky="ew")
        self.dato8 = tk.StringVar()
        self.entry8 = tk.Entry(self.fr_buttons, width=20, textvariable=self.dato8)
        self.entry8.grid(column=1, row=8)

        # sympthom 9
        self.labelrest = tk.Label(self.fr_buttons, text="Restlessness:")
        self.labelrest.grid(column=0, row=9, sticky="ew")
        self.dato9 = tk.StringVar()
        self.entry9 = tk.Entry(self.fr_buttons, width=20, textvariable=self.dato9)
        self.entry9.grid(column=1, row=9)

        # sympthom 10
        self.labelst = tk.Label(self.fr_buttons, text="Sore Throat:")
        self.labelst.grid(column=0, row=10, sticky="ew")
        self.dato10 = tk.StringVar()
        self.entry10 = tk.Entry(self.fr_buttons, width=20, textvariable=self.dato10)
        self.entry10.grid(column=1, row=10)

        # sympthom 11
        self.labelfever = tk.Label(self.fr_buttons, text="Fever:")
        self.labelfever.grid(column=0, row=11, sticky="ew")
        self.dato11 = tk.StringVar()
        self.entry11 = tk.Entry(self.fr_buttons, width=20, textvariable=self.dato11)
        self.entry11.grid(column=1, row=11)

        # sympthom 12
        self.labelnausea = tk.Label(self.fr_buttons, text="Nausea:")
        self.labelnausea.grid(column=0, row=12, sticky="ew")
        self.dato12 = tk.StringVar()
        self.entry12 = tk.Entry(self.fr_buttons, width=20, textvariable=self.dato12)
        self.entry12.grid(column=1, row=12)

        # sympthom 13
        self.labelblurv = tk.Label(self.fr_buttons, text="Blurred vision:")
        self.labelblurv.grid(column=0, row=13, sticky="ew")
        self.dato13 = tk.StringVar()
        self.entry13 = tk.Entry(self.fr_buttons, width=20, textvariable=self.dato13)
        self.entry13.grid(column=1, row=13)

        # Button
        self.boton1 = tk.Button(self.fr_buttons, text="Diagnosticar", command=self.disease)
        self.boton1.grid(column=1, row=14)

        self.fr_buttons.grid(row=0, column=0, sticky="ns")
        self.txt_edit.grid(row=0, column=1, sticky="nsew")
        self.ventana.mainloop()
        yield Fact(action="find_disease")

    # Ingresar síntomas
    @Rule(Fact(action='find_disease'), NOT(Fact(headache=W())), salience=1)
    def symptom_0(self):
        self.declare(Fact(headache=self.dato1))

    @Rule(Fact(action='find_disease'), NOT(Fact(back_pain=W())), salience=1)
    def symptom_1(self):
        self.declare(Fact(back_pain=self.dato1))

    @Rule(Fact(action='find_disease'), NOT(Fact(chest_pain=W())), salience=1)
    def symptom_2(self):
        self.declare(Fact(chest_pain=self.dato1))

    @Rule(Fact(action='find_disease'), NOT(Fact(cough=W())), salience=1)
    def symptom_3(self):
        self.declare(Fact(cough=self.dato1))

    @Rule(Fact(action='find_disease'), NOT(Fact(fainting=W())), salience=1)
    def symptom_4(self):
        self.declare(Fact(fainting=self.dato1))

    @Rule(Fact(action='find_disease'), NOT(Fact(fatigue=W())), salience=1)
    def symptom_5(self):
        self.declare(Fact(fatigue=self.dato1))

    @Rule(Fact(action='find_disease'), NOT(Fact(sunken_eyes=W())), salience=1)
    def symptom_6(self):
        self.declare(Fact(sunken_eyes=self.dato1))

    @Rule(Fact(action='find_disease'), NOT(Fact(low_body_temp=W())), salience=1)
    def symptom_7(self):
        self.declare(Fact(low_body_temp=self.dato1))

    @Rule(Fact(action='find_disease'), NOT(Fact(restlessness=W())), salience=1)
    def symptom_8(self):
        self.declare(Fact(restlessness=self.dato1))

    @Rule(Fact(action='find_disease'), NOT(Fact(sore_throat=W())), salience=1)
    def symptom_9(self):
        self.declare(Fact(sore_throat=self.dato1))

    @Rule(Fact(action='find_disease'), NOT(Fact(fever=W())), salience=1)
    def symptom_10(self):
        self.declare(Fact(fever=self.dato1))

    @Rule(Fact(action='find_disease'), NOT(Fact(nausea=W())), salience=1)
    def symptom_11(self):
        self.declare(Fact(nausea=self.dato1))

    @Rule(Fact(action='find_disease'), NOT(Fact(blurred_vision=W())), salience=1)
    def symptom_12(self):
        self.declare(Fact(blurred_vision=self.dato1))

    # Evaluar sintomas y diagnosticar la enfermedad
    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="yes"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="yes"), Fact(sunken_eyes="no"), Fact(nausea="yes"),
          Fact(blurred_vision="no"))
    def disease_0(self):
        self.declare(Fact(disease="Jaundice"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="no"), Fact(restlessness="yes"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"))
    def disease_1(self):
        self.declare(Fact(disease="Alzheimers"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="yes"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="yes"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"))
    def disease_2(self):
        self.declare(Fact(disease="Arthritis"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="yes"),
          Fact(cough="yes"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="no"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="yes"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"))
    def disease_3(self):
        self.declare(Fact(disease="Tuberculosis"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="yes"),
          Fact(cough="yes"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="no"), Fact(restlessness="yes"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"))
    def disease_4(self):
        self.declare(Fact(disease="Asthma"))

    @Rule(Fact(action='find_disease'), Fact(headache="yes"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="yes"), Fact(fainting="no"), Fact(sore_throat="yes"), Fact(fatigue="no"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="yes"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"))
    def disease_5(self):
        self.declare(Fact(disease="Sinusitis"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="yes"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"))
    def disease_6(self):
        self.declare(Fact(disease="Epilepsy"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="yes"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="no"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="yes"),
          Fact(blurred_vision="no"))
    def disease_7(self):
        self.declare(Fact(disease="Heart Disease"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="yes"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="yes"),
          Fact(blurred_vision="yes"))
    def disease_8(self):
        self.declare(Fact(disease="Diabetes"))

    @Rule(Fact(action='find_disease'), Fact(headache="yes"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="no"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="yes"),
          Fact(blurred_vision="yes"))
    def disease_9(self):
        self.declare(Fact(disease="Glaucoma"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="yes"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="yes"),
          Fact(blurred_vision="no"))
    def disease_10(self):
        self.declare(Fact(disease="Hyperthyroidism"))

    @Rule(Fact(action='find_disease'), Fact(headache="yes"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="no"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="yes"), Fact(sunken_eyes="no"), Fact(nausea="yes"),
          Fact(blurred_vision="no"))
    def disease_11(self):
        self.declare(Fact(disease="Heat Stroke"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="yes"), Fact(sore_throat="no"), Fact(fatigue="no"), Fact(restlessness="no"),
          Fact(low_body_temp="yes"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"))
    def disease_12(self):
        self.declare(Fact(disease="Hypothermia"))

    # Diagnóstico
    @Rule(Fact(action='find_disease'), Fact(disease=MATCH.disease), salience=-998)
    def disease(self, disease):
        print("")
        id_disease = disease
        disease_details = get_details(id_disease)
        treatments = get_treatments(id_disease)
        diagnostico = "The most probable disease that you have is %s\n" % id_disease % "A short description of the " \
                                                                                       "disease is given below :\n" \
                      + disease_details + "\n ""The common medications and procedures suggested by other real doctors are: \n" + treatments + "\n "

        self.txt_edit.configure(text=diagnostico)
        '''
        print("")
        print("The most probable disease that you have is %s\n" % (id_disease))
        print("A short description of the disease is given below :\n")
        print(disease_details + "\n")
        print("The common medications and procedures suggested by other real doctors are: \n")
        print(treatments + "\n")
        '''

    @Rule(Fact(action='find_disease'),
          Fact(headache=MATCH.headache),
          Fact(back_pain=MATCH.back_pain),
          Fact(chest_pain=MATCH.chest_pain),
          Fact(cough=MATCH.cough),
          Fact(fainting=MATCH.fainting),
          Fact(sore_throat=MATCH.sore_throat),
          Fact(fatigue=MATCH.fatigue),
          Fact(low_body_temp=MATCH.low_body_temp),
          Fact(restlessness=MATCH.restlessness),
          Fact(fever=MATCH.fever),
          Fact(sunken_eyes=MATCH.sunken_eyes),
          Fact(nausea=MATCH.nausea),
          Fact(blurred_vision=MATCH.blurred_vision), NOT(Fact(disease=MATCH.disease)), salience=-999)
    def not_matched(self, headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,
                    low_body_temp, fever, sunken_eyes, nausea, blurred_vision):
        print("\nDid not find any disease that matches your exact symptoms")
        lis = [headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness, low_body_temp,
               fever, sunken_eyes, nausea, blurred_vision]
        max_count = 0
        max_disease = ""
        for key, val in symptom_map.items():
            count = 0
            temp_list = eval(key)
            for j in range(0, len(lis)):
                if temp_list[j] == lis[j] and lis[j] == "yes":
                    count = count + 1
            if count > max_count:
                max_count = count
                max_disease = val
        if_not_matched(max_disease)


if __name__ == "__main__":

    preprocess()
    engine = Greetings()
    while (1):
        engine.reset()  # Prepare the engine for the execution.
        engine.run()  # Run it!
        print("Would you like to diagnose some other symptoms?")
        if input() == "no":
            exit()
