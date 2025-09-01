#fstring- used for string formatting
#old method of formatting strings
letter="hey my name is {} and im from {}"
country="india"
name="sam"
print(letter.format(name,country))
#f string method
print(f"hey my name is {name} and im from {country}")
#example
city=input("enter your city: ")
name1=input("enter your name: ")
print(f"your name is {name1} and you are from {city} city")

