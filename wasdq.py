"""
Create a function which gets the user input and returns it.
Do not allow anything other than WASDQ
If something is entered, reprompt for input:
"""

def get_command(valid_inputs):
    user_input = input('Enter a command: ').upper()
    if user_input in valid_inputs:
        return user_input
    else:
        print("Error. Only valid inputs are: ")
        for key in valid_inputs:
            print(key, end = " ")
        print()


def main():
    print("The key you pressed was: "+get_command(["W", "A", "S", "D", "Q"]))


if __name__ == "__main__":
    main()

"""
import
"""
