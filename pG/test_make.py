import random
import string

def generate_test_data(min_length, max_length):
	length = random.randint(min_length, max_length)
	s = ''.join(random.choice(string.ascii_letters) for __ in range(length))
	return s


min_length = 1
max_length = 100
test_data = generate_test_data(min_length, max_length)
test_data_b=generate_test_data(min_length,max_length)


a=random.randint(0,1)
if(a):
	print(test_data+"小ㄌㄌ"+test_data_b)
else:
	print(test_data+test_data_b)

