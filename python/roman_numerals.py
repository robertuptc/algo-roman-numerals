def to_roman(num):
    output = ""
    romman_numeral_to_arabic = { 
        'M': 1000, 
        'CM': 900, 
        'D': 500, 
        'CD': 400, 
        'C': 100, 
        'XC': 90, 
        'L': 50, 
        'XL': 40, 
        'X': 10, 
        'IX': 9, 
        'V': 5, 
        'IV': 4, 
        'I': 1 
    }
    for key in romman_numeral_to_arabic:
        while num >= romman_numeral_to_arabic[key]:
            output += key
            num -= romman_numeral_to_arabic[key]
    return output



