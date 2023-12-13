import random
import string

def generate_test_data(T, min_length, max_length):
	test_data = []
	total_length = 0
	for _ in range(T):
		remaining_length = int(1e8) - total_length
		if remaining_length <= 0:
			break
		length = random.randint(min_length, min(max_length, remaining_length))
		if total_length + length > int(1e8):
			length = int(1e8) - total_length
		s = ''.join(random.choice(string.ascii_letters) for __ in range(length))
		test_data.append(s)
		total_length += length
	return test_data


T = int(1e5)
min_length = 1
max_length = 100
test_data = generate_test_data(T, min_length, max_length)
print(len(test_data))
for i in test_data:
	print(i)

