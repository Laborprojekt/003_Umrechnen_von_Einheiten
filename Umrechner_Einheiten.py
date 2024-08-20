'''
#-----------------------#
Programm: 		Einheitenumrechner
Version: 		V1.0

Programmierer: 	Eberlei
Datum:			20.08.2024
#-----------------------#
'''

def float_check (num):
     
    try:
        num = float(num)	#versucht Input in float umzuwandeln
        return True	#wenn möglich, wird der Input zurückgegeben
        
    except ValueError:			#wenn nicht möglich, wird Fehlermeldung rausgegeben
        return False
    
    
def input_check ():
    check = False				#Variable für while Schleife wird deffiniert
    
    while not check:
        user_inp = input("\nInput: ")
        check_return = float_check(user_inp)	#nimmt Eingabe des Users auf und kontrolliert float kompatibilität
        
        if check_return:								#nur wenn die Umwandlung erfolgreich war, enhält user_inp einen Wert größer 0
            check = True 
        
        else:
            check = False 
            print("\nInput can't include letters, try again")
    return user_inp

print(
    "\nChoose unit you want do transfer:\n"

    "------------\n" #12x -
    "1. cm to inch \n"
    "2. km to eng. mile / international seemile \n"
    "3. liter to beer \n"
    "4. kg to pound \n"
    "5. Celsius to Kelvin \n"
    "------------"
    )
unit_num = float(input("Unit number: ")) #Check, if digit and is in list 0-4
                  
checked_inp = float(input_check())


match unit_num:

    case 1 :
        inch = checked_inp * 2.54				#inch = cm * 2.54
        print(f"{checked_inp}cm are {inch} inch.")
              
    case 2 :
        eng_mile = checked_inp * 1.60934 		#englisch mile = km * 1.60934
        seemile = checked_inp * 1.852			#international seemile = km * 1.852
        print(f"{checked_inp}km are {eng_mile} englisch miles or {seemile} international seemiles.")
              
    case 3 :
        beer = checked_inp * 0.33				#one beer has 330ml
        print(f"{checked_inp} liter are {beer} beers.") 
              
    case 4 :
        pound = checked_inp * 0.5				#one Pound are 500g
        print(f"{checked_inp}kg are {pound} pound.") 
              
    case 5 :
        kelvin = 273.15 + checked_inp 			#Kelvin starts at -273.15°C. 273.15 Kelvin is equal to 0°C
        print(f"{checked_inp}°C are {kelvin} Kelvin.")
        
    case _:
        print("invalid unit number")

              
              