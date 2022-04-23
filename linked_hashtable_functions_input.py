
from linked_hashtable_functions import *

def inputNumber():

    phone_number = input("Please Enter a Pakistani 11 digits Phone Number: \n >>>> ")

    if phone_number.isalpha()  or " " in phone_number or "." in phone_number or len(phone_number) != 11 or not phone_number.isdigit() or phone_number[0] != "0":

        print("Please enter a valid 11 digits Pakistani Phone Number e.g 03181236267")
        print("Try Again! \n")
        return inputNumber()

    return phone_number

def inputLinkedOptions():

    print("1) Search")
    print("2) Insert")
    print("3) Delete\n")
    print("========= Select an Option to continue =========\n")

    option_number = input(">>>> ")

    if option_number.isalpha()  or " " in option_number or "." in option_number or len(option_number) != 1 or not option_number.isdigit() or (option_number != "1" and option_number != "2" and option_number != "3"):

        print("Please enter a valid number (1 or 2 or 3)!")
        print("Try Again! \n")
        return inputLinkedOptions()
    
    return int(option_number)


def showOptionsLinked(linked_hashtable):
    print("\n============ Seperate Chaining (Linked List) ============\n")
    user_option = inputLinkedOptions()


    if user_option == 1:
        
        hashSearchLinked(linked_hashtable)

    if user_option == 2:
        hashInsertLinked(linked_hashtable)

    if user_option == 3:
        hashDeleteLinked(linked_hashtable)


    while True:
        break_input= input("Please Press ENTER to return back to main menu!")
        if break_input == "":
            break

    showOptionsLinked(linked_hashtable)