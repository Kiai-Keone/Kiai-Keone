def readposint():
    try:
        UserInput = int(input("Enter a positive integer: "))
        if UserInput <= 0:
            print ("Enter a positive integer.")
        else:
            return UserInput
    except ValueError:
        print ("Invalid. Enter a valid positive integer.")

print (readposint())
    
    
