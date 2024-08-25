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
        us_input = input("Selection: ")

        if len(us_input) == 1 and us_input.isdigit(): # prüfung, ob input einzelne Zahl ist

            if 1 <= int(us_input) <= menu_pos:
                check = True
                return us_input
            else:
                print("Error: Selection not in list\n") 
        else:
            print("Error: Input must be a single integer.\n")


def input_check():
    check = False

    while not check:
        us_input = input(f"\nInput for conversion: ")
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
     

def valide_operator():
        val_op = False
        val_op_list = ["+", "-", "*", "/"]

        while not val_op:
            op = input ("\nOperator (currently only +,-,* and / allowed): ")
            if op in val_op_list :
                val_op = True
                return op
            else:
                print(f"{op} is not in allowed character list or to long")

def add_summary(function_name, start_un, end_un, op, fac):
    print("input summary: \n"
            f"Function name:        {function_name}\n"
            f"1. Start unit:        {start_un}\n"
            f"2. End unit:          {end_un}\n"
            f"3. Operator:          {op}\n"
            f"4. Conversion factor: {fac}\n"
            )
    
def add_unit():

    ready = False
    val_confirm = False
    export_ready = False

    while not ready:
        
        
        start_un = input("\nbeginning unit:")

        end_un = input("\nending unit:")

        function_name = f"{start_un} to {end_un}"

        op = valide_operator()
        
        fac = input_check()


        while not export_ready:
            add_summary(function_name, start_un, end_un, op, fac)

                
            confirm = input("Are the inputs correct?\n"
                            "(y/n): ")
            confirm = confirm.lower()

            if confirm == "y":
                export_ready = True
                ready = True

            elif confirm == "n":
                val_corr = False

                while not val_corr :
                    correct = input("what would you like to correct: ")
                        
                    if len(correct) == 1 and correct.isdigit(): # prüfung, ob input einzelne Zahl ist
                            
                        if 0< int(correct) <= 4:
                                

                            match correct:

                                case "1" :
                                        start_un = input("beginning unit:")

                                case "2" :
                                        end_un = input("ending unit:")

                                case "3" :
                                        op = valide_operator()

                                case "4" :
                                        fac = input_check()


                            val_corr = True

                else:
                    print("input invalid, try again\n")



    new_export = f'{{"name" : "{function_name}", "start_unit" : "{start_un}", "operator": "{op}", "faktor" : "{fac}", "end_unit" : "{end_un}"}}'
    print(new_export)

    storage = open(FILE, "a")
    storage.write(new_export)
    storage.close()




# --------------------------------------------------------------------------------------------------------------------

# Main Schleife
while True:

    # Counter Variabelen. Müssen bei jedem run zurückgesetzt werden, sonst kommt es zu fehlen
    i = 0 # Counter Listenindex dict
    menu_count = 0 # Counter für die nummerierung der Optionen

    name_list = []          
    start_list = []         
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
        valid_input = float(input_check())
        calc = calculator()

        print (f"{name_list[calc_index]}: {valid_input} {start_list[calc_index]} are {calc} {end_list[calc_index]}.\n") #Ausgabe: cm to inch: 20.0 cm are 7.874 inch.)

    elif valid_menu == menu_count-1 : # add Unit function 
        add_unit()

    elif valid_menu == menu_count : # close program function
        print("\nHave a nice day :)\n")
        break
        
    else:
        print("CRITICAL SYSTEM ERROR! Menu number is invalid. Errorhandling out of service")