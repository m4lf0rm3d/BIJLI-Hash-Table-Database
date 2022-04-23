from linear_hashtable_functions_input import *
from math import ceil

def inputNumber():

    phone_number = input("Please Enter a Pakistani 11 digits Phone Number: \n >>>> ")

    if phone_number.isalpha()  or " " in phone_number or "." in phone_number or len(phone_number) != 11 or not phone_number.isdigit() or phone_number[0] != "0":

        print("Please enter a valid 11 digits Pakistani Phone Number e.g 03181236267")
        print("Try Again! \n")
        return inputNumber()

    return phone_number

def inputName():

    input_name = input("Please enter the full name: \n >>>> ")
    modified_name = input_name.split(" ")
    modified_name = "".join(modified_name)

    if not modified_name.isalpha() or input_name.isnumeric() or input_name.isdigit() or "." in input_name or input_name.isdecimal() or len(input_name) < 3 or len(input_name) > 19:
        
        print("Please enter a valid name less than 19 charachters!")
        print("Try Again! \n")
        return inputName()

    return input_name

def inputCity():
    input_city = input("Please enter the city name: \n >>>> ")
    modified_name = input_city.split(" ")
    modified_name = "".join(modified_name)

    if not modified_name.isalpha() or input_city.isnumeric() or input_city.isdigit() or "." in input_city or input_city.isdecimal() or len(input_city) < 3 or len(input_city) > 20:
        
        print("Please enter a valid city name less than 20 charachters!")
        print("Try Again! \n")
        return inputName()

    return input_city

def inputState():
    input_state = input("Please enter the state name: \n >>>> ")
    input_state = input_state.upper()

    if input_state not in ["BALOCHISTAN","KPK","SINDH","PUNJAB","KASHMIR"]:
        print("Please enter a valid state of Pakistan!")
        print("Try Again! \n")
        return inputState()

    return input_state

def inputTime():


    def inputHours():
        input_hours = input("Please enter the HOURS time: \n >>>> ")
        
        if input_hours.isalpha()  or " " in input_hours or "." in input_hours or len(input_hours) > 2 or not input_hours.isdigit():
            print("Please enter HOURS time between [1,12] inclusive!")
            print("Try Again! \n")
            return inputHours()

        if int(input_hours) <= 0 or int(input_hours) > 12:
            print("Please enter HOURS time between [1,12] inclusive!")
            print("Try Again! \n")
            return inputHours()

        return int(input_hours)

    def inputMinutes():
        input_minutes = input("Please enter the MINUTES time: \n >>>> ")
        
        if input_minutes.isalpha()  or " " in input_minutes or "." in input_minutes or len(input_minutes) > 2 or not input_minutes.isdigit():
            print("Please enter MINUTES time between [10,59] inclusive!")
            print("Try Again! \n")
            return inputMinutes()

        if int(input_minutes) < 10 or int(input_minutes) > 59:
            print("Please enter MINUTES time between [10,59] inclusive!")
            print("Try Again! \n")
            return inputMinutes()

        return int(input_minutes)

    def amOrPm():
        input_time_format = input("Please enter AM or PM: \n >>>> ")
        
        input_time_format = input_time_format.upper()

        if input_time_format != "AM" and input_time_format != "PM":
            print("Please enter AM or PM!")
            print("Try Again! \n")
            return amOrPm()

        return input_time_format

    return (inputHours(), inputMinutes(), amOrPm())


    


def hashSearch(linear_hashtable):

    #getting input
    input_number = inputNumber()

    #search for given phone number
    phone_number_data = linear_hashtable.search(int(input_number[1:]))

    if not phone_number_data:
        print("\n================ SORRY :( ================")
        print("The number does not exist in our database!")
        print("==========================================\n")

    else:

        print("|"+"="*86+"|")
        print("|  PHONE NUMBER  |         NAME         |      CITY      |     STATE     |  LAST SEEN  |")
        print("|"+"="*86+"|")
        print("|   0"+str(phone_number_data[0])  +"  |"+" "*ceil((22-len(phone_number_data[1]))/2) + str(phone_number_data[1])+ " "*((22-len(phone_number_data[1]))//2)+"|" + " "*ceil((16-len(phone_number_data[2]))/2) + str(phone_number_data[2])+ " "*((16-len(phone_number_data[2]))//2)+ "|"+ " "*ceil((15-len(phone_number_data[4]))/2) + str(phone_number_data[4])+ " "*((15-len(phone_number_data[4]))//2)+"|"+ " "*ceil((13-len(phone_number_data[3]))/2) + str(phone_number_data[3])+ " "*((13-len(phone_number_data[3]))//2)+"|")
        print("|"+"="*86+"|\n")


def hashDelete(linear_hashtable):

    #getting input
    input_number = int(inputNumber()[1:])

    if not linear_hashtable.search(input_number):
        print("\n================ SORRY :( ================")
        print("The number does not exist in our database!")
        print("==========================================\n")

    linear_hashtable.delete(input_number)
    print("\n=================================================")
    print("Given number's data has been deleted Successfully!")
    print("=================================================\n")


def hashInsert(linear_hashtable):

    print("\n=================================================")
    print("Please enter the following details, so BIJLI can add it to Hash Table ;)\n")
    
    input_number,input_name,input_city,input_state, input_time = int(inputNumber()[1:]),inputName(),inputCity(),inputState(), inputTime()

    input_time = str(input_time[0]) + ":" + str(input_time[1]) + " " + str(input_time[2])

    data = [input_number,input_name,input_city,input_time, input_state]
    linear_hashtable.insert(data)






    