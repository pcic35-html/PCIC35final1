import random
import string


def generate_test_data(min_length, max_length):#  回傳隨機字串
	length = random.randint(min_length, max_length)
	s = ''.join(random.choice(string.ascii_letters) for __ in range(length))
	return s
def build_tree(n):#  建樹
	re=[]
	for i in range(n-1):
		re.append([i,random.randint(i+1,n-1)])
	random.shuffle(re)
	return re

N=random.randint(1,100)
print(N)
for _ in range(N):
	print(generate_test_data(1,100))
	print(random.randint(1,100))
print(generate_test_data(1,100))

