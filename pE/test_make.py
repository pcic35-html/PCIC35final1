import random
import math

operators = ['+', '-', '*', '/', '%']
functions = ['math.sin', 'math.cos', 'math.tan','']
random_function = random.choice(functions)
random_operator = random.choice(operators)
random_argument1 = random.uniform(0, 1)
random_argument2 = random.uniform(0, 1)
test_data = (f"{random_function}({random_argument1}){random_operator}{random_function}({random_argument2})").replace(" ", "")
expected_result = eval(test_data)

print(test_data)
