import os
for i in range(11):
	print(">",("./run < io/"+"{:0>2d}".format(i) + ".in > io/" + "{:0>2d}".format(i) + ".out"))
	os.system("./run < io/"+"{:0>2d}".format(i) + ".in > io/" + "{:0>2d}".format(i) + ".out")