"""
Robert Fesperman
2026_09_23
Grade Classifier
"""

def classify_grade(grade):
    if grade >= 90:
        letter = "A"
    elif grade >= 80:
        letter = "B"
    elif grade >= 70:
        letter = "C"
    elif grade >= 60:
        letter = "D"
    else:
        letter = "F"
    return letter

def main():
    grades = []
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0
    count_f = 0
    while True:
        user_grade = float(input("Enter a grade (-1 to quit): ".upper()))
        if user_grade == -1:
            break
        grades.append(user_grade)
        print("Letter grade: "+ classify_grade(user_grade))

        if user_grade >= 90:
            count_a += 1
        elif user_grade >= 80:
            count_b += 1
        elif user_grade >= 70:
            count_c += 1
        elif user_grade >= 60:
            count_d += 1
        else:
            count_f += 1

# Make it so that when the user is done entering grades it displays the average grade in number and letter.
# Add all of the grade numbers entered together and then divide by the entries.

    print("Number of grades: "+str(len(grades)))
    print("Average grade: "+str(sum(grades)/len(grades)), end= " ")
    print(classify_grade(sum(grades)/len(grades)))
    print("Max grade: "+str(max(grades)))
    print("Min Grade: "+str(min(grades)))


if __name__ == "__main__":
        main()
