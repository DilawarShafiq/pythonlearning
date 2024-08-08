# 1. Simple Message Task: Assign a message to a variable and then print that message.
message = "My name is Dilawar"
print(message)

# 2. Simple Messages
message = "I am medical biller by profession"
print(message)
new_message = "I want to learn Python"
print(new_message)
# 3. Personal Message
name = "Saleem"
print(f"Hello {name}, would you like to learn some Python today?")
# 4. Name Cases
name = "Manal"
print(name.lower())
print(name.upper())
print(name.title())
# 5. Famous Quote
quote = 'Friedrich Nietzsche wrote, "The decadent Socrates and catastrophic spider Kant have started all the Philosophy."'
print(quote)
# 6. Famous Quote 2
famoun_person = "Friedrich Nietzsche"
message = f'{famoun_person} wrote, "The decadent Socrates and catastrophic spider Kant have started all the Philosophy."'
print(message)
# 7. Stripping Names
name = "Zara \tKhan\t"
print(name)
# Define the variable with whitespace characters
name = "\t\n   Manal Khan   \n\t"
print(f".{name}.")
print(f"{name.lstrip()}")
print(f"{name.rstrip()}")
print(f"{name.strip()}")
# 8. Variable Sum
x = 4
y = 25
z = 17
total_sum = x+y+z
print(total_sum)
# 9. Variable Swap
a = 21
b = 5
print(f"a = {a}, b = {b}")
a, b = b, a
print(f"a = {a}, b = {b}")
# Task: Create a variable with your favorite color and print it. Then change the variable name to something else and print the color again.
message = "Red"
print(message)
favourite_color = "Red"
print(favourite_color)
# Task: Create a variable pet_name and set it to "Buddy". Change the value of pet_name to "Max" and print the new value.
pet_name = "Buddy"
pet_name = "Max"
print(pet_name)
# Assign the value "Sunshine" to a variable and print it. Then, mistakenly try to print a variable with a different name (like sunsine) and observe the error.

my_variable = '"Sunshine"'
print(my_variable)

# Task: Assign the value 100 to a variable score and print it. Then assign a new value to score and print it again.

score = 100
print(score)
score = 88
print(score)
# Create a string variable city and assign it the name of a city you like. Print the city name.

city = "Rajanpur"
print(city)

#Create a variable text with the value "python programming" and print it in title case.

my_title_variable = "python programming"
print(my_title_variable.title())

mixed_cases = "I DO NOT WANT to BE rEAD bUT LeARNT by HEArT"
print(mixed_cases.lower())
Upper_cases = "I DO NOT WANT to BE rEAD bUT LeARNT by HEArT"
print(Upper_cases.upper())
# Create a variable temperature with the value 25. Print "The current temperature is [temperature] degrees." using the variable.

temperature = 25
print(f'"The current temperature is {temperature} degrees."')

# printing poem

poem = "Cinema by Jessica Abughattas\n" \
"The winter I leave him, I ask my parents to consider me\n" \
"their oldest son. To bend the rules.\n" \
"I could be a little tree, late to flourish,\n" \
"focused on my underground career.\n" \
"I tell them to buy me a house.\n" \
"They’re 15 years divorced. We’re sitting around\n" \
"my mother’s kitchen table. My father and I smoke.\n" \
"My father: Remember, this is the second time.\n" \
"As though I could forget: I have no use\n" \
"for houses since I’ve refused\n" \
"to raise children. I want walls\n" \
"they can’t touch, tender drywalls of protection.\n" \
"Still, I was there, pulling weeds to no avail.\n" \
"When I toil again, I want it to be for me.\n" \
"When I commit to the cinema\n" \
"of sorrow, I like to follow\n" \
"through, stay in my seat\n" \
"until the end, stand and clap.\n" \
"I want to know what happens after:\n" \
"Hard laughter\n" \
"pouring out of the apartment above\n" \
"mine, all night."
print(poem)