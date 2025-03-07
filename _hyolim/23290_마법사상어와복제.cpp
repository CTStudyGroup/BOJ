#include <iostream>
#include <vector>
#include <string>
using namespace std;

/*
구현해야하는 것
4. 상어가 이동할 방향 재귀로 찾기
*/

int m,s;
// 반시계방향은 -
string fishDP[8]={"←","↖","↑", "↗", "→", "↘", "↓", "↙"};
int fishD[8][2]={{0,-1},{-1,-1},{-1,0},{-1,1},{0,1},{1,1},{1,0},{1,-1}}; //물고기 이동 방향
// 상 좌 하 우
int sharkD[4][2]={{-1,0},{0,-1},{1,0},{0,1}};
int fishScent[4][4]={0,};
vector<int> fish[4][4];
vector<int> tempfish[4][4];


// 상어
int sharky,sharkx;
bool visited[4][4];
vector<int> sharkM;
int maxeatcnt=0;

void setV(){
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			visited[i][j]=0;
		}
	}
}

void printFish(){
	cout<<"---------------\n";
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(fish[i][j].empty()) continue;
			cout<<i<<" "<<j<<": ";
			for(auto e:fish[i][j]){
				cout<<fishDP[e]<<",";
			}
			cout<<"\n";
		}
	}
}

void input(){
	cin>>m>>s;
	for(int i=0;i<m;i++){
		int y,x,d;
		cin>>y>>x>>d;
		fish[y-1][x-1].push_back(d-1); 
	}
	cin>>sharky>>sharkx;
	sharky--;
	sharkx--;
}

void setTempFish(){
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			tempfish[i][j].clear();
		}
	}
}

void printTempFish(){
	cout<<"-------temp--------\n";
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(tempfish[i][j].empty()) continue;
			cout<<i<<" "<<j<<": ";
			for(auto e:tempfish[i][j]){
				cout<<fishDP[e]<<",";
			}
			cout<<"\n";
		}
	}
}

void fishMove(){
	int nexty,nextx;
	setTempFish();
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			for(auto e:fish[i][j]){
				int nextd=e;
				for(int z=0;z<8;z++){
					nextd=(8+e-z)%8;

					nexty=fishD[nextd][0]+i;
					nextx=fishD[nextd][1]+j;

					// 범위 조건 만족하고
					if(nexty<0||nextx<0||nexty>3||nextx>3) continue;

					// 상어
					if(nexty==sharky&&nextx==sharkx) continue;

					// 물고기 냄새
					if(fishScent[nexty][nextx]>0) continue;

					tempfish[nexty][nextx].push_back(nextd);
					break;
				}
			}
		}
	}
}

void findsharkMove(vector<int> s,int eatcnt,int y,int x){
	if(s.size()>=3){
		if(maxeatcnt<eatcnt){
			cout<<maxeatcnt;
			maxeatcnt=eatcnt;
			sharkM=s;
		}
		return;
	}

	for(int i=0;i<4;i++){
		int nexty=y+sharkD[i][0];
		int nextx=x+sharkD[i][1];

		// 범위 조건 만족하고
		if(nexty<0||nextx<0||nexty>3||nextx>3) continue;

		// 방문한 적 없는
		// if(visited[nexty][nextx]) continue;

		// visited[nexty][nextx]=true;
		s.push_back(i);
		findsharkMove(s,eatcnt+tempfish[nexty][nextx].size(),nexty,nextx);
		// visited[nexty][nextx]=false;
		s.pop_back();
	}
}

void copyFish(){
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			for(auto e:tempfish[i][j]){
				fish[i][j].push_back(e);
			}
		}
	}
}

void sharkMove(){
	// 상어가 갈 방향 찾기
	setV();
	vector<int> s;
	sharkM.clear();
	printTempFish();
	findsharkMove(s,0,sharky,sharkx);
	for(auto e:sharkM){
		cout<<e<<" ";
	}
	cout<<"\n";
	for(auto e:sharkM){
		sharky+=sharkD[e][0];
		sharkx+=sharkD[e][1];

		// 만약 물고기가 있을 경우
		if(!tempfish[sharky][sharkx].empty()){
			fishScent[sharky][sharkx]=;
			tempfish[sharky][sharkx].clear();
		}
	}
}

void minusScent(){
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(fishScent[i][j]) fishScent[i][j]-=1;
		}
	}
}

void solve(){
	while(s--){
		// 물고기 흔적 냄새 지우기
		minusScent();

		// 물고기 이동
		fishMove();

		// 상어 이동
		sharkMove();

		// 물고기 복ㅈㅔ
		copyFish();

		printFish();
	}
}

void output(){
	int answer=0;
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			answer+=fish[i][j].size();
		}
	}
	cout<<answer;
}

int main(){
	input();
	solve();
	output();
}