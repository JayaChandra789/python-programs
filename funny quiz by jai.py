def start_quiz():
 ask_user = input("Press 0 to start quiz: ")
 if ask_user == "0":
    print("What is the name of your college?")
    print("a. Avanthi PG College")
    print("b. Avanti PG Kalashala")
    print("c. Avanti PG")
    print("d. Both a & b")
    
    option = input("Enter your option (a/b/c/d): ").lower()
    
    if option == 'd':
        print("+10 marks, remaining 90 to win")
    else:
        print("The answer you have entered is wrong.")
    
    ask_user = input("Press 1 for next question: ")
    
    if ask_user == "1":
        print("Whom do you think is the best faculty in your college?")
        print("a. Manisha Mam")
        print("b. Naveen HOD")
        print("c. Your friend")
        print("d. Enter your answer by pressing 'd'")
        
        option = input("Enter your option (a/b/c/d): ").lower()
        
        if option == "a":
            print("Great, nice answer! +10 marks, 80 remaining to win")
        elif option == "b":
            print("Great, nice answer! -10 marks, 90 remaining to win")
        elif option == "c":
            print("Great, nice answer! +10 marks, 70 remaining to win")
        elif option == "d":
            answer = input("Enter your answer: ")
            print(f"Your answer: is the best faculty is {answer}")
        else:
            print("Invalid option selected.")
    else:
        print("Invalid input for next question.")
 else:
    print("You didn't press 0 to start the quiz. Exiting.")

start_quiz()

