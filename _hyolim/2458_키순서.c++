#include <iostream>
#include <vector>

using namespace std;

int n,m;

vector<int> svec[500]; // 더 큰 애가 작은 애를 가리키는 연결리스트
vector<int> bvec[500]; // 더 작은 애가 큰 애를 가리키는 연결리스트
bool visited[500][500]={false,};

void printVec(){

	for(int i=0;i<=n;i++){
		cout<<i<<" : ";
		for(auto e:svec[i]){
			cout<<e<<" ";
		}
		cout<<"\n";
	}
	cout<<"------\n";
	for(int i=1;i<=n;i++){
		cout<<i<<" : ";
		for(auto e:bvec[i]){
			cout<<e<<" ";
		}
		cout<<"\n";
	}

}


void input(){
	cin>>n>>m;

	while(m--){
		int a,b;
		cin>>a>>b;
		svec[b].push_back(a);
		bvec[a].push_back(b);
	}

}

void solve(){

}

int main(){
	input();
	solve();
}