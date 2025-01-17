#include <iostream>
#include <algorithm>

using namespace std;

int n;
int arr[1025][1025]={0,};

void input(){
	cin>>n;

	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			cin>>arr[i][j];
		}
	}

}

int solve(int depth,int y,int x){
	if(depth==1){
		return arr[y][x];
	}

	int temp[4];
	temp[0]=solve(depth/2,y,x);
	temp[1]=solve(depth/2,y,x+depth/2);
	temp[2]=solve(depth/2,y+depth/2,x);
	temp[3]=solve(depth/2,y+depth/2,x+depth/2);

	sort(temp,temp+4);
	return temp[2];
}

int main(){
	input();
	cout<<solve(n,0,0);
}