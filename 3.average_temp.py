#Getting Values from a text file and performing some operation with it

def get_average():
    with open('Files/data.txt') as file:
        data = file.readlines()
    
    values = data[1:] #Because data is a List, so we can slice
    values = [float(i) for i in values]

    average_local = sum(values) / len(values)

    return average_local



average = get_average()

print(average)