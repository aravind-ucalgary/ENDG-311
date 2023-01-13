# TODO: w01-2 add pytests
# TODO: w01-1 add docstrings and comments

# TODO: w01-1 Turn this into a function
def sqrt_exhaustive(x):
    # TODO: w01-2 make sure x is positive
    guess = 0

    # TODO: w01-1 Replace this with a for loop
    while guess ** 2 < x:
        guess = guess + 1
    
    if guess ** 2 == x:
        return guess
    else:
        return -1


x = int(input("Enter a positive integer: "))

sqrt_of_x = sqrt_exhaustive(x)

# TODO: w01-1 Show f-strings
if sqrt_of_x >= 0:
    # print("Square root of {} is {}".format(x, sqrt_of_x))
    print(f"Square root of {x} is {sqrt_of_x}")
else:
    # print("No square root found for {}".format(x))
    print(f"No square root found for {x}")
