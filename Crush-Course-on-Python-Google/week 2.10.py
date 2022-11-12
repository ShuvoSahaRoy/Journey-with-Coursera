def fractional_part(numerator, denominator):
    # Operate with numerator and denominator to
# keep just the fractional part of the quotient
    if numerator!= 0 and denominator !=0:
        a = numerator/denominator
        b = numerator//denominator
        return a-b
    else:
        return 0

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0