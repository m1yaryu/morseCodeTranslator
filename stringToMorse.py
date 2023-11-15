#Takes input from user
Input = input("Enter message: ").upper()
#Blank variable to enter morse code
MorseCode = ""

#Dictionary to define the Morse code for each letter
MorseDict = {"A" :".-",
            "B" : "-..." ,
            "C" : "-.-." ,
            "D" : "-.." ,
            "E" : "." ,
            "F" : "..-." ,
            "G" : "--." ,
            "H" : "...." ,
            "I" : ".." ,
            "J" : ".---" ,
            "K" : "-.-" ,
            "L" : ".-.." ,
            "M" : "--" ,
            "N" : "-." ,
            "O" : "---" ,
            "P" : ".--." ,
            "Q" : "--.-" ,
            "R" : ".-." ,
            "S" : "..." ,
            "T" : "-" ,
            "U" : "..-" ,
            "V" : "...-" ,
            "W" : ".--" ,
            "X" : "-..-" ,
            "Y" : "-.--" ,
            "Z" : "--.."}

#for loop that goes through each letter in the input message
#   and enters the code for each letter and puts it in the MorseCode variable
for element in Input:
    if element != " ":
        MorseCode += MorseDict[element] + " "
    elif element == ' ':
        MorseCode += "/ "
    else:
        MorseCode += " "
    

#prints the Morse code of the input message
print("Your message in Morse code: " + MorseCode)
