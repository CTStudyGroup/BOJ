#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int n;
vector<pair<long,long>> vec; // 시작 시간, 끝 시간
long answer=0;

void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		long st,en; cin>>st>>en;
		vec.push_back({st,en});
	}
}

bool cmp(pair<long,long> a,pair<long,long> b){
	if(a.first==b.first){
		return a.second<b.second;
	}
	return a.first<b.first;
}

void solve(){
	sort(vec.begin(),vec.end(),cmp);
	// for(auto e:vec){
	// 	cout<<e.first<<" "<<e.second<<"\n";
	// }

	priority_queue<long, vector<long>, greater<long>> room;

	for(int i=0;i<n;i++){

		// 빈 자리 있는지 확인
		if(room.empty()){
			room.push(vec[i].second);
			if(answer<room.size()) answer=room.size();
			continue;
		}

		// 맨 처음이 가능한지 확인, set은 오름차순이라 맨 처음만 확인하면 
		if(room.top()<=vec[i].first){
			room.pop();
		}

		room.push(vec[i].second);
		if(answer<room.size()) answer=room.size();

	}
	cout<<answer;
}

void output(){

}

int main(){	
	input();
	solve();
	output();
}