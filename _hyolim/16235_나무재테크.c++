#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int n; // 보드 크기
int m; // 나무 개수
int k; // k년이 지났을 때

// 1base
int board[11][11]={0,}; // 양분
int a[11][11] = {0,}; // 겨울에 추가되는 양분의 양
vector<int> tree[11][11]; // 각 보드의 나무 정보
vector<int> temp_tree[11][11]; // 죽은 나무 저장소

int d[8][2]={{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};

void printT(){
	cout<<"----tree-----\n";
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			for(auto e:tree[i][j]){
				cout<<i<<" "<<j<<" "<<e<<"\n";
			}
		}
	}
}

void printB(){
	cout<<"----board----\n";

	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			cout<<board[i][j]<<" ";
		}
		cout<<"\n";
	}
}

// 나무 정렬
void sortT(){
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			sort(tree[i][j].begin(),tree[i][j].end());
		}
	}
}

void input(){
	cin>>n>>m>>k;

	for(int i=0;i<11;i++){
		for(int j=0;j<11;j++){
			board[i][j]=5;
		}
	}

	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			cin>>a[i][j];
		}
	}

	// 나무정보 
	int x,y,z;
	for(int i=0;i<m;i++){
		cin>>x>>y>>z;
		tree[x][y].push_back(z);
	}
	sortT();
}

void spring(){

	// 나무가 자신의 나이만큼 양분을 먹는다.
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			for(auto it=tree[i][j].begin();it!=tree[i][j].end();){
				if(*it>board[i][j]){
					temp_tree[i][j].push_back(*it);
					it=tree[i][j].erase(it);
				}else{
					board[i][j]-=*it;
					*it=*it+1;

					++it;
				}
			}
		}
	}
}

void summer(){
	// 봄에 죽은 나무가 양분으로 변한다.
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			for(auto e:temp_tree[i][j]){

				board[i][j]+=(e/2);
			}
			temp_tree[i][j].clear();
		}
	}
}

void autumn(){
	// 번식
	// 번식하는 나무는 나이가 5의 배수
	// 인접한 8칸에 나이가 1인 나무가 생ㄱ긴다.
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			for(auto e:tree[i][j]){
				if(e%5!=0) continue;

				for(int k=0;k<8;k++){
					int ny=d[k][0]+i;
					int nx=d[k][1]+j;

					if(ny<=0||nx<=0||ny>n||nx>n) continue;
					tree[ny][nx].push_back(1);
				}
			}
		}
	}
	sortT();
}

void winter(){
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			board[i][j]+=a[i][j];
		}
	}
}

void solve(){
	while(k--){
		spring();
		summer();
		autumn();
		winter();
		// printB();

	}

}

void output(){
	long ans=0;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			ans+=tree[i][j].size();
		}
	}
	cout<<ans;
}


int main(){
	input();

	solve();
	output();
}