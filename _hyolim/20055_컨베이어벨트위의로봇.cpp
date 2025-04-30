#include <iostream>

using namespace std;

int n,k;
int arr[201]={0,};
bool robot[201];
long answer=0;

int p=0; // 벨트 시작점, 로봇 시작점

void input(){
	cin>>n>>k;
	for(int i=0;i<2*n;i++){
		cin>>arr[i];
	}
}

void printRobot(){
	cout<<"---robot---\n";
	for(int i=0;i<2*n;i++){
		cout<<robot[i]<<" ";
	}
	cout<<"\n";
}

bool check(){
	int cnt=0;
	for(int i=0;i<(2*n);i++){
		if(!arr[i]) cnt++;
		if(cnt>=k) return true;
	}

	return false;
}

void solve(){
	while(true){
		// 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
		p=(p-1+2*n)%(2*n);
		// 언제든지 로봇이 내리는 위치에 도달하면 그 즉시 내린다. 
		robot[(p+n-1)%(2*n)]=false;

		// 2. **가장 먼저 벨트에 올라간 로봇**부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
		// 2-1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
		int rp=(p-1+n)%(2*n);
		for(int i=n;i>0;i--){
			int next_rp=(rp+1)%(2*n);
			if(robot[rp]&&!robot[next_rp]&&arr[next_rp]){
				robot[rp]=false;
				if(next_rp!=(p+n)%(2*n)){
					robot[next_rp]=true;
					arr[next_rp]--;
				}
			}

			rp=(rp-1+(2*n))%(2*n);
		}
		robot[(p+n-1)%(2*n)]=false;

		// 4. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다
		if(arr[p]){
			robot[p]=true;
			arr[p]--;
		}

		answer++;
		if(check()){
			cout<<answer;
			return;
		}
	}
	
	// 5. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
}

int main(){
	input();
	solve();
}