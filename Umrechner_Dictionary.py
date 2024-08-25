'''
#-----------------------#
Programm: 		Einheitenumrechner
Version: 		V2.0

Programmierer: 	Eberlei
Datum:			25.08.2024
#-----------------------#
'''

import ast

#Konstanten
FILE = "Storage.py" # Dateiname der dict Datei


# Funktionen
def menu_check(menu_pos):
    check = False
    while not check:
        us_input = input("Select function: ")

        if len(us_input) == 1 and us_input.isdigit(): # prüfung, ob input einzelne Zahl ist

            if 1 <= int(us_input) <= menu_pos:
                check = True
                return us_input
            else:
                print("Error: Selection not in list\n") 
        else:
            print("Error: Input must be a single integer.\n")


def calc_check(unit_list, index):
    check = False
    unit_list = list(unit_list)
    index = int(index)

    while not check:
        us_input = input(f"Input in {unit_list[index]}: ")
        us_input = us_input.replace(",",".")

        try:
            float(us_input)
            check = True
        except ValueError:
            print("invalid input, try again\n")
    
    return us_input

def calculator ():
    op = operator_list[calc_index]

    match op:
        case "+" :
            result = round(valid_input + float(faktor_list[calc_index]), 3)
        case "-" :
            result = round(valid_input - float(faktor_list[calc_index]), 3)
        case "*" :
            result = round(valid_input * float(faktor_list[calc_index]), 3)
        case "/" :
            result = round(valid_input / float(faktor_list[calc_index]), 3)
    
    return result
    
    

def add_unit():
    print ("Function will be added soon\n")

# --------------------------------------------------------------------------------------------------------------------

# Main Schleife
while True:
    # Counter Variabelen
    i = 0 # Counter Listenindex dict
    menu_count = 0 # Counter für die nummerierung der Optionen

    name_list = []          #um das index rechnen zu vereinfachen könnte man einen Platzhalter auf index 0 setzen 
    start_list = []         #um verwirrung zu vermeiden, habe ich mich dagegen entschieden
    operator_list = []
    faktor_list = []
    end_list = []

    # Einlesen der Speicherdatei. Muss bei jedem durchlauf erneuert werden, da sonst neue Funktionen erst nach Neustart verfügbar sind
    storage = open(FILE, "r")
    storage_list = storage.readlines()
    storage.close()

    # Schreibt alle Werte in separate Listen, für die spätere Auswertung
    for positions in storage_list:
        unit = ast.literal_eval(storage_list[i])    # "ast.literal_eval" kann Strings, deren Formatierung einem dict entspricht, in Dictionarys umwandeln. Teil der inbuild python libary

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

    # Fügt der Liste Systemfuntionen zu, die ebenfalls im Menü erscheinen sollen
    name_list.append("add Unit")
    name_list.append("close program")

    # genreierung Auswahlmenü des Users
    print("# ------------ #") # 12x -
    for operation in name_list: # List alle Positionen aus der Liste aus und schreibt sie in die Konsole. Auswahlmenü des Users

        print (f"{menu_count+1}. {name_list[menu_count]}") # menücouner -1, da der Listenindex mit 0 beginnt
        menu_count += 1

    print("# ------------ #\n\n")


    # Auswahl Menüfunktion
    valid_menu = int(menu_check(menu_count))
    calc_index = valid_menu -1
    print(f"You choose '{name_list[calc_index]}'")

    if 0<= valid_menu <= menu_count-2 :
        valid_input = float(calc_check(start_list, calc_index))
        #formula = f"{valid_input} {operator_list[calc_index]} {faktor_list[calc_index]}"
        calc = calculator()
        result = f"{name_list[calc_index]}: {valid_input} {start_list[calc_index]} are {calc} {end_list[calc_index]}.\n" #Ausgabe: cm to inch: 20.0cm are 7.874 inch.
        print(result)

    elif valid_menu == menu_count-1 : # add Unit function 
        add_unit()

    elif valid_menu == menu_count : # close program function
        print("\nHave a nice day :)\n")
        break
        
    else:
        print("CRITICAL SYSTEM ERROR! Menu number is invalid. Errorhandling out of service")







































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