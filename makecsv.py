import os

while True:
    input_file_name = input("INPUT FILE > ")
    
    if os.path.isfile(input_file_name):
        break
    else:
        print("File not found please enter a valid file.")

output_file_name = input("OUTPUT FILE > ")

os.path.isfile(output_file_name)

delimiter = input("DELIMITER > ")

while True:
    extrafields = input("You want to add extra fields? [Y/N] > ")

    if extrafields.lower() == 'y':
        extrafields = True
        break
    elif extrafields.lower() == 'n':
        extrafields = False
        break
    else:
        print("You can only select Y for yes and N for no.")

if extrafields:
    while True:
        extrafields = input("How many extrafields you want? > ")
        if extrafields.isdigit():
            break
        else:
            print("You must type a number.")

extras = []

for i in range(int(extrafields)):
    extras.append(input(f"Extra field {i+1}/{extrafields} > "))

while True:
    mode = input("Append or Rewrite OUTPUT FILE [A/R] > ")

    if mode.lower() == 'a':
        break
    elif mode.lower() == 'r':
        break
    else:
        print("The mode can be 'A' to Append or 'R' to Rewrite only.")


with open(input_file_name, 'r') as input_file:
    lines = input_file.read().split('\n')

if mode.lower() == 'a':
    with open(output_file_name, 'a+') as output_file:
        for line in lines:
            line = line.split()
            if extrafields:
                line = line + extras
            output_file.write(f"{delimiter}".join(line)+"\n")

elif mode.lower() == 'r':
    with open(output_file_name, 'w') as output_file:
        for line in lines:
            line = line.split()
            if extrafields:
                line = line + extras
            output_file.write(f"{delimiter}".join(line)+"\n")

else:
    print("I really don't know how you're here")
