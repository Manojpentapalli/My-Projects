import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

pwd=[]
for i in range(1,nr_letters+1):
    r1=random.randint(1,len(letters)-1)
    pwd.append(letters[r1])
for j in range(1,nr_numbers+1):
    r2=random.randint(1,len(numbers)-1)
    pwd.append(numbers[r2])
for k in range(1,nr_symbols+1):
    r3=random.randint(1,len(symbols)-1)
    pwd.append(symbols[r3])
    
random.shuffle(pwd)
password="".join(pwd)
print(f"Here is your password: {password}")
