class FactorialErrors():
    error_n_is_below_0 = "Sorry, factorial does not exist for negative numbers"
    error_n_is_0 = "The factorial of 0 is 1"


def recursive_factorial(n):
    if n < 0:
        return FactorialErrors.error_n_is_below_0
    if n == 0:
        return FactorialErrors.error_n_is_0
    if n == 1:
        return n
    else:
        return n * recursive_factorial(n - 1)


assert recursive_factorial(-1) is FactorialErrors.error_n_is_below_0
assert recursive_factorial(0) is FactorialErrors.error_n_is_0
print(recursive_factorial(7))
