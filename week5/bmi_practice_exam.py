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
    """Calculate the users's BMI. weight in kg and height in meters."""
    return weight / height ** 2

def classify_BMI(BMI):
    """Look up table for BMI classes based on BMI calculation"""
    if BMI <= 18:
        return "underweight"
    elif BMI <= 24:
        return "Healthy"
    elif BMI <= 29:
        return "Overweight"
    else:
        return "Obese"


def main():
    """ Initialize aggragate counters """
    count = 0
    total = 0
    min_num = ""
    max_num = ""

    print("This program will calculate the users BMI.")
    while True:
        # Get user input for weight and height
        user_weight = float(input("Enter your weight(kg) or 0 to quit: "))
        if user_weight == "0":
            break
        user_height = float(input("Enter your height(m): "))

        # Calc and classify the BMI. Increment total and count agreggates
        user_BMI = calc_BMI(user_weight, user_height)
        user_BMI_class = classify_BMI(user_BMI)
        print(user_BMI_class)
        count += 1
        total += user_BMI

        # Capture min and max BMI
        if min_num == "" or min_num < user_BMI:
            min_num = user_BMI
        if max_num == "" or max_num > user_BMI:
            max_num = user_BMI

    print("count: "+str(count))
    print("Average: "+str(total/count))
    print("Min BMI: "+str(min_num))
    print("Max BMI: "+str(max_num))

if __name__ == "__main__":
    main()

# Missing for exam: Make sure I understand what scientitifc notation is and how it works in python 1.234 x 10^9 (normal) 1.234e9 (python)(e == 10 to the X power)
