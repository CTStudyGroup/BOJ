#include <iostream>
#include <algorithm>

using namespace std;

int a[6][3];

pair<int,int> g[]={{0,1},{0,2},{0,3},{0,4},{0,5},{1,2},{1,3},{1,4},{1,5},{2,3},{2,4},{2,5},{3,4},{3,5},{4,5}};

bool sol(int n){
	if(n==15){
		for(int i=0;i<6;i++){
			for(int j=0;j<3;j++){
				if(a[i][j]) return false;
			}
		}
		return true;
	}

	auto [p,q] =g[n];

	// 무승부
	if(a[p][1]&&a[q][1]){
		a[p][1]--,a[q][1]--;
		if(sol(n+1)) return true;
		a[p][1]++,a[q][1]++;
	}

	// 승리, 패배
	if(a[p][0]&&a[q][2]){
		a[p][0]--,a[q][2]--;
		if(sol(n+1)) return true;
		a[p][0]++,a[q][2]++;
	}

	// 패배, 승리
	if(a[p][2]&&a[q][0]){
		a[p][2]--,a[q][0]--;
		if(sol(n+1)) return true;
		a[p][2]++,a[q][0]++;
	}
	return false;
}

int main(){
	for(int i=0;i<4;i++){
		for(int j=0;j<6;j++){
			for(int k=0;k<3;k++){
				cin>>a[j][k];
			}
		}
		cout<<sol(0)<<" ";
	}
}