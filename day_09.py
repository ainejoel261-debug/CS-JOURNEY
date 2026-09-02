while True:
    try:
        num_1 = int(input("Enter your number: "))
        num_2 = int(input("Enter your number: "))
        result = num_1//num_2
    except ValueError:
        print("Nigga enter numbers only!")
    except ZeroDivisionError:
        print("Cant enter 0, try other numbers!")
    else:
        print("The result is" ,result)                        #else is for when the try has worked
        break
    finally:
        print("Calculation attempt finished.")

while True:
    try:
        cgpa = float(input("Enter your CGPA: "))
        if cgpa > 5 or cgpa < 0:
            raise ValueError("CGPA is 0, 5 or between 0 and 5!")
    except ValueError:
        print("Enter the correct value CGPA!")
    else:
        print("Your CGPA is:" ,cgpa)
        break
    finally:
        print("CGPA validation finished.")

