#include <iostream>
#include <queue>
#include <vector>
#include <cstring>
#include <string>

using namespace std;

int t,h,w;
char building[102][102];
bool visited[102][102];
bool keys[26];
vector<pair<int,int>> door[26]; // 열쇠가 없어서 기다리는 문 위치

int dy[4]={-1,1,0,0};
int dx[4]={0,0,-1,1};

void reset(){
	memset(building,'.',sizeof(building));
	memset(visited,false,sizeof(visited));
	memset(keys,false,sizeof(keys));
	for(int i=0;i<26;i++){
		door[i].clear();
	}

}

void input(){
	cin>>h>>w;
	for(int i=1;i<=h;i++){
		string line;
		cin>>line;

		for(int j=1;j<=w;j++){
			building[i][j]=line[j-1];
		}
	}

	string keyInput;
	cin>>keyInput;
	if(keyInput!="0"){
		for(char c:keyInput){
			keys[c-'a']=true;
		}
	}
}


void solve(){
	queue<pair<int,int>> q;
	q.push({0,0});
	visited[0][0]=true;
	int answer=0;

	while(!q.empty()){
		int y=q.front().first;
		int x=q.front().second;
		q.pop();

		for(int i=0;i<4;i++){
			int ny=y+dy[i], nx=x+dx[i];
			if(ny<0||nx<0||ny>=h+2||nx>=w+2) continue;
			if(visited[ny][nx]) continue;
			if(building[ny][nx]=='*') continue;


			if(building[ny][nx]=='$') answer++;

			// 열쇠인 경우, 새 키라면 안열렸던 문 열기
			if(building[ny][nx]>='a'&&building[ny][nx]<='z'){
				int keyIdx=building[ny][nx]-'a';
				if(!keys[keyIdx]){
					keys[keyIdx]=true;

					for(auto &e :door[keyIdx]){
						if(!visited[e.first][e.second]){
							visited[e.first][e.second]=true;
							q.push(e);
						}
					}
					door[keyIdx].clear();
				}
			}

			if(building[ny][nx]>='A'&& building[ny][nx]<='Z'){
				int doorIdx=building[ny][nx]-'A';
				if(!keys[doorIdx]){
					door[doorIdx].push_back({ny,nx});
					continue;
				}
			}
			visited[ny][nx]=true;
			q.push({ny,nx});
		}
	}
	cout<<answer<<"\n";

}


int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	cin>>t;
	while(t--){
		reset();
		input();
		solve();
	}
}