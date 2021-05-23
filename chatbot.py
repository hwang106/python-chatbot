#declaring global variables to be shared by later functions
#sum_mp will be the sum of all the grades available in the existing marking periods
sum_mp = 0
#max_mp will be the total marking periods at the end of the school year
max_mp = 0
#number_mp will be the number of marking periods that have finished
number_mp = 0

#function that validates marking period grade input from user and returns input as float if validation successful.
def validate_input(mp):
    if("%" in mp):
        print("Please type your grade without a percent sign.")
        mp = input("What did you get for the 1st marking period? \n") 
        return validate_input(mp)

    try: 
        mp = float(mp)
        return mp

    except ValueError:
        print("You did not type in a number. Try again.")
        mp = input("What did you get for the 1st marking period? \n")
        return validate_input(mp)

#function that asks user for initial information about marking periods that are used throughout the program
def initial_input():
    global sum_mp
    global number_mp
    global max_mp
    number_mp = input("How many marking periods do you have a grade for so far this school year? \n")
    #the validate_input function was designed to return a float input, hence the int casting for use in for loops
    number_mp = int(validate_input(number_mp))
    
    max_mp = input("How many total marking periods are there at the end of the school year? \n")
    #again appropriating the validate_input function out of laziness and int casting the return for use in for loops
    max_mp = int(validate_input(max_mp))

    #did not end up using list structure, but could be useful for storing grades for multiple classes to calculate something like GPA    
    #grade_list = []
    #iterates user input for existing grades
    for x in range(number_mp):
        mp = input("What did you get for marking period " + str(x+1) + "? \n")
        mp = validate_input(mp)
        sum_mp += mp
        #grade_list.append(mp)

#function that calculates the average grade of existing marking periods and prints the result
def avg_grade(sum, mps):
    avg = sum / mps
    print("Your current average is " + str(round(avg, 2)) + ".")

#function that calculates the minimum average needed for remaning marking periods and prints the result
def min_avg(sum, total_mps, mps):
    grade_target = input("What average grade would you like to get at the end of the year? \n")
    grade_target = validate_input(grade_target)
    grade_needed = ((grade_target * total_mps) - (sum)) / (total_mps - mps)    
    print("You will need a minimum average of " + str(round(grade_needed, 2)) + " for the remaining " + str(total_mps - mps) + " marking periods.")

#function used for flow control at the end of initial calculation
def ending_choice():
    global sum_mp
    global number_mp
    global max_mp
    end_choice = input("Would you like to 1) calculate another average, 2) figure out the minimum average you need for the remaining marking period, or 3) end here? \n")
    while(end_choice != "1" and end_choice != "2" and end_choice != "3"):
        print("Sorry, you have to type either 1, 2, or 3")
        print("This grade calculator can determine 1) your current average or 2) the minimum average you need to reach a target grade.")
        end_choice = input("Would you like to 1) calculate another average, 2) figure out the minimum average you need for the remaining marking period, or 3) end here? \n")
    if(end_choice == "1"):
        initial_input()
        avg_grade(sum_mp, number_mp)
        ending_choice()
    elif(end_choice == "2"):
        min_avg(sum_mp, max_mp, number_mp)
        ending_choice()
    else:
        return


#main
print("This grade calculator can determine 1) your current average or 2) the minimum average you need to reach a target grade.")

calc_choice = input("What would you like the grade calculator to do for you? \n")

while(calc_choice != "1" and calc_choice != "2"):
    print("Sorry, you have to type either 1 or 2")
    print("This grade calculator can determine 1) your current average or 2) the minimum average you need to reach a target grade.")
    calc_choice = input("What would you like the grade calculator to do for you? \n")

initial_input()

if(calc_choice == "1"):
    avg_grade(sum_mp, number_mp)
    ending_choice()
    
else:
    min_avg(sum_mp, max_mp, number_mp)
    ending_choice()


