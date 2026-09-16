import math

# Calc Circle 1 circumference
# side^2 + side^2 = C^2
d = 230.4 * math.sqrt(2)
# solve for c (squae root it)
print(d)
# calculate circumference using d
c1 = d * math.pi
print(c1)


# Option C calculations
d = 230.4 * math.sqrt(2)
c1 = d * math.pi # calculate circumference using c
c2 = math.pi * 230.4
answer = c1 - c2

print(c2)
