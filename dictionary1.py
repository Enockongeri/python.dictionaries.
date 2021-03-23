ideantification_number=input("enter your ID NO please")
number_mapping = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "0":"zero"
}
output = ""
for numerals in ideantification_number:
    output += number_mapping.get(numerals, "!") +" "
print(output)