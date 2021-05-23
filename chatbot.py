number_mp = 0

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

print("This grade calculator can determine 1) your current average or 2) the minimum average you need to reach a target grade.")

calc_choice = input("What would you like the grade calculator to do for you? \n")

while(calc_choice != "1" and calc_choice != "2"):
    print("Sorry, you have to type either 1 or 2")
    print("This grade calculator can determine 1) your current average or 2) the minimum average you need to reach a target grade.")
    calc_choice = input("What would you like the grade calculator to do for you? \n")

if(calc_choice == "1"):
    mp1 = input("What did you get for the 1st marking period? \n")
    mp1 = validate_input(mp1)
    mp2 = input("What did you get for the 2nd marking period? \n")
    mp2 = validate_input(mp2)
    mp3 = input("What did you get for the 3rd marking period? \n")
    mp3 = validate_input(mp3)
    mp4 = input("What did you get for the 4th marking period? \n")
    mp4 = validate_input(mp4)
    avg = (mp1 + mp2 + mp3 + mp4) / 4
    print("Your current average is " + str(round(avg, 2)) + ".")

else:
    grade_target = float(input("What grade would you like to get at the end of the year? \n"))
    mp1 = input("What did you get for the 1st marking period? \n")
    mp1 = validate_input(mp1)
    mp2 = input("What did you get for the 2nd marking period? \n")
    mp2 = validate_input(mp2)
    mp3 = input("What did you get for the 3rd marking period? \n")
    mp3 = validate_input(mp3)
    grade_needed = (grade_target * 4) - (mp1 + mp2 + mp3)    
    print("You will need a minimum average of " + str(round(grade_needed, 2)) + ".")


