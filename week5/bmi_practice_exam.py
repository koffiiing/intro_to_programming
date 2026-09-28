"""
Robert Fesperman
2026_09_28
BMI Practice
"""

def get_user_input(prompt):
    print(prompt)
    # loop
        # Get uer input
        # if it is what you want:
            # return

def calc_BMI(weight, height):
    return weight / height ** 2

def classify_BMI(BMI):
    if BMI <= 18:
        return "underweight"
    elif BMI <= 24:
        return "Healthy"
    elif BMI <= 29:
        return "Overweight"
    else:
        return "Obese"


def main():
    count = 0
    total = 0
    min_num = ""
    max_num = ""
    while True:
        user_weight = float(input("Enter your weight(kg) or 0 to quit: "))
        if user_weight == 0:
            break
        user_height = float(input("Enter your height(m): "))
        user_BMI = calc_BMI(user_weight, user_height)
        user_BMI_class = classify_BMI(user_BMI)
        print(user_BMI_class)
        count += 1
        total += user_BMI


        if min_num == "" or min_num < user_BMI:
            min_num = user_BMI
        if max_num == "" or max_num < user_BMI:
            max_num = user_BMI

    print("count: "+str(count))
    print("Average: "+str(total/count))
    print("Min BMI: "+str(min_num))
    print("Max BMI: "+str(max_num))

if __name__ == "__main__":
    main()
