import os
os.system("mkdir io")
os.system("g++ -o run ans.cpp")
for i in range(11):
	print(">",("python3 test_make.py > io/"+"{:0>2d}".format(i) + ".in"))
	os.system("python3 test_make.py > io/"+"{:0>2d}".format(i) + ".in")
	print(">",("./run < io/"+"{:0>2d}".format(i) + ".in > io/" + "{:0>2d}".format(i) + ".out"))
	os.system("./run < io/"+"{:0>2d}".format(i) + ".in > io/" + "{:0>2d}".format(i) + ".out")
	print(">",("python3 ans.py < io/"+"{:0>2d}".format(i) + ".in > io/" + "{:0>2d}".format(i) + ".check"))
	os.system("python3 ans.py < io/"+"{:0>2d}".format(i) + ".in > io/" + "{:0>2d}".format(i) + ".check")
	print()