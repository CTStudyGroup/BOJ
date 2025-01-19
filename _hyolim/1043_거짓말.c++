#include <iostream>
#include <vector>
#include <set>
#include <queue>
using namespace std;
// 사람들끼리 전부 엮어놓은 후에 각 파티를 돌면서 확인한다.
// 친구의 친구까지만 검열
int n,m;
vector<int> t;
vector<int> party[51];
vector<int> vec[51];
set<int> s; // 진실을 알고있는 사람 리스트
int ans=0;

void printvec(){
	for(int i=1;i<=n;i++){
		for(int j=0;j<vec[i].size();j++){
			cout<<vec[i][j]<<" ";
		}
		cout<<"\n";
	}
}

void input(){
	cin>>n>>m;
	int tnum;
	cin>>tnum;
	for(int i=0;i<tnum;i++){
		int temp;
		cin>>temp;
		t.push_back(temp);
	}

	for(int i=0;i<m;i++){
		int pnum;
		cin>>pnum;
		for(int j=0;j<pnum;j++){
			int temp;
			cin>>temp;
			party[i].push_back(temp);
		}
	}

	for(int i=0;i<m;i++){
		for(int j=0;j<party[i].size();j++){
			for(int k=0;k<j;k++){
				if(j==k) continue;
				vec[party[i][j]].push_back(party[i][k]);
				vec[party[i][k]].push_back(party[i][j]);
			}
		}
	}
}

void prints(){
	for(auto i=s.begin();i!=s.end();i++){
		cout<<*i<<" ";
	}
	cout<<"\n";
}

void solve(){
	// 친구랑 연결된 모든 노드를 다 비활성화 시켜야함
	queue<int> q;

	if(t.size()!=0){
		for(int i=0;i<t.size();i++){
			q.push(t[i]);
		}


		for(int temp=q.front();!q.empty();q.pop()){
			temp=q.front();
			s.insert(temp);
			for(int i=0;i<vec[temp].size();i++){
				// 이미 있는 경우 패스
				if(s.find(vec[temp][i])!=s.end()) continue;
				s.insert(vec[temp][i]);
				q.push(vec[temp][i]);
			}
		}
	}
	
	// prints();
	// 파티 돌면서 진실 아는 사람 있는지 확인하기
	for(int i=0;i<m;i++){
		bool sig=true;
		for(int j=0;j<party[i].size();j++){
			if(s.find(party[i][j])!=s.end()) sig=false;
		}
		if(sig) ans++;
	}
}

int main(){
	input();
	// printvec();
	solve();
	cout<<ans;
}