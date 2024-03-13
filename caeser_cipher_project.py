alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

def caeser(text,shift):
    
    if direction=="decode":
        shift=shift*(-1)
    end_text=""
    for i in text:
        if i in alphabet:
            x=(alphabet.index(i))+shift
            
            if direction=='encode': 
                
                if x <= 25:
                    end_text=end_text+alphabet[x]
                else:
                    x=x%26
                    end_text=end_text+alphabet[x]
            
            elif direction=='decode':
                
                if x >= 0:
                    end_text=end_text+alphabet[x]
                else:
                    while x<0:
                        x=x+26
                    end_text=end_text+alphabet[x]
        else:
            end_text=end_text+i
    
    print(f"The {(direction).capitalize()}d Text is {end_text}")    
            
print(logo)            
            
continuation=True
while continuation:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
                
    caeser(text,shift)
    
    restart = input("Do you Want to Restart the program, type yes or no: \n").lower()
    
    if restart=="no":
        continuation=False
        print("Adios")



