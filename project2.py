introverted_points = 0
extroverted_points= 0
ambiverted_points = 0

answer1 = input("Would you rather A go hang out with friends, B stay home, C hang out with friends for a little bit? ")
if answer1 == "A" or answer1 == "a" or answer1 == " A" or answer1 == " a":
    extroverted_points += 1
elif answer1 == "B" or answer1 == "b" or answer1 == " B" or answer1 == " b":
    introverted_points += 1
elif answer1 == "C" or answer1 == "c" or answer1 == " C" or answer1 == " c":
    ambiverted_points += 1
input("")

answer2 = input("Are you A scared of meeting new people, B neutral about meeting new people, C eager to meet new people? ")
if answer2 == "A" or answer2 == "a" or answer2 == " A" or answer2 == " a":
    introverted_points += 1
elif answer2 == "B" or answer2 == "b" or answer2 == " B" or answer2 == " b":
    ambiverted_points += 1 
elif answer2 == "C" or answer2 == "c" or answer2 == " C" or answer2 == " c":
    extroverted_points += 1 
input("")

answer3 = input("Do you like to A work alone, B work with anyone, C work with only friends? ")
if answer3 == "A" or answer3 == "a" or answer3 == " A" or answer3 == " a":
    introverted_points += 1
elif answer3 == "B" or answer3 == "b" or answer3 == " B" or answer3 == " b":
    extroverted_points += 1
elif answer3 == "C" or answer3 == "c" or answer3 == " C" or answer3 == " c":
    ambiverted_points += 1
input("")

answer4 = input("Do you like to A spend time with friends, B spend time by yourself, C both? ")
if answer4 == "A" or answer4 == "a" or answer4 == " A" or answer4 == " a":
    extroverted_points += 1
elif answer4 == "B" or answer4 == "b" or answer4 == " B" or answer4 == " b":
    introverted_points += 1
elif answer4 == "C" or answer4 == "c" or answer4 == " C" or answer4 == " c":
    ambiverted_points += 1
input("")

answer5 = input("How much do you hang out with your friends weekly? A depends on the week, B 3-7 times a week, C 0-2 times a week. ")
if answer5 == "A" or answer5 == "a" or answer5 == " A" or answer5 == " a":
    ambiverted_points += 1
elif answer5 == "B" or answer5 == "b" or answer5 == " B" or answer5 == " b":
    extroverted_points += 1
elif answer5 == "C" or answer5 == "c" or answer5 == " C" or answer5 == " c":
    introverted_points += 1 
input("")

if introverted_points >= extroverted_points and introverted_points >= ambiverted_points:
    print("You are a introverted person. You might be more shy about meeting new people.")
elif extroverted_points >= introverted_points and extroverted_points >= ambiverted_points:
    print("You are a extroverted person. You like to meet new people!")
elif ambiverted_points >= introverted_points and ambiverted_points >= extroverted_points:
    print("You are an ambiverted person. You like to meet new people but are a little shy.")
else:
    print("I don't know which one you are...")
input("")
print("Thank you for taking this quiz! Have a nice day!")
