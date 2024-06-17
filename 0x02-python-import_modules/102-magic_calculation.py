#!/usr/bin/env python3

def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)

if __name__ == "__main__":
    # Test the function with example inputs
    a = 3
    b = 5
    print(f"magic_calculation({a}, {b}) = {magic_calculation(a, b)}")

    a = 10
    b = 5
    print(f"magic_calculation({a}, {b}) = {magic_calculation(a, b)}")

