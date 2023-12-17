#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	string stra;
	getline(cin,stra);
	for(int i=0;i<t;i++){
		string str;
		getline(cin,str);
		int a=0,p=0,l=0,e=0;
		for(int j=0;j<str.size();j++){
			if(str[j]=='a' || str[j]=='A')a++;
			if(str[j]=='p' || str[j]=='P')p++;
			if(str[j]=='l' || str[j]=='L')l++;
			if(str[j]=='e' || str[j]=='E')e++;
		}
		if(a>=1 && p>=2 && l>=1 && e>=1){
			cout<<"An apple a day keeps the doctor away."<<endl;
		}else{
			cout<<"The apples on the other side of the wall are the sweetest."<<endl;
		}
	}
}