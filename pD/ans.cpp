#include<bits/stdc++.h>

using namespace std;
#define int long long


signed main(){
	int T;
	cin>>T;
	string str[T];
	for(int i=0;i<T;i++){
		cin>>str[i];
	}
	for(int i=T-1;i>=0;i--){
		cout<<str[i]<<endl;
	}
	return 0;
}
/**/