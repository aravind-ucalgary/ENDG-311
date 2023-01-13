# TODO: w01-2 add pytests
# see sqrt_exhaustive_test.py
# TODO: w01-1 add docstrings and comments


# TODO: w01-1 Turn this into a function
def sqrt_exhaustive(x):
    """ Searches for integers that would be square-root of x

        x(int): Value to search the square root of

        returns: (int or None) Square-root of x if found
    
    """

    # TODO: w01-2 make sure x is positive
    assert x > 0, f"argument x={x} needs to be positive"

    guess = 0

    # TODO: w01-1 Replace this with a for loop
    for guess in range(x + 1):
        if guess ** 2 == x:
            return guess
    return None

    # while guess ** 2 < x:
    #     guess = guess + 1

    # # Check if the loop found a result
    # if guess ** 2 == x:
    #     return guess
    # else:
    #     return None


def main():
    x = int(input("Enter a positive integer: "))

    res = sqrt_exhaustive(x)

    # TODO: w01-1 Show f-strings
    # Sometimes we do not find a result.
    if res is not None:
        # print("Square root of {} is {}".format(x, res))
        print(f"Square root of {x} is {res}")
    else:
        # print("No square root found for {}".format(x))
        print(f"No square root found for {x}")


if __name__ == "__main__":
    main()
