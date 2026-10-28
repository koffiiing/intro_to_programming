"""
Robert Fesperman - Python Practice Drills

HOW TO USE THIS FILE
1. Run it right away. Every drill will say TODO.
2. Pick the first TODO. Replace `pass` with your code, then run the file again.
3. PASS means you're done. FAIL shows you what your function returned and
   what it should have returned. Use that to fix your code.
4. Don't look anything up until you've tried for at least 10 minutes.
   Being stuck and working your way out is how you actually learn this.
5. Once you pass a drill, come back in 2-3 days, delete your answer, and
   write it again from a blank function. The second time is where it sticks.

The drills go in order. Each level uses the skills from the levels before it.
"""

import math

SIGMA = 5.67e-8   # Stefan-Boltzmann constant. Remember: e-8 means x 10^-8 (a tiny number)


# =====================================================================
# LEVEL 1 - Types and math  (input gives you text; math needs numbers)
# =====================================================================

def dollars_to_cents(dollars):
    cents = round(dollars * 100)
    return cents
    """Convert a dollar amount (float) to a whole number of cents (int).
    dollars_to_cents(1.78) -> 178
    HINT: Try int(0.29 * 100) in the Python shell first and see what you get.
          Then try round() instead of int(). Why is there a difference?
    """
def main():
    print("This program converts dollar amounts to cents")
    dollars = float(input("Please enter a dollar amount: $"))
    cents = dollars_to_cents(dollars)
    print(f"${dollars} is {cents} in cents!")

if __name__ == "__main__":
    main()


def least_coins(cents):
    """Return the fewest quarters, dimes, nickels, and pennies for `cents`,
    as a tuple: (quarters, dimes, nickels, pennies)
    least_coins(178) -> (7, 0, 0, 3)
    HINT: `//` tells you how many whole coins fit.
          `%`  tells you how much is left over after that.
          178 // 25 = 7 quarters, and 178 % 25 = 3 cents left for the other coins.
    """
    pass


def calc_luminosity(radius, temp):
    """Luminosity of a star: L = 4 * pi * radius^2 * SIGMA * temp^4
    Use the SIGMA constant at the top of this file. Don't type the number in again.
    calc_luminosity(6.957e8, 5772) -> about 3.83e26   (that's our Sun)
    """
    pass


# =====================================================================
# LEVEL 2 - Decisions  (if / elif / else, and the order you check things)
# =====================================================================

def classify_bmi(bmi):
    """Return "Underweight" (below 18.5), "Healthy" (below 25),
    "Overweight" (below 30), or "Obese" (30 and up).
    classify_bmi(24.9) -> "Healthy"      classify_bmi(25) -> "Overweight"
    """
    pass


def fizzbuzz_word(n):
    """Return "FizzBuzz" if n is divisible by 3 AND 5, "Fizz" if only by 3,
    "Buzz" if only by 5, and otherwise the number as a string.
    fizzbuzz_word(15) -> "FizzBuzz"     fizzbuzz_word(7) -> "7"
    HINT: Which check has to come FIRST in the if/elif chain? Why?
    """
    pass


# =====================================================================
# LEVEL 3 - Loops, accumulators, and counters
#           Don't use the built-in sum(), min(), max(), or .count().
#           The point is to write the loop yourself.
# =====================================================================

def sum_to(n):
    """Add up 1 + 2 + ... + n.   sum_to(5) -> 15
    HINT: start a total at 0 and add to it inside a for loop (range).
    """
    pass


def count_evens(numbers):
    """Count how many numbers in the list are even.   count_evens([1, 2, 3, 4]) -> 2"""
    pass


def find_min(numbers):
    """Return the smallest number in a non-empty list.   find_min([4, 2, 9]) -> 2
    HINT: Say what you're checking out loud:
          "if THIS number is SMALLER than the smallest so far..."
          then turn that sentence into code.
    """
    pass


def find_max(numbers):
    """Return the largest number in a non-empty list.   find_max([4, 2, 9]) -> 9"""
    pass


def average(numbers):
    """Return the average of the list. If the list is empty, return 0
    (don't divide by zero!).   average([90, 80, 70]) -> 80.0
    """
    pass


def count_letter(text, letter):
    """Count how many times `letter` appears in `text` (case matters).
    count_letter("banana", "a") -> 3
    """
    pass


def is_whole_number(text):
    """Return True if `text` is made up of only digits 0-9 and isn't empty.
    Otherwise return False.
    is_whole_number("42") -> True     is_whole_number("4.2") -> False
    is_whole_number("") -> False      is_whole_number("-3") -> False
    (You wrote this logic already in get_whole_number. Try it without looking.)
    """
    pass


# =====================================================================
# LEVEL 4 - Putting it together
# =====================================================================

def slot_result(a, b, c):
    """Given three slot symbols, return "jackpot" if all three match,
    "pair" if exactly two match, or "lose" if none of them match.
    slot_result("7", "7", "7") -> "jackpot"
    slot_result("Lemon", "Bar", "Lemon") -> "pair"
    """
    pass


def summarize_grades(grades):
    """Return (count, average, lowest, highest) for a list of grades.
    For an empty list, return (0, 0, None, None).
    summarize_grades([90, 80, 70, 100]) -> (4, 85.0, 70, 100)
    This is the same count/total/min/max pattern from grade_classifier and
    the BMI program. Do it in ONE loop.
    """
    pass


