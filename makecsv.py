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
    mode = input("Append or Rewrite OUTPUT FILE [A/R] > ")

    if mode.lower() == 'a':
        break
    elif mode.lower == 'r':
        break
    else:
        print("The mode can be 'A' to Append or 'R' to Rewrite only.")


with open(input_file_name, 'r') as input_file:
    lines = input_file.read().split('\n')

if mode.lower() == 'a':
    with open(output_file_name, 'a+') as output_file:
        for line in lines:
            output_file.write(f"{delimiter}".join(line.split())+"\n")
elif mode.lower() == 'r':
    with open(output_file_name, 'a+') as output_file:
        for line in lines:
            output_file.write(f"{delimiter}".join(line.split())+"\n")
else:
    print("I really don't know how you're here") 
