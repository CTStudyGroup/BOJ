#include <iostream>
#include <vector>
#include <string>
#include <cstring>
using namespace std;

struct point_t{
	int y;
	int x;
};

int n,r,c;
int map[101][101]={0,};
int boom[101][101];
int dy[9]={1,1,1,0,0,0,-1,-1,-1};
int dx[9]={-1,0,1,-1,0,1,-1,0,1};
vector<int> jongsu; // 종수의 움직임
int jy,jx; // 종수의 위치

void printMap(){
	cout<<"---map---\n";
	for(int i=0;i<r;i++){
		for(int j=0;j<c;j++){
			cout<<map[i][j]<<" ";
		}
		cout<<"\n";
	}
}

void input(){
	cin>>r>>c;
	for(int i=0;i<r;i++){
		string temp;
		cin>>temp;

		for(int j=0;j<temp.length();j++){
			if(temp[j]=='I') {
				map[i][j]=1;
				jy=i;
				jx=j;
			}
			if(temp[j]=='R') map[i][j]=2;
		}
	}

	string temp;
	cin>>temp;
	for(int i=0;i<temp.length();i++){
		jongsu.push_back(temp[i]-'0');
	}
	n=temp.length();

	// printMap();

}

point_t closetoJ(point_t temp){
	
	int minN=abs(jy-temp.y)+abs(jx-temp.x);
	int miny=temp.y;
	int minx=temp.x;
	point_t next;

	for(int i=0;i<9;i++){
		next.y=temp.y+dy[i];
		next.x=temp.x+dx[i];

		if(next.y<0||next.x<0||next.y>=r||next.x>=c) continue;

		// 최솟값 확인
		if(minN>abs(jy-next.y)+abs(jx-next.x)){
			minN=abs(jy-next.y)+abs(jx-next.x);
			miny=next.y;
			minx=next.x;
		}

	}

	point_t ans={miny,minx};
	return ans;
}

void solve(){
	for(int idx=0;idx<n;idx++){
		// 종수의 움직임. 어디로 갈 지만 확인
		map[jy][jx]=0;
		jy+=dy[jongsu[idx]-1];
		jx+=dx[jongsu[idx]-1];

		// 종수가 미친 아두이노와 같은 칸에 있는지 확인
		if(map[jy][jx]==2){
			cout<<"kraj "<<idx+1;
			exit(0);
		}
		else{
			map[jy][jx]=1;
		}

		memset(boom,0,sizeof(boom));
		// 미친 아두이노들 2 의 움직임
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){	
				if(map[i][j]!=2) continue;

				// 미친 아두이노가 종수와 가장 가까워지는 방향을 구하기 -> 이동
				point_t temp={i,j};
				point_t next=closetoJ(temp);

				// 종수가 미친 아두이노와 같은 칸에 있는지 확인
				if(next.y==jy&&next.x==jx){
					cout<<"kraj "<<idx+1;
					exit(0);			
				}

				// 미친 아두이노 옮기기
				if(!boom[next.y][next.x]) boom[next.y][next.x]=2;
				else boom[next.y][next.x]=3;
			}
		}

		// boom 배열 복사
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				if(map[i][j]==1) continue;
				if(boom[i][j]==2) map[i][j]=2;
				else map[i][j]=0;
			}
		}	
		// printMap();
	}
}

void output(){
	for(int i=0;i<r;i++){
		for(int j=0;j<c;j++){
			if(map[i][j]==0) cout<<'.';
			if(map[i][j]==1) cout<<'I';
			if(map[i][j]==2) cout<<'R';
		}
		cout<<"\n";
	}
}

int main(){
	input();
	solve();
	output();
}