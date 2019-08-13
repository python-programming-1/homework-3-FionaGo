def collatz():
    """A function to replicate Collatz Conjecture

    Parameters
    ----------
    num: integer

    Returns
    -------
    Print out all computed results

    Raises
    ------
    Raise value error if a non integer was input by the user.

    Notes
    -----
    This function will perform the below computations:
    The coltz conjecture takes a user input integer,
        evaluating whether the number is an even or an odd:
        If it's even, coltz will print and return the number //2.
        If it's odd, coltz will print and return 3*num + 1

    References
    ----------
    https://en.wikipedia.org/wiki/Collatz_conjecture

    """
    while True:
        try:
            num = int(input('Hey you, I\'m Collatz! Please enter a positive integer:'))
            while num != 1:
                if num == 0:
                    print("Zero is not a positive integer, try again!")
                    break
                elif num % 2 == 0:
                    num = num // 2
                elif num % 2 == 1:
                    num = num * 3 + 1
                print(num)

        except ValueError:
            print("The input was not a valid integer. Please rerun the program and input a postive integer!")
            break

        finally:
            return num


if __name__ == "__main__":
    collatz()
