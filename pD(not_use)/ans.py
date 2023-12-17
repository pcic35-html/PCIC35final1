
T=int(input())
a=[""]*T
for i in range(T):
	a[i]=input()

a.reverse()
for i in range(T):
	print(a[i])