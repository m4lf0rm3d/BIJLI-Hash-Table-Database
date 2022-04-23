
def inputMethod():

    
    print("1) Open Addressing (Linear Probing)")
    print("2) Separate Chaining (Linked Lists)\n")
    print("========= Select a Method to continue =========\n")

    method_number = input(">>>> ")

    if method_number.isalpha()  or " " in method_number or "." in method_number or len(method_number) != 1 or not method_number.isdigit() or (method_number != "1" and method_number != "2"):

        print("Please enter a valid number (1 or 2)!")
        print("Try Again! \n")
        return inputMethod()
    
    return int(method_number)