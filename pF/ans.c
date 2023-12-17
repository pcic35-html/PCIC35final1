#include<stdio.h>
int main(){
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		char c[100000];
		scanf("%s",c);
		int a=0;
		int p=0;
		int l=0;
		int e=0;
		for(int i=0;i<100000;i++){
			if(c[i]=='A'){
				a++;
			}
			if(c[i]=='P'){
				p++;
			}
			if(c[i]=='L'){
				l++;
			}
			if(c[i]=='E'){
				e++;
			}
			if(c[i]=='\0'){
				break;
			}
		}
		if(a>=1&&p>=2&&l>=1&&e>=1){
			printf("An apple a day keeps the doctor away.\n");
		}
		else{
			printf("The apples on the other side of the wall are the sweetest.\n");
		}
	}
	return 0;
}