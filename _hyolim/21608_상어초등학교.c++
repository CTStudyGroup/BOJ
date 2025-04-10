#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

struct point_t{
	int y;
	int x;
};

int n;
int dy[4]={-1,1,0,0};
int dx[4]={0,0,-1,1};
int map[20][20]={0,};
vector<int> preferList[401];
vector<int> stuList;
long answer=0;
// map은 0base, 학생은 1base

void input(){	
	cin>>n;
	for(int i=0;i<pow(n,2);i++){
		int stu;
		cin>>stu;
		stuList.push_back(stu);
		for(int j=0;j<4;j++){
			int p;
			cin>>p;
			preferList[stu].push_back(p);
		}
	}
}

bool cmp(pair<int,point_t> a,pair<int,point_t> b){
	if(a.first==b.first){
		if(a.second.y==b.second.y) return a.second.x<b.second.x;
		return a.second.y<b.second.y;
	}
	return a.first>b.first;
}

void solve(){
	for(auto e:stuList){ 	// *입력 순서대로 학생 넣기
		vector<pair<int,point_t>> vec;

		// *비어있는 칸 중에서 좋아하는 학생이 상하좌우 중에서 가장 많은 칸을 찾기
		// 비어있는 칸에 좋아하는 학생이 몇 명 있는지 temp 배열에 넣기
		int tempMap[20][20]={0,};
		int maxNum=0;

		// 이때, 최댓값 같이 구하기
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				if(map[i][j]!=0) continue;
				for(int k=0;k<4;k++){
					int ny=i+dy[k];
					int nx=j+dx[k];

					if(ny<0||nx<0||ny>=n||nx>=n) continue;
					for(auto v:preferList[e]){
						if(map[ny][nx]==v) tempMap[i][j]++;
					}

					maxNum=max(maxNum,tempMap[i][j]);
				}	
			}
		}

		// 최댓값을 가지는 칸을 벡터(Pair)에 넣기
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				if(map[i][j]!=0) continue;
				if(maxNum==tempMap[i][j]){
					vec.push_back({0,{i,j}});
				}
			}
		}

		// *그 칸이 여러개일 경우 비어있는 칸이 가장 많은 자리를 찾기
		// 벡터에서 비어있는 칸의 개수를 세서 넣기
		for(auto& v:vec){
			int cnt=0;
			int y=v.second.y;
			int x=v.second.x;
			for(int i=0;i<4;i++){
				int ny=dy[i]+y;
				int nx=dx[i]+x;
				if(ny<0||nx<0||ny>=n||nx>=n) continue;
				if(!map[ny][nx]) cnt++;
			}
			v.first=cnt;

		}

		// *그 중에서 행의 번호가 가장 작고, 열의 번호가 가장 작은 자리를 찾기
		// 비어있는 칸이 제일 많고, 행의 번호가 가장 작고, 열의 번호가 가장 작은 자리로 정렬하기ㅣ
		sort(vec.begin(),vec.end(),cmp);

		// 그 칸에 학생 집어넣기
		map[vec[0].second.y][vec[0].second.x]=e;
	}	
}

void output(){
	// 만족도 구하기
	// 인접한 학생이 0-0, 1-1, 2-10,3-100,4-1000
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			int cnt=0;
			int student=map[i][j];
			for(int k=0;k<4;k++){
				int ny=i+dy[k];
				int nx=j+dx[k];
				if(ny<0||nx<0||ny>=n||nx>=n) continue;
				for(auto v:preferList[student]){
						if(map[ny][nx]==v) cnt++;
				}
			}
			if(cnt==1) answer+=1;
			else if(cnt==2) answer+=10;
			else if(cnt==3) answer+=100;
			else if(cnt==4) answer+=1000;
		}
	}
	cout<<answer;
}

int main(){
	input();
	solve();
	output();
}