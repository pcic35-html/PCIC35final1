#include<bits/stdc++.h>
using namespace std;
int main(){
	int n;
	cin>>n;
	int ans=0;
	for(int i=0;i<n;i++){
		string str;
		cin>>str;
		int ad;
		cin>>ad;
		ans+=ad;
	}
	cout<<ans<<endl;
	return 0;
}