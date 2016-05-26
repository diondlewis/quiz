

# A list of blank spaces in numerical order to be passed in to the play game function for the user to put in the answer.
answer_spaces = ["__1__", "__2__", "__3__", "__4__"]

# This the first level of the quiz.
easy_level = """\nYou have chosen easy. You are to be commended for enjoying the simple things in life.
Some simple things that programmers enjoy in Python is the use of a single equal sign to assign a value to a __1__.
These values are classified into various data types. For example 4 is an __2__, but 'Hello World' is a __3__. 
Creating a __4__ is as simple as putting different comma-separated values between square brackets.\n"""

# This is the second level of the quiz.
medium_level = """\nYour choice was not an easy one, literally. Kudos to you for choosing medium and having an adventureous spirit.
Many beginning programmers find the difference between the __1__ statement and the return statement to be a difficult choice. 
You can think of the __1__ statement as something that takes an object from the land of the program and makes it visible 
to the land of the human observer. It is very useful for understanding how a __2__ works and can be used in debugging to 
check various values in a __2__ without interrupting it. The return statement is the main way a __2__ returns a __3__. 
An __4__ is a combination of values, variables, and operators. Although they contain values, variables, and operators, 
not every __4__ contains all of these elements.\n"""

# This is the third level of the quiz. 
hard_level = """\nYou have laughed at easy and want nothing to do with medium. You are a true champion that desires a real challenge.
Since problem solving can be a real challenge in programmers write a detailed yet readable description of what a 
computer program or algorithm must do. This description is called __1__ and is expressed in natural language rather than 
in a programming language. After writing some __1__, you can create a function by using typing in def, the name of the function, 
parentheses, and finally a colon. An __2__ statement tells your script, "If this boolean expression is True, then run the code 
under it, otherwise skip it." A __3__ loop can only iterate (loop) "over" collections of things. A __4__ 
loop can do any kind  of iteration (looping) you want.\n"""

# These are the answers for each level of the quiz.
easy_answers = ["variable", "integer", "string", "list"]
medium_answers = ["print", "function", "value", "expression"]
hard_answers = ["pseudocode", "if", "for", "while"]

print "Welcome to a quiz that tests your knowledge of the programming language Python.\n"

# This will ask the user to choose a level: easy, medium, or hard. ase and return
user_choice = raw_input("Please enter a quiz difficulty level. Possible choices are easy, medium, or hard.\n").lower()


def level_choice(user_choice):
    '''This function will take as input the raw_input from the user and return as output the quiz level they selected.'''
    if user_choice == "easy":
        return easy_level
    if user_choice == "medium":
        return medium_level
    if user_choice == "hard":
            return hard_level
    else:
        return "That is not one of the options listed, please try again." 

print level_choice(user_choice)


def level_answers(user_choice):
    '''This function takes as input the raw_input from user_choice and returns as output the 
    list of answers that matches the level they chose.'''
    if level_choice(user_choice) == easy_level:
        return easy_answers
    if level_choice(user_choice) == medium_level:
        return medium_answers
    if level_choice(user_choice) == hard_level:
        return hard_answers


def right_wrong_answer(user_answer, answers, check_answers_index): 
    '''This function takes in as input 3 parameters and checks the user response with the answer list 
    and returns a boolean value True or False for the right or wrong answer.'''  
    if user_answer == answers[check_answers_index]:        
        return True
    return False


def start_quiz():
    '''This function is the actual quiz. It will take in as input the quiz_selection variable, which points to the value returned 
    by the level_choice function to choose which level the quiz will start on.'''
    quiz_selection = level_choice(user_choice)
    answers = level_answers(user_choice)   
    answer_spaces_index = 0 
    check_answers_index = 0 
    while answer_spaces_index < len(answer_spaces):
        while check_answers_index < len(answers):
            user_answer = raw_input("What word should replace" + answer_spaces[answer_spaces_index] + "?\n")
            while right_wrong_answer(user_answer, answers, check_answers_index) == False: 
                user_answer = raw_input("That is incorrect, please try again.\n" + "What word should replace" + answer_spaces[answer_spaces_index] + "?\n")
            if right_wrong_answer(user_answer, answers, check_answers_index) == True:
                print "That is correct!" 
                quiz_selection = quiz_selection.replace(answer_spaces[answer_spaces_index], user_answer) 
                print quiz_selection
                answer_spaces_index += 1 
                check_answers_index += 1 
                
    print "Great job! You are awesome!"
            
print start_quiz()



