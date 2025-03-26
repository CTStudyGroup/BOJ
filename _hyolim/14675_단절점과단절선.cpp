#include <iostream>
#include <vector>
using namespace std;

// 간선이 두 개 이상 연결되어있으면 단절점이 아니다.
// 단절점과 연결되어있는 선은 단절선이다.

// 연결리스트를 구현해서 연결리스트에서 하나만 연결되어있는 원소들을 찾아서 bool true 해놓는다.
// 간선 정보도 순서대로 저장한 후에 질의가 오면 bool true가 있는지 확인한다.
int n;
vector<int> vec[100001]; // 연결 리스트
bool isCut[100001];
int arr[100001][2];

void input(){
	cin>>n;
	for(int i=1;i<=n-1;i++){
		int a,b;
		cin>>a>>b;
		arr[i][0]=a;
		arr[i][1]=b;

		vec[a].push_back(b);
		vec[b].push_back(a);
	}
}

void solve(){
	// 먼저 bool 배열 채우기
	for(int i=1;i<=n;i++){
		if(vec[i].size()==1) isCut[i]=true;
	}
}

void output(){
	int x,y;
	cin>>x>>y;
	if(x==1){ // 단절점
		if(isCut[y]) cout<<"no\n";
		else cout<<"yes\n";
	}else{ // 단절선
		cout<<"yes\n";
	}
}

int main(){
	input();
	solve();
	int q;
	cin>>q;
	for(int i=0;i<q;i++){
		output();
	}
}