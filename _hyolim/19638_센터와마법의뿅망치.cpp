#include <iostream>
#include <queue>

using namespace std;

int n,h,t;
priority_queue<int> pq;

void input(){
	cin>>n>>h>>t;
	for (int i = 0; i < n; ++i)
	{
		int temp; cin>>temp;
		pq.push(temp);
	}
}

bool isLower(){
	if(pq.top()<h) return true;
	return false;
}

void solve(){
	for (int i = 0; i < t; ++i)
	{
		if(isLower()){
			cout<<"YES\n"<<i;
			return;
		}

		int temp=pq.top();
		if(temp==1) continue;
		pq.pop();
		pq.push(temp/2);
	}
	if(isLower()){
		cout<<"YES\n"<<t;
		return;
	}

	cout<<"NO\n"<<pq.top();
}	

int main(){
	input();
	solve();
}