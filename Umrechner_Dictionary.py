'''
#-----------------------#
Programm: 		Einheitenumrechner
Version: 		V2.0

Programmierer: 	Eberlei
Datum:			25.08.2024
#-----------------------#
'''

import ast

#Startvariablen
i = 0 # Counter Listenindex dict
file = "Storage.py" # Dateiname der dict Datei

name_list = []
start_list = []
operator_list = []
faktor_list = []
end_list = []


# Funktionen
def menu_check(menu_pos):
    check = False
    print (menu_pos)
    while not check:
        us_input = input("Select function: ")

        if len(us_input) == 1 and us_input.isdigit(): # prüfung, ob input einzelne Zahl ist

            if 0 <= int(us_input) <= menu_pos:
                check = True
                return us_input
            else:
                print("Error: Selection not in list") 
        else:
            print("Error: Input must be a single integer.")




# Einlesen der Speicherdatei
storage = open(file, "r")
storage_list = storage.readlines()
storage.close()


# Schreibt alle Werte in separate Liste, für die spätere Auswertung
for positions in storage_list:
    unit = ast.literal_eval(storage_list[i])    # "ast.literal_eval" kann Strings, deren Inhalt einem dict entspricht, in Dictionarys umwandeln. Teil der inbuild python libary

    name = unit["name"]
    name_list.append (name)

    start_unit = unit["start_unit"]
    start_list.append (start_unit)

    operator = unit["operator"]
    operator_list.append (operator)

    faktor = unit["faktor"]
    faktor_list.append (faktor)

    end_unit = unit["end_unit"]
    end_list.append (end_unit)
    
    i +=1

# Main Schleife
while True:
    # genreierung Auswahlmenü des Users
    print("# ------------ #") # 12x -

    menu_count = 0 # Counter für die nummerierung der Optionen

    name_list.append("add Unit")
    name_list.append("close program")

    for i in name_list: # List alle Positionen aus der Liste aus und schreibt sie in die Konsole. Auswahlmenü des Users

        print (f"{menu_count+1}. {name_list[menu_count]}") # menücouner -1, da der Listenindex mit 0 beginnt

        menu_count += 1

    print("# ------------ #\n\n")


    # Auswahl Menüfunktion
    valid_menu = int(menu_check(menu_count)-1)

    print(f"You choose '{name_list[valid_menu - 1]}'")









































'''
def input_check ():
    check = False				                    #Variable für while Schleife wird deffiniert
    
    while not check:
        user_inp = input("\nInput: ")
        user_inp = user_inp.replace("," , ".")
        
        try:
            user_inp = float(user_inp)	            #versucht Input in float umzuwandeln
            check_return = True	                    #wenn möglich, wird der Input zurückgegeben
            
        except ValueError:			                #wenn nicht möglich, wird Fehlermeldung rausgegeben
            check_return = False


        if check_return:							#nur wenn die Umwandlung erfolgreich war, enhält user_inp einen Wert größer 0
            check = True 
            
        else:
            check = False 
            print("\nInput can't include letters, try again")
            
    return user_inp


def digit_num ():                                   #kann auch über "match" Funktion  realisiert werden, Fehlermeldung ist aber ungenau
    list_digit = False
    menu_opt = [1,2,3,4,5,6]                        #Liste, die alle Zahlen der Menüoptionen beinhaltet
    while not list_digit:

        user_inp = input("Unit number: ")
        
        if user_inp.__len__() == 1:                 #Leitet Eingabe nur weiter, wenn sie aus max. 1 Wert besteht

            if user_inp.isdigit():
                user_inp = int(user_inp)            #funktion .isdigit muss ein string sein, zum abgleich der Liste wird ein integer benötigt

                if user_inp in menu_opt:            #Durchsucht die Liste nach einer übereinstimmung
                    list_digit = True
                    return user_inp
                else:
                    print("invalid input. Must between 1-6")
                    
            else:
                print("invalid input. Must be one number, without dezimal characters")

        else:
            print("invalid input. Must be only one character")
            

while True:
    print(
        "\nChoose unit you want do transfer:\n"

        "------------\n" #12x -

        "------------"
        )
    

    unit_num = digit_num()                                  #checks input if it is a single, int character

    if unit_num == 6:
        print("\nHave a nice day :)\n"
              "\n-- programm closed --\n")
        break
                   
    checked_inp = float(input_check())                      #checks, if the input include letters    
'''