# This function a number, numerator, and another to divide the first by, denominator.
def oldDivisor(numerator, denominator):
    signCounter = -1 if numerator < 0 or denominator < 0 else 1
    numerator = abs(numerator)
    denominator = abs(denominator)

    
    quotient = 0
    while numerator >= denominator:
        numerator = numerator - denominator
        quotient += 1

    quotient *= signCounter
    return quotient

print(oldDivisor(-20, 5))

