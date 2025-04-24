#include <iostream>
#include <vector>

using namespace std;

int dy[8]={-1,-1,0,1,1,1,0,-1};
int dx[8]={0,1,1,1,0,-1,-1,-1};

struct fire{
	int m;
	int s;
	int d;
};

int n,m,k;

vector<fire> map[51][51];

void printMap(){
	cout<<"---map---\n";
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			for(auto e:map[i][j]){
				cout<<"i: "<<i<<" j: "<<j<<", ";
				cout<<e.m<<" "<<e.s<<" "<<e.d<<"\n";
			}
		}
	}
}

void input(){
	cin>>n>>m>>k;

	for(int i=0;i<m;i++){
		int r,c,m,s,d;
		cin>>r>>c>>m>>s>>d;
		fire temp={m,s,d};
		map[r-1][c-1].push_back(temp);
	}
	// printMap();
}

// map=tempMap;
void copy(vector<fire> tempMap[51][51]){
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			map[i][j]=tempMap[i][j];	
		}
	}
}

// 1. 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
void move(){
	vector<fire> tempMap[51][51];

	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			for(int l=0;l<map[i][j].size();l++){
				// int ny=i+dy[map[i][j][l].d]*map[i][j][l].s;
				// int nx=j+dx[map[i][j][l].d]*map[i][j][l].s;
				// if(ny<0) ny+=n;
				// if(ny>=n) ny%=n;
				// if(nx<0) nx+=n;
				// if(nx>=n) nx%=n;

				int ny=i;
				int nx=j;
				for(int c=0;c<map[i][j][l].s;c++){
					ny+=dy[map[i][j][l].d];
					nx+=dx[map[i][j][l].d];
					if(ny<0) ny+=n;
					if(ny>=n) ny-=n;
					if(nx<0) nx+=n;
					if(nx>=n) nx-=n;
				}

				tempMap[ny][nx].push_back(map[i][j][l]);
			}
		}
	}
	copy(tempMap);
}

void engraft(){
	vector<fire> tempMap[51][51];
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			if(map[i][j].empty()) continue;
			if(map[i][j].size()==1){
				tempMap[i][j].push_back(map[i][j][0]);
				continue;
			}

			// 두 개 이상일 때
			int tempM=0, tempS=0;

			// 방향	
			int dir=0;
			if(map[i][j][0].d%2){ // 홀수이면
				dir=1;
			}else{
				dir=0;
			}
			

			bool dirsig=false;
			// 질량 합, 
			for(int l=0;l<map[i][j].size();l++){
				tempM+=map[i][j][l].m;
				tempS+=map[i][j][l].s;

				if(map[i][j][l].d%2!=dir){
					dirsig=true;
				}
			}


			int startd=0;
			if(dirsig){ // 하나라도 다를 경우
				startd=1;
			}

			tempM/=5;
			tempS/=map[i][j].size();
			// cout<<tempM<<" "<<tempS<<" "<<startd<<"\n";

			// 질량이 0일 경우는 사라지기
			if(tempM==0) continue;

			// 새로운 파이어볼 만들기
			for(int l=0;l<4;l++){
				fire temp={tempM,tempS,startd+l*2};
				tempMap[i][j].push_back(temp);
			}
		}
	}
	copy(tempMap);
}

void solve(){
	while(k--){
		// 1. 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
		// cout<<k<<"\n";
		move();
		// printMap();

		// 2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
		// 같은 칸에 있는 파이어볼을 모두 하나로 합쳐진다.
		engraft();
		// 파이어볼은 4개의 파이어볼로 나눠진다.
		// printMap();
	}
}

void output(){
	long answer=0;
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			for(auto e:map[i][j]){
				answer+=e.m;
			}
		}
	}
	cout<<answer;
}

int main(){
	input();
	solve();
	output();
}