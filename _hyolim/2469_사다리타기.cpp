#include <iostream>
#include <vector>
#include <string>


using namespace std;

int k; // 참가자수
int n; // 가로줄 수
string final_state; // 마지막 상태
vector<string> map;
string answer="";

void printMap(){
	cout<<"---map---\n";
	for(auto e:map) cout<<e<<"\n";
}

void input(){
	cin>>k>>n;
	cin>>final_state;

	for(int i=0;i<n;i++){
		string temp;
		cin>>temp;
		map.push_back(temp);
	}
	// printMap();
}

string upDown(){
	string temp="";
	for(int i=0;i<k;i++){
		temp+=(char)('A'+i);
	}

	// 안보이는 곳까지 내려가기
	for(int idx=0;idx<k;idx++){
		// int idx=1;
		int y=0; // 행
		int x=idx; // 열

		while(y<map.size()){	
			// cout<<y<<" "<<x<<" \n";

			if(map[y][0]=='?') break;	
			// 내 오른쪽에 사다리가 있는가
			if(x<map[y].length()){
				if(map[y][x]=='-'){
					x++;
					y++;
					continue;
				}
			}

			// 내 왼쪽에 사다리가 있는가
			if(x>0){
				if(map[y][x-1]=='-'){
					x--;
					y++;
					continue;
				}
			}
			y++;
		}
		temp[x]=(char)('A'+idx);
		// cout<<(char)('A'+idx)<<" "<<x<<"\n";
		// cout<<"-----\n";

	}
	return temp;
}

string DownUp(){
	string temp=final_state;

	// 안보이는 곳까지 올라가기
	for(int idx=0;idx<k;idx++){
		// int idx=1;
		int y=n-1; // 행
		int x=idx; // 열

		while(y>=0){	
			// cout<<y<<" "<<x<<" \n";

			if(map[y][0]=='?') break;	
			// 내 오른쪽에 사다리가 있는가
			if(x<map[y].length()){
				if(map[y][x]=='-'){
					x++;
					y--;
					continue;
				}
			}

			// 내 왼쪽에 사다리가 있는가
			if(x>0){
				if(map[y][x-1]=='-'){
					x--;
					y--;
					continue;
				}
			}
			y--;
		}
		temp[x]=final_state[idx];
		// cout<<(char)('A'+idx)<<" "<<x<<"\n";
		// cout<<"-----\n";

	}

	return temp;
}

void solve(){
	// 위에서 안보이는 곳까지 갔을 때 상황
	string up=upDown();

	// 아래에서 안보이는 곳까지 갔을 때 상황
	string down=DownUp();

	// 가능하도록 바꾸기
	for(int i=0;i<k;i++){
		if(up[i]==down[i]){
			answer+='*';
		}else{
			answer+='-';
			char c=up[i];
			up[i]=up[i+1];
			up[i+1]=c;
		}
	}

	if(up!=down){
		for(int i=0;i<k-1;i++){
			cout<<'x';
		}
		return;
	}else{
		for(int i=0;i<k-1;i++){
			cout<<answer[i];
		}
		return;
	}
}

int main(){
	input();
	solve();

}