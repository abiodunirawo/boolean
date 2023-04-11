
1. # Write a function that return bool type

# bool

pass_mark = 50
user_score = 50

def pass_fail():

    if user_score >= pass_mark:
       student_passed = True
    else:
       student_passed = False

    if student_passed:
       print("student passed")
    else:
       print("student did not pass")        

pass_fail()