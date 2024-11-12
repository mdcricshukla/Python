
''' 8 number =float(input("Enter the number"))
formatted_number = f"{number:.2f}"
print(formatted_number)'''



''' 9 number = float(input("Enter the Number"))
rounded_number = int(number)
print(rounded_number)'''



''' 10  integer1 = int(input("Enter The integer"))

width =int(input("Enter the Width"))  
formatted_integer1 = str(integer1).zfill(width)
print(formatted_integer1)'''



integer1 = (input("Enter the number:"))

width = (input("Enter the width:"))


formatted_integer1 = "{:<0{width}}".format(integer1, width=width)



print(formatted_integer1)





