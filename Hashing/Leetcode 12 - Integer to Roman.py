#  Integer to roman

def solutions1(n):
    roman_symbols = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    # Tuple of the respective values of the Roman numerals
    roman_values = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)

    result = []
    for symbol, value in zip(roman_symbols, roman_values):
        while n >= value:
            n -= value
            result.append(symbol)

    return "".join(result)


n = 3749
print(solutions1(n))