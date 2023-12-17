import random
import string


T = 1000
min_length = 10
max_length = 25
characters = ['a', 'A', 'p', 'P', 'l', 'L', 'e', 'E']

def generate_test_data():
	test_data = ''
	
	# Add 1 'a' or 'A'
	test_data += random.choice(['a', 'A'])
	
	# Add 2 'p' or 'P'
	test_data += random.choice(['p', 'P']) * 2
	
	# Add 1 'l' or 'L'
	test_data += random.choice(['l', 'L'])
	
	# Add 1 'e' or 'E'
	test_data += random.choice(['e', 'E'])
	
	# Add remaining characters randomly
	mxl=random.randint(min_length, max_length)
	for _ in range(mxl - len(test_data)):
		test_data += random.choice(string.ascii_letters)
	
	# Rearrange the string
	test_data = ''.join(random.sample(test_data, len(test_data)))
	
	return test_data

def generate_test_data_2():
	mxl=random.randint(min_length, max_length)
	test_data=""
	c='a'
	for _ in range(mxl):
		while(1):
			c=random.choice(string.ascii_letters)
			if(characters.count(c)==0):
				break
		test_data += c
	return test_data





print(T)
for i in range(T):
	tpe=random.randint(0,1)
	if(tpe):
		print(generate_test_data())
	else:
		print(generate_test_data_2())
