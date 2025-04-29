#include <iostream>
#include <cmath>

using namespace std;

int mid;

void star(int y,int x,int num,int top,int bot){
	int left=mid-abs(top-y);
	int right=mid+abs(top-y);

	if(y==bot&&x>=left&&x<=right) cout<<"*";
	else if(x==left||x==right){
		if((top>bot?top:bot)>=y && (top<bot?top:bot)<=y){
			cout<<"*";
		}else{
			cout<<" ";
		}
	}
	else{
		if(num==1) cout<<" ";
		else star(y,x,num-1,num%2==0?bot+1:bot-1,(top+bot)/2);
	}
	
}

int main(){
	int n;
	cin>>n;
	int h=pow(2,n)-1;
	int w=h*2-1;
	mid=w/2;

	for(int i=0;i<h;i++){
		for(int j=0;j<(n%2==0?w-i:w-(mid-i));j++){
			if(n%2==0) star(i,j,n,h-1,0);
			else star(i,j,n,0,h-1);
		}
		cout<<"\n";
	}
}