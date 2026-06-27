decimal = int(input("Enter a decimal number: "))

binary = ""

while decimal > 0:
    remainder = decimal % 2

    for i in range(1):   # nested loop
        binary = str(remainder) + binary

    decimal = decimal // 2

print("Binary number:", binary)