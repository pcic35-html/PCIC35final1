T=int(input())
for _ in range(T):
	str=input()
	str=str.lower()
	ispass=True

	if(str.count("a")<1):
		ispass=False
	if(str.count("p")<2):
		ispass=False
	if(str.count("l")<1):
		ispass=False
	if(str.count("e")<1):
		ispass=False
	
	if(ispass):
		print("An apple a day keeps the doctor away.")
	else:
		print("The apples on the other side of the wall are the sweetest.")