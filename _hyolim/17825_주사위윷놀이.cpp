#include <iostream>
#include <algorithm>

using namespace std;

int dice[10];
int pos[4];
int map[34];
int score[34];
int turn[34];
bool check[34];

int ans;

void input(){
	for(int i=0;i<10;i++) cin>>dice[i];

	for(int i=0;i<21;i++) map[i]=i+1;
	map[21]=21;
	for(int i=22;i<27;i++) map[i]=i+1;
	map[27]=20;
    map[28] = 29; map[29] = 30; map[30] = 25;
    map[31] = 32; map[32] = 25;

    turn[5] = 22; turn[10] = 31; turn[15] = 28;

    for (int i = 0; i < 21; i++) score[i] = 2 * i;
    score[22] = 13; score[23] = 16; score[24] = 19;
    score[25] = 25; score[26] = 30; score[27] = 35;
    score[28] = 28; score[29] = 27; score[30] = 26;
    score[31] = 22; score[32] = 24;
}

void solve(int cnt,int sum){
	if(cnt==10){
		ans=max(ans,sum);
		return;
	}

	for(int i=0;i<4;i++){
		int prev=pos[i];
		int cur=prev;
		int mov_cnt=dice[cnt];

		if(turn[cur]>0){
			// 현재 파란색에 있다면 방향 전환
			cur=turn[cur];
			mov_cnt--;
		}

		while(mov_cnt--){
			cur=map[cur];
		}

		// 도착 위치가 아닌데, 현재 위치에 다른 말이 있는 경우
		if(cur!=21&&check[cur]) continue;

		check[prev]=false;
		check[cur]=true;
		pos[i]=cur;
		solve(cnt+1,sum+score[cur]);

		check[prev]=true;
		check[cur]=false;
		pos[i]=prev;
	}
}

int main(){
	input();
	solve(0,0);

	cout<<ans;
}