#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

/*
아기상어 > 물고기 : 잡아먹음
아기상어 == 물고기 : 지나감
아기상어 < 물고기 : 못 지나

갈 때 최솟값으로 지나가야함
자신과 같은 크기의 수만큼 물고기를 먹어야하
가는 기준 : 위왼아래오
*/

/*
1. 물고기 위치, 상어로부터 거리 정보(몇 초 걸리는지), 물고기 크기를 포함한 구조체 생성
2. 매 사이클마다 상어로부터 거리 정보를 기준으로 정렬하기 vector를 queue처럼 사용
3. 아기상어는 현재 크기, 먹은 물고기의 개수를 저장
*/

struct fish{
	int y;
	int x;
	int size;
	int dis;

	bool operator<(const fish& other) const{
		if(dis<other.dis) return true;
		else if(dis==other.dis) {
			if(y<other.y) return true;
			else if(y==other.y){
				return x<other.x;
			}
		}
		return false;
	}
};

struct shark{
	int y;
	int x;
	int size;
	int fish;
};

struct point_t{
	int y;
	int x;
};

vector<fish> vec; // 물고기
shark s; // 상어
int direct[4][2]={{-1,0},{0,-1},{1,0},{0,1}};
int t=0; // 시간
int board[21][21]={0,};
int visited[21][21]={0,};
int n;

// 거리 구하는 함수
void caldis(int y1,int x1,int y2,int x2){
	queue<point_t> q;
	point_t f={y1,x1};
	for(q.push(f);!q.empty();q.pop()){
		point_t temp=q.front();
		point_t next;
		// 만약 상어가 지나갈 수 있다면
		for(int i=0;i<4;i++){
			next.y=direct[i][0]+temp.y;
			next.x=direct[i][1]+temp.x;
			if(next.y<0||next.y>=n||next.x<0||next.x>=n) continue;
			if(visited[next.y][next.x]) continue;
			if(s.size>=board[next.y][next.x]){
				visited[next.y][next.x]=visited[temp.y][temp.x]+1;
				if(next.y==y2&&next.x==x2) break;
				q.push(next);
			}
		}

	}
}

// visited 초기화하는 함수
void setV(){
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			visited[i][j]=0;
		}
	}
}

void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			int temp;
			cin>>temp;
			board[i][j]=temp;
			if(temp==9){
				s.y=i;
				s.x=j;
				s.size=2;
				s.fish=0;
			}
			else if(temp>0){
				fish tf={i,j,temp,99999999};
				vec.push_back(tf);
			}
		}
	}
}

void printB(){
	cout<<"=======board======\n";
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			cout<<board[i][j]<<" ";
		}
		cout<<"\n";
	}
}

void printV(){
	cout<<"=======visited======\n";
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			cout<<visited[i][j]<<" ";
		}
		cout<<"\n";
	}
}

void printF(){
	cout<<"---------fish--------\n";
	for(auto e:vec){
		cout<<e.y<<" "<<e.x<<" "<<e.size<<" "<<e.dis<<"\n";
	}
}

void sortfish(){
	for(auto& e:vec){
		if(e.size>=s.size) continue;
		setV();
		// fish 거리 설정
		caldis(s.y,s.x,e.y,e.x);
		if(visited[e.y][e.x]) e.dis=visited[e.y][e.x];
	}
	// fish 거리 초기화
	sort(vec.begin(),vec.end());
}

// 갈 수 있는 곳이 있는지 확인하는 함수
bool isGo(){
	for(auto e:vec){
		if(e.dis<99999999) return true;
	}
	return false;
}

void solve(){
	sortfish();
	while(isGo()){
		// printB();
		// printV();
		// 하나 꺼내오기
		fish temp=vec[0];
		// cout<<temp.y<<" "<<temp.x<<" "<<temp.size<<"\n";
		// 먹기
		if(s.size>temp.size) s.fish++; // 나보다 작으면 먹기 
		if(s.fish==s.size){ //내 몸사이즈만큼 먹었으면 사이즈 키우고 먹은 횟수 초기화하기
			s.size++;
			s.fish=0;
		}

		//보드 갱신 
		board[s.y][s.x]=0;
		board[temp.y][temp.x]=9;

		// 이동
		s.y=temp.y;
		s.x=temp.x;
		t+=temp.dis;

		// 처리 끝났으면 지우기
		// cout<<"TEMP : "<<temp.y<<" "<<temp.x<<"\n";
		vec.erase(vec.begin());
		//board 셋업
		sortfish();
	}
}

void output(){
	cout<<t;
}

int main(){
	input();
	// printB();
	solve();
	output();
}