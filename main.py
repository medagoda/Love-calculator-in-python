print("Welcome to the love calculator")
name1 = input("What is your name :\n")
name2 = input("What is their name :\n")
name1_lower = name1.lower()
name2_lower = name2.lower()

num_of_l = name1_lower.count("l") + name2_lower.count("l")
num_of_o = name1_lower.count("o") + name2_lower.count("o")
num_of_v = name1_lower.count("v") + name2_lower.count("v")
num_of_e = name1_lower.count("e") + name2_lower.count("e")
num_of_t = name1_lower.count("t") + name2_lower.count("t")
num_of_r = name1_lower.count("r") + name2_lower.count("r")
num_of_u = name1_lower.count("u") + name2_lower.count("u")

love_value = str(num_of_l + num_of_o + num_of_v + num_of_e)
true_value = str(num_of_t + num_of_r + num_of_u + num_of_e)

love_calculated_value = true_value + love_value
new = int(love_calculated_value)

if new<10 or new>90:
    print(f"Your score is {new} , you go together like coke and mentos.")
elif 40<new<50:
    print(f"Your score is {new} , you are alright together")
else:
    print(f"Your score is {new}")