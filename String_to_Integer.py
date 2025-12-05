#Just understood the concept alone
def myAtoi(s):
    INT_MAX = 2**31 - 1   # 2147483647
    INT_MIN = -2**31      # -2147483648

    i = 0
    n = len(s)

    # 1. Skip leading whitespace
    while i < n and s[i] == ' ':
        i += 1

    # If only whitespace
    if i == n:
        return 0

    # 2. Check sign
    sign = 1
    if s[i] == '-':
        sign = -1
        i += 1
    elif s[i] == '+':
        i += 1

    # 3. Convert digits
    num = 0
    digits_found = False

    while i < n and s[i].isdigit():
        digits_found = True
        digit = ord(s[i]) - ord('0')   # convert char → digit manually
        num = num * 10 + digit
        i += 1

        # Check overflow on the fly
        if sign == 1 and num > INT_MAX:
            return INT_MAX
        if sign == -1 and -num < INT_MIN:
            return INT_MIN

    # If no digits found
    if not digits_found:
        return 0

    # 4. Apply sign
    num = num * sign

    return num
