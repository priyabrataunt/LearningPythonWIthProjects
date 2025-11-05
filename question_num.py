questions = (("What is the Capital of India"),
            ("Who is the Prime Minister of India"),
            ("What is the President name of India"),
            ("Who was the first prime minister of India"),
            ("When was the India got independence"))

options = (("A. Mumbai", "B. New York", "C. Delhi", "D. Hyderabad"), 
           ("A. Rahul Gandhi", "B. Donald Trump", "C. Modi", "D. Lalu Yadav"),
           ("A. Draupadi Murmu", "B. Vascodi Gamma", "C. Rahul Shukla", "D. Narendra modi"), 
           ("A. Jawaharlal nehru", "B. Draupadi murmu", "C. Rahul gandhi", "D. George Wahington"),
           ("A. 1945", "B. 1947", "C. 1950", "D. 1974"))

answers = ("C", "C", "A", "A", "B")

guessses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Choose an option").upper()
    guessses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
    