#include <iostream>
#include <algorithm>

using namespace std;

int dir[3][2]={{-1,0},{-1,-1},{0,-1}};
int plus_arr[1400]={0,};
int arr[701][701]={0,};
int m,n; // 세로, 날짜수

void input(){
	cin>>m>>n;
	int z,o,t; // 0,1,2 개수

	for(int i=0;i<n;i++){
		cin>>z>>o>>t;
		for(int j=z;j<z+o;j++){
			plus_arr[j]+=1;
		}
		for(int j=o+z;j<t+z+o;j++){
			plus_arr[j]+=2;
		}
	}	
}


void solve(){
	// 1 더해서 plus_arr에 있는 값들 arr로 옮겨놓기
	int temp=0;
	// 왼쪽 아래에서 올라오기
	for(int i=m-1;i>=0;i--){
		arr[i][0]=1+plus_arr[temp];
		temp++;
	}

	// 오른쪽으로 가기
	for(int i=1;i<m;i++){
		arr[0][i]=1+plus_arr[temp];
		temp++;
	}

	// 왼쪽, 왼쪽위, 위에서 가장 큰 숫자 대입하기
	for(int i=1;i<m;i++){
		for(int j=1;j<m;j++){
			int mnum=0;
			for(int k=0;k<3;k++){
				if(mnum<arr[i+dir[k][0]][j+dir[k][1]]){
					mnum=arr[i+dir[k][0]][j+dir[k][1]];
				}
			}
			arr[i][j]=mnum;
		}
	}
}

void output(){
	for(int i=0;i<m;i++){
		for(int j=0;j<m;j++){
			cout<<arr[i][j]<<" ";
		}
		cout<<"\n";
	}
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	input();
	solve();
	output();


}