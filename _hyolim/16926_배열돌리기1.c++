#include <iostream>
#include <vector>
using namespace std;

int n,m,r;
vector<vector<int>> vec;

void printArr(){
	// cout<<"---vec---\n";
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cout<<vec[i][j]<<" ";
		}
		cout<<"\n";
	}
}

void input(){
	cin>>n>>m>>r;

	for(int i=0;i<n;i++){
		vector<int> temp;
		for(int j=0;j<m;j++){
			int t;
			cin>>t;
			temp.push_back(t);
		}
		vec.push_back(temp);
	}

}

void rotate(int y1,int x1,int y2,int x2){
	// 0,0,3,3
	int temp=vec[y1][x1];

	for(int i=x1;i<x2;i++){
		vec[y1][i]=vec[y1][i+1];
	}

	for(int i=y1;i<y2;i++){
		vec[i][x2]=vec[i+1][x2];
	}

	for(int i=x2;i>x1;i--){
		vec[y2][i]=vec[y2][i-1];
	}

	for(int i=y2;i>y1+1;i--){
		vec[i][x1]=vec[i-1][x1];
	}

	vec[y1+1][x1]=temp;
}

void solve(){

	int i=0;
	while(1){
		if(i>=n-1-i || i>=m-1-i){
			break;
		}
		rotate(i,i,n-1-i,m-1-i);
		i++;

	}
	// printArr();

}

int main(){
	input();
	// printArr();
	while(r--){
		solve();
	}
	printArr();
	
}