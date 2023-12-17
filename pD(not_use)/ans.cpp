#include<bits/stdc++.h>

using namespace std;
#define int long long

string str[100000];

signed main(){
	int T;
	cin>>T;
	for(int i=0;i<T;i++){
		cin>>str[i];
	}
	for(int i=T-1;i>=0;i--){
		cout<<str[i]<<endl;
	}
	return 0;
}
/**/