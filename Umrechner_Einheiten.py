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
        float_num = float(num)
        return float_num
        
    except ValueError:
        return False
    
def input_check ():
    check = False
    
    while not check:
        user_inp = float_check(input("\nInput: "))
        
        if user_inp:
            float_inp = float(user_inp)
            check = True 
            return float_inp
        
        else:
            print("\nInput can't include letters, try again")

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
Unit_num = input("Unit number: ") #Check, if digit and is in list 0-4
                  
checked_inp = input_check()


              
              