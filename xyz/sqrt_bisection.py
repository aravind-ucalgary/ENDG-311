# https://en.wikipedia.org/wiki/Bisection_method
# f(x) = x^2 - xs
# xs: user input
# 
# finding roots: f(x) = 0 = x^2 -xs -> x = sqrt(xs)
# when we find a root, we have the sqrt of xs
epsilon = 0.01
xs = float(input("Enter a positive real number: "))

# define a, b such that f(a) is negative and f(b) is positive
a = 0 # f(a=0)=-xs -> negative
b = xs # f(b=xs)= xs(xs-1) -> positive

# current guess
c= (a+b) / 2

# count how many iterations
count = 0

# repeat until we are close to zero (root)
while abs(c**2 - xs) >= epsilon:
    #check if f(c) is negative
    if (c**2 - xs) > 0:
        # move a up to c
        a = c
    else:
        # move b down to c
        b = c
    # new guess
    c = a + b / 2
    
    count += 1

print("Square root of {} is close to {} found in {} steps".format(xs, c, count))

