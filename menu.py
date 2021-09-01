day=input("enter the day:-")
time=input("enter the time")
if day=="monday":
    if time=="breakfast":
        print("sandwich")
    elif time=="lunch":
        print("dal chawal")
    elif time=="dinner":
        print("roti sabji")      
    else:
        print("fast food")