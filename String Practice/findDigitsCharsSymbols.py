def findDigitsCharsSymbols(str1):
    char_count = 0
    digit_count = 0
    symbols_count = 0

    for i in str1:
        if i.isnumeric():
            digit_count += 1
        elif i.islower() or i.isupper():
            char_count += 1
        else:
            symbols_count += 1
    print("Chars = ", char_count, "Digits = ", digit_count, "Symbol = ", symbols_count)


findDigitsCharsSymbols("P@#yn26at^&i5ve")