# =====================================================================
# FULL PROGRAM CHALLENGES  (these use input(), so you test them by hand)
# Make a new file for each one. Start from a blank file every time.
# =====================================================================
#
# A. COIN CHANGE: Ask for a dollar amount, then print the fewest coins.
#    Use your dollars_to_cents() and least_coins() functions.
#
# B. STAR LUMINOSITY (redo your exam): Keep asking for a radius. Quit
#    RIGHT AWAY if they type 0, before asking for the temperature. Reject
#    negative numbers with a message. Use calc_luminosity(). When they
#    quit, print how many stars they checked and the brightest one.
#
# C. BMI TRACKER: Keep asking for weight (0 to quit) and height. Print each
#    BMI's class. When they quit, print the count, average, min, and max.
#    Test it: what happens if they type 0 on the very first prompt?
#
# D. SLOT MACHINE: Start with a bankroll of 100. Ask for a bet (can't be more
#    than the bankroll). Spin 3 random symbols, store them in variables,
#    and use slot_result(). Jackpot pays 10x the bet, a pair pays 2x, and a
#    loss costs the bet. Keep going until they quit or run out of money.
#
# =====================================================================
#                 TEST RUNNER - you don't need to edit below
# =====================================================================

def _same(result, expected):
    if isinstance(expected, bool):
        return isinstance(result, bool) and result == expected
    if isinstance(expected, float):
        return isinstance(result, (int, float)) and not isinstance(result, bool) \
            and math.isclose(result, expected, rel_tol=1e-3, abs_tol=1e-12)
    if isinstance(expected, tuple):
        return isinstance(result, tuple) and len(result) == len(expected) and all(
            _same(r, e) for r, e in zip(result, expected))
    return type(result) == type(expected) and result == expected


def _check(func, cases):
    name = func.__name__
    for i, (args, expected) in enumerate(cases):
        try:
            result = func(*args)
        except Exception as error:
            print(f"  FAIL  {name}{args} crashed -> {type(error).__name__}: {error}")
            return False
        if i == 0 and result is None:
            print(f"  TODO  {name}")
            return False
        if not _same(result, expected):
            print(f"  FAIL  {name}{args}")
            print(f"          you returned: {result!r}")
            print(f"          expected:     {expected!r}")
            return False
    print(f"  PASS  {name}")
    return True


def _run_all():
    tests = [
        ("LEVEL 1 - Types and math", [
            (dollars_to_cents, [((1.78,), 178), ((0.29,), 29), ((5,), 500), ((0.07,), 7)]),
            (least_coins, [((178,), (7, 0, 0, 3)), ((41,), (1, 1, 1, 1)),
                           ((99,), (3, 2, 0, 4)), ((0,), (0, 0, 0, 0))]),
            (calc_luminosity, [((6.957e8, 5772), 3.828e26), ((1.0, 1.0), 4 * math.pi * 5.67e-8)]),
        ]),
        ("LEVEL 2 - Decisions", [
            (classify_bmi, [((17.0,), "Underweight"), ((18.5,), "Healthy"), ((24.9,), "Healthy"),
                            ((25,), "Overweight"), ((29.9,), "Overweight"), ((30,), "Obese")]),
            (fizzbuzz_word, [((3,), "Fizz"), ((5,), "Buzz"), ((15,), "FizzBuzz"),
                             ((7,), "7"), ((30,), "FizzBuzz"), ((9,), "Fizz")]),
        ]),
        ("LEVEL 3 - Loops and accumulators", [
            (sum_to, [((5,), 15), ((1,), 1), ((100,), 5050), ((0,), 0)]),
            (count_evens, [(([1, 2, 3, 4],), 2), (([7],), 0), (([0, 10, 12],), 3), (([],), 0)]),
            (find_min, [(([4, 2, 9],), 2), (([-5, -1],), -5), (([3],), 3), (([9, 8, 7],), 7)]),
            (find_max, [(([4, 2, 9],), 9), (([-5, -1],), -1), (([3],), 3), (([7, 8, 9],), 9)]),
            (average, [(([90, 80, 70],), 80.0), (([5],), 5.0), (([1, 2],), 1.5), (([],), 0.0)]),
            (count_letter, [(("banana", "a"), 3), (("Robert", "r"), 1),
                            (("Robert", "R"), 1), (("", "x"), 0)]),
            (is_whole_number, [(("42",), True), (("",), False), (("4.2",), False),
                               (("-3",), False), (("abc",), False), (("007",), True)]),
        ]),
        ("LEVEL 4 - Putting it together", [
            (slot_result, [(("7", "7", "7"), "jackpot"), (("Lemon", "Bar", "Lemon"), "pair"),
                           (("Bar", "Bar", "Cherry"), "pair"), (("Melon", "7", "7"), "pair"),
                           (("Lemon", "Bar", "7"), "lose")]),
            (summarize_grades, [(([90, 80, 70, 100],), (4, 85.0, 70, 100)),
                                (([55],), (1, 55.0, 55, 55)),
                                (([70, 95, 60],), (3, 75.0, 60, 95)),
                                (([],), (0, 0.0, None, None))]),
        ]),
    ]
    passed = total = 0
    for level_name, level_tests in tests:
        print(f"\n{level_name}")
        for func, cases in level_tests:
            total += 1
            if _check(func, cases):
                passed += 1
    print(f"\n{passed} / {total} drills passing.")
    if passed == total:
        print("All done! Now go do the full program challenges near the bottom of this file.")


if __name__ == "__main__":
    _run_all()
