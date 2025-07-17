try:
   width = float(input("Enter rectangle width: "))
   length = float(input("Enter rectangle length: "))

   if width == length:
    exit("That Look like a Square")
   area = width * length

except ValueError:
    print("Please enter a number.")