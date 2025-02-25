#include <iostream>

using namespace std;

int n,m,h;
bool ladder_pos[31][11];
int ladder_cnt; // 가로선을 추가할 개수
bool flag=false;

void dfs(int y,int cnt){
	if(ladder_cnt==cnt){
		bool possible=true;
		for(int i=1;i<=n;i++){
			int verti=i;
			for(int j=0;j<h;j++){
				int hight=j;
				if(ladder_pos[hight][verti]){
					verti++;
				}else if(verti>1&&ladder_pos[hight][verti-1]){
					verti--;
				}
			}

			if(verti!=i){
				possible=false;
				break;
			}
		}
		if(possible){
			flag=true;
		}
		return;
	}
	for(int i=y;i<h;i++){
		for(int j=1;j<n;j++){
			if(!ladder_pos[i][j-1]&&!ladder_pos[i][j]&&!ladder_pos[i][j+1]){
				ladder_pos[i][j]=true;
				dfs(i,cnt+1);
				ladder_pos[i][j]=false;
			}
		}
	}
	return;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	cin>>n>>m>>h;

	for(int i=0;i<m;i++){
		int a,b;
		cin>>a>>b;
		ladder_pos[a-1][b]=true;
	}

	for(int i=0;i<=3;i++){
		ladder_cnt=i;
		dfs(0,0);
		if(flag){
			cout<<ladder_cnt<<endl;
			return 0;
		}
	}
	cout<<-1;
}

