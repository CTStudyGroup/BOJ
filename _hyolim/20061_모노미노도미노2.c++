#include <iostream>
#include <vector>

using namespace std;

struct point_t{
	int y;
	int x;
};

int n;
vector<pair<int, point_t>> inv; // 들어오는 블록
int green[4][4]={0,};
int blue[4][4]={0,};
long answer=0;

void printGreen(){
	cout<<"---green---\n";
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			cout<<green[i][j]<<" ";
		}
		cout<<"\n";
	}
}

void printBlue(){
	cout<<"---blue---\n";
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			cout<<blue[i][j]<<" ";
		}
		cout<<"\n";
	}
}


void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		int t,y,x;
		cin>>t>>y>>x;
		inv.push_back({t,{y,x}});
	}

	// for(auto e:inv){
	// 	cout<<e.first<<", "<<e.second.y<<"&"<<e.second.x<<"\n";
	// }
}

// idx 행을 지우고 그 위에있는 블록들이 밑으로 내려오게 하는 것
void removeGreen(int idx){
	for(int i=idx-1;i>=0;i--){
		for(int j=0;j<4;j++){
			green[i+1][j]=green[i][j];
		}
	}

	for(int i=0;i<4;i++){
		green[0][i]=0;
	}
}

// idx 행을 지우고 그 위에있는 블록들이 밑으로 내려오게 하는 것
void removeBlue(int idx){
	for(int i=idx-1;i>=0;i--){
		for(int j=0;j<4;j++){
			blue[i+1][j]=blue[i][j];
		}
	}

	for(int i=0;i<4;i++){
		blue[0][i]=0;
	}
}

void checkFull(){
	for(int i=0;i<4;i++){
		bool sig=true;
		for(int j=0;j<4;j++){
			if(!green[i][j]) sig=false;
		}
		if(sig){
			answer++;
			removeGreen(i);
		}
	}

	for(int i=0;i<4;i++){
		bool sig=true;
		for(int j=0;j<4;j++){
			if(!blue[i][j]) sig=false;
		}
		if(sig){
			answer++;
			removeBlue(i);
		}
	}
}

void addGreen(int t,point_t temp){
	// t = 1: 크기가 1×1인 블록을 (x, y)에 놓은 경우
	if(t==1){
		int idx=-1;
		for(int i=0;i<4;i++){
			// 빈 자리가 있을 경우
			if(green[i][temp.x]==0){
				idx=i;
			}else{
				break;
			}
		}
		if(idx!=-1) {
			green[idx][temp.x]=1;
			return;
		}

		// 빈 자리가 없을 경우, 밑의 행을 전부 지우고 추가한다.
		removeGreen(3);
		addGreen(t,temp);
	}

	// t = 2: 크기가 1×2인 블록을 (x, y), (x, y+1)에 놓은 경우
	if(t==2){
		int idx=-1;
		for(int i=0;i<4;i++){
			// 빈 자리가 있을 경우
			if(green[i][temp.x]==0&&green[i][temp.x+1]==0){
				idx=i;
			}else{
				break;
			}
		}
		if(idx!=-1) {
			green[idx][temp.x]=1;
			green[idx][temp.x+1]=1;
			return;
		}

		removeGreen(3);
		addGreen(t,temp);
	}

	// t = 3: 크기가 2×1인 블록을 (x, y), (x+1, y)에 놓은 경우
	if(t==3){
		int idx=-1;
		for(int i=0;i<3;i++){
			// 빈 자리가 있을 경우
			if(green[i][temp.x]==0&&green[i+1][temp.x]==0){
				idx=i;
			}else{
				break;
			}
		}
		if(idx!=-1){
			green[idx][temp.x]=1;
			green[idx+1][temp.x]=1;
			return;
		}

		if(green[0][temp.x]==1) removeGreen(3);
		green[0][temp.x]=1;
		bool sig=true;
		for(int i=0;i<4;i++){
			if(!green[0][i])sig=false;
		}
		if(sig) {
			removeGreen(0);
			answer++;
		}else{
			removeGreen(3);
		}
		green[0][temp.x]=1;
	}
}

void addBlue(int t,point_t temp){
	// t = 1: 크기가 1×1인 블록을 (x, y)에 놓은 경우
	if(t==1){
		int idx=-1;
		for(int i=0;i<4;i++){
			// 빈 자리가 있을 경우
			if(blue[i][temp.x]==0){
				idx=i;
			}else{
				break;
			}
		}
		if(idx!=-1) {
			blue[idx][temp.x]=1;
			return;
		}

		// 빈 자리가 없을 경우, 밑의 행을 전부 지우고 추가한다.
		removeBlue(3);
		addBlue(t,temp);

	}

	// t = 1: 크기가 1×2인 블록을 (x, y), (x, y+1)에 놓은 경우
	if(t==3){
		int idx=-1;
		for(int i=0;i<4;i++){
			// 빈 자리가 있을 경우
			if(blue[i][temp.x]==0&&blue[i][temp.x+1]==0){
				idx=i;
			}else{
				break;
			}
		}
		if(idx!=-1) {
			blue[idx][temp.x]=1;
			blue[idx][temp.x+1]=1;
			return;
		}

		removeBlue(3);
		addBlue(t,temp);
	}

	// t = 3: 크기가 2×1인 블록을 (x, y), (x+1, y)에 놓은 경우
	if(t==2){
		int idx=-1;
		for(int i=0;i<3;i++){
			// 빈 자리가 있을 경우
			if(blue[i][temp.x]==0&&blue[i+1][temp.x]==0){
				idx=i;
			}else{
				break;
			}
		}
		if(idx!=-1){
			blue[idx][temp.x]=1;
			blue[idx+1][temp.x]=1;
			return;
		}


		if(blue[0][temp.x]==1) removeBlue(3);
		blue[0][temp.x]=1;
		bool sig=true;
		for(int i=0;i<4;i++){
			if(!blue[0][i])sig=false;
		}
		if(sig) {
			removeBlue(0);
			answer++;
		}else{
			removeBlue(3);
		}
		blue[0][temp.x]=1;
	}
}



void solve(){
	for(int i=0;i<inv.size();i++){
		// 1. 블럭의 이동
		// 	다른 블록을 만나거나, 보드의 경계를 만나기 전까지 계속해서 이동
		// 	* 초록은 열->열, 파랑은 행->열
		// 	블록이 들어갈 자리가 없다면, 한 줄 지우고 넣기
		//  가득 차서 사라졌다면 블록 이동
		//	사라진 행의 수만큼 아래로 이동
		// cout<<answer<<"\n";
		addGreen(inv[i].first,inv[i].second);
		// printGreen();

		addBlue(inv[i].first,{inv[i].second.x,inv[i].second.y});
		// printBlue();
		// 2. 어떤 행이 가득 찼는지 확인
		// 	가득 찼다면 answer+1& 해당 행 0으로 초기화
		checkFull();
	}

}

void output(){
	cout<<answer<<"\n";
	int cnt=0;
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(green[i][j]) cnt++;
			if(blue[i][j]) cnt++;
		}
	}
	cout<<cnt;
}

int main(){
	input();
	solve();	 
	output();
}