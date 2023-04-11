# write a python function that takes the name of student,and calculates their ages.
# If the age is greater or equal to 18, it should return true, else false.

stud_name = input("Enter your name: ")
age = int(input("Input your age: "))

print(stud_name)
print(age)

def age_calcular():

    if age >= 18:
        print(True)
    else:
        print(False)

age_calcular()