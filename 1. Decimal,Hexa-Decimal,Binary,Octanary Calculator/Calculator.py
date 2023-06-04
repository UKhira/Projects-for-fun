list_for_mod = list()
maintance = True

# TODO decimal to octanary, hexa-decimal 
# TODO binary to decimal, octanary, hexa-decimal
# TODO octanary to decimal, binary, hexa-decimal
# TODO Hexa-decimal to decimal, binary, octanary
   # if num_mod == 10:
        #     num_mod == "A"
        # elif num_mod == 11:
        #     num_mod == "B"
        # elif num_mod == 12:
        #     num_mod == "C"
        # elif num_mod == 13:
        #     num_mod == "D"
        # elif num_mod == 14:
        #     num_mod == "E"
        # elif num_mod == 15:
        #     num_mod = "F"
        # else:
        #     num_mod = num_mod

# ================verification section========================== 
def decimal_verification(num):
    try:
        num = int(num)
        if num >= 0 :
            print("Verified")
        else:
            print("Number must be positive")
    except Exception:
        print("Decimal number must be an integer")



# ================decimal to ... section=========================
def decimal_to_binary(num):
    global list_for_mod
    num = int(num)
    if num == 1:
        print(10)
    else:
        while num!= 1:
            num_mod = num% 2
            list_for_mod.insert(0, num_mod)
            num= num// 2
        list_for_mod.insert(0, 1)
        for index in list_for_mod:
            print(index, end = '')
        list_for_mod.clear() 
    
def decimal_to_octanary(num):
    global list_for_mod
    num = int(num)
    if num == 1:
        print(10)
    else:
        while num != 1:
            num_mod = num% 8
            list_for_mod.insert(0, num_mod)
            num= num// 8
        list_for_mod.insert(0, 1)
        for index in list_for_mod:
            print(index, end = '')
        list_for_mod.clear() 
    
def decimal_to_hexa_decimal(num):
    global list_for_mod
    num = int(num)
    if num == 1:
        print(10)
    else:
        while num != 1:
            num_mod = num % 16
            list_for_mod.insert(0, num_mod)
            num= num// 16
        list_for_mod.insert(0, 1)
        for index in list_for_mod:
            print(index, end = ' ')
        list_for_mod.clear() 
    
while maintance:
    print("Choose option: which number system you are going to enter \n1. Binary \n2. Octanary \n3. Decimal \n4. Hexa-Decimal")
    input_option1 = input("Please enter the index of your choice or the name \n") 

    if input_option1 == "3" or input_option1.lower() == "decimal":
        number = input("Enter Your number \n")
        decimal_verification(number)

    print("Choose option: which number system you want to convert \n1. Binary \n2. Octanary \n3. Decimal \n4. Hexa-Decimal")
    input_option2 = input("Please enter the index of your choice or the name \n") 

    if (input_option1 =='3' or input_option1.lower() == "decimal") and (input_option2 == "1" or input_option2.lower() == "binary"):
        decimal_to_binary(number)

    elif(input_option1 =='3' or input_option1.lower() == "decimal") and (input_option2 == "2" or input_option2.lower() == "octanary"):
        decimal_to_octanary(number)
        
    elif(input_option1 =='3' or input_option1.lower() == "decimal") and (input_option2 == "4" or input_option2.lower() == "hexa-decimal"):
        decimal_to_hexa_decimal(number)
        
    
    continue_method = input("\nDo you want to continue (Yes/No) \n")
    
    if continue_method.lower() == "y" or continue_method.lower() == "yes":
        maintance = True
    elif continue_method.lower() == "n" or continue_method.lower() == "no":
        maintance = False
    else:
        print("Unrecognized Input")
        maintance = True     

