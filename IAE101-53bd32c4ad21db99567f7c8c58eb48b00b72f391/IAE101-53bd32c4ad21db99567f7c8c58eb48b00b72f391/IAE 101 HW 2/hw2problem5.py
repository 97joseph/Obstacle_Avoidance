# Eshan Shakrani
# 112802596
# eshakrani
#
# IAE 101 (Fall 2021)
# HW 2, Problem 5

def is_palindrome(s):
    left = 0
    right = len(s) - 1
    s = s.lower()
    numbers = list(map(str, range(0,10)))
    letters = [chr(n) for n in range(ord('a'), ord('z') + 1)]
    while (left <= right):
        while ((cl := s[left]) not in numbers and cl not in letters):
            left += 1
        while ((cr := s[right]) not in numbers and cr not in letters):
            right -= 1
        if cr != cl:
            return False
        left += 1
        right -= 1
    return True

# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    test1 = is_palindrome("racecar")
    print("is_palindrome(\"racecar\") is:", test1)
    print()
    test2 = is_palindrome("raceboat")
    print("is_palindrome(\"raceboat\") is:", test2)
    print()
    test3 = is_palindrome("a man a plan a canal panama")
    print("is_palindrome(\"a man a plan a canal panama\") is:", test3)
    print()
    test4 = is_palindrome("a place to call up")
    print("is_palindrome(\"a place to call up\") is:", test4)
    print()
    test5 = is_palindrome("deified")
    print("is_palindrome(\"deified\") is:", test5)
    print()

