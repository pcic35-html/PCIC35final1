import os
import threading
from colorama import Fore, Style, Back
print("請打包一資料夾")
print("裡面包含test_make.py自動生成輸入測資")
print("裡面包含ans.cpp自動生成輸出測資")
print("裡面包含ans.py用以比對測資")
print()
dir=input("請輸入題目資料夾位置：")
if((dir[-1])!=id("/")):
	dir+="/"
T=int(input("請輸入測資數量"))
os.system("mkdir "+dir+"io")
os.system("g++ -o "+dir+"run "+dir+"ans.cpp")

allOK=True

ic=Back.LIGHTYELLOW_EX
oc=Back.LIGHTBLUE_EX
cc=Back.LIGHTCYAN_EX
pc=Back.LIGHTGREEN_EX
rc=Back.LIGHTRED_EX
res=Style.RESET_ALL

def ioc(i,b):
	return dir+"io/"+"{:0>2d}".format(i) +b

def runner(i):
	print(ic+"生成input測資",str(i)+res)
	os.system("python3 "+dir+"test_make.py > "+ioc(i,".in"))
	print(oc+"生成output測資",str(i)+res)
	os.system("./"+dir+"run < "+ioc(i,".in")+" > "+ioc(i,".out"))
	print(cc+"生成比對output測資",str(i)+res)
	os.system("python3 "+dir+"ans.py < "+ioc(i,".in")+" > "+ioc(i,".check"))
	if(open(ioc(i,".out")).read()==open(ioc(i,".check")).read()):
		print(pc+"測資",i,"通過"+res)
	else:
		print(rc+"測資",i,"不通過"+res)


runlist=(threading.Thread(target=runner, args=(i,)) for i in range(1,T+1,1))
for i in runlist:
	i.start()
"""
for i in runlist:
	i.join()

if(allOK):
	print(Fore.GREEN+"全部通過"+Style.RESET_ALL)
else:
	print(Fore.RED+"有錯誤"+Style.RESET_ALL)
"""
