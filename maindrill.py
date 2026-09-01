# arithmetic functions
from pyscript import display, document

# addition
def adding_numbers(e):
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    sum = first_number + second_number

    display(f'The sum of {first_number} and {second_number} is {sum}', target='result1')

# subtraction
def subtracting_numbers(e):
    third_number = float(document.getElementById('num3').value)
    fourth_number = float(document.getElementById('num4').value)
    dif = third_number - fourth_number
    
    display(f'The difference of {third_number} and {fourth_number} is {dif}', target='result2')

# multiplication
def multiplying_numbers(e):
    fifth_number = float(document.getElementById('num5').value)
    sixth_number = float(document.getElementById('num6').value)
    product = fifth_number * sixth_number
    
    display(f'The product of {fifth_number} and {sixth_number} is {product}', target='result3')

# exponentiation
def exponentiating_numbers(e):
    seventh_number = float(document.getElementById('num7').value)
    eighth_number = float(document.getElementById('num8').value)
    exponent = seventh_number ** eighth_number
    
    display(f'The product of {seventh_number} raised to the power of {eighth_number} is {exponent}', target='result4')

# float division
def floatdividing_numbers(e):
    ninth_number = float(document.getElementById('num9').value)
    tenth_number = float(document.getElementById('num10').value)
    quotient = ninth_number / tenth_number
    
    display(f'The true quotient of {ninth_number} and {tenth_number} is {quotient}', target='result5')

# floor division
def floordividing_numbers(e):
    eleventh_number = float(document.getElementById('num11').value)
    twelveth_number = float(document.getElementById('num12').value)
    quotientalt = eleventh_number // twelveth_number
    
    display(f'The rounded-down quotient of {eleventh_number} and {twelveth_number} is {quotientalt}', target='result6')

# modulo or remainder
def gettingtheremainderof_numbers(e):
    thirteenth_number = float(document.getElementById('num13').value)
    fourteenth_number = float(document.getElementById('num14').value)
    modulo = thirteenth_number % fourteenth_number

    display(f'The remainder of the numbers {thirteenth_number} and {fourteenth_number} is {modulo}', target='result7')
