#In the USA, they have the system that lengths can be expressed
#in something like 5 12 - Which means 5 feet, 12 inches
#Thats the kind of input the program expects

#Used to explain decoupling - spliting or dividing responsibilities
#of a function

feet_inches = input("Enter feet and inches: ")

def parse(feetinches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    return feet, inches


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254

    return meters



f, i = parse(feet_inches) #Tuple unpacking

result = convert(f, i)

if result < 1:
    print("Kid is too small.")

else:
    print("Kid can use the slide.")