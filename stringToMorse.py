#Takes input from user
Input = input("Enter message: ").upper()
#Blank variable to enter morse code
translation = ""

#Dictionary to define the Morse code for each letter
string_morse_dict = {"A" :".-",
                     "B" : "-...", 
                     "C" : "-.-.", 
                     "D" : "-..",
                     "E" : ".",
                     "F" : "..-.", 
                     "G" : "--.",
                     "H" : "....", 
                     "I" : "..",
                     "J" : ".---", 
                     "K" : "-.-",
                     "L" : ".-..", 
                     "M" : "--",
                     "N" : "-.",
                     "O" : "---",
                     "P" : ".--.", 
                     "Q" : "--.-", 
                     "R" : ".-.",
                     "S" : "...",
                     "T" : "-",
                     "U" : "..-",
                     "V" : "...-", 
                     "W" : ".--",
                     "X" : "-..-", 
                     "Y" : "-.--", 
                     "Z" : "--.."}

#Dictionary to define the letter for each Morse code
morse_string_dict = {".-" : "A",
                      "-..." : "B",
                      "-.-." : "C",
                      "-.."  : "D",
                      "."  : "E",
                      "..-." : "F",
                      "--."  : "G",
                      "...." : "H",
                      ".."  : "I",
                      ".---" : "J",
                      "-.-"  : "K",
                      ".-.." : "L",
                      "--"  : "M",
                      "-."  : "N",
                      "---"  : "O",
                      ".--." : "P",
                      "--.-" : "Q",
                      ".-."  : "R",
                      "..."  : "S",
                      "-"  : "T",
                      "..-"  : "U",
                      "...-" : "V",
                      ".--"  : "W",
                      "-..-" : "X",
                      "-.--" : "Y",
                      "--.." : "Z"}

#for loop that goes through each letter in the input message
#   and enters the code for each letter and puts it in the translation variable
def stringToMorse():
    if Input in string_morse_dict:
        for element in Input:
            if element != " ":
                translation += string_morse_dict[element] + " "
            elif element == ' ':
                translation += "/ "
            else:
                translation += " "
    return translation

#def morseToString():
#    if Input in morse_string_dict:
#        for element in Input:
#            if element != " ":


        

#prints the Morse code of the input message
print("Your message in Morse code: " + translation)
