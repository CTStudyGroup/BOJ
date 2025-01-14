#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> m;
vector<int> p;
int zcnt=0;
int n;
int ans=0;

void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		int x;
		cin>>x;
		if(x==0){
			zcnt++;
		}
		if(x>0){
			p.push_back(x);
		}
		if(x<0){
			m.push_back(x);
		}
	}

	sort(p.begin(),p.end());
	sort(m.begin(),m.end());

	if(m.size()%2!=0) {
		if(zcnt>0) {
			m.erase(m.end()-1);
		}
	}

}

void solve(){
	// 큰 거 두 개씩 곱해서 더하기
	if(!p.empty()){
		for(int i=p.size()-1;i>=1;i=i-2){
			if(p[i]==1||p[i-1]==1){
				ans+=p[i];
				ans+=p[i-1];
			}else{
				ans+=p[i]*p[i-1];
			}
		}
		if(p.size()%2!=0) ans+=p[0];
	}

	if(!m.empty()){
		for(int i=0;i<m.size()-1;i=i+2){
			ans+=m[i]*m[i+1];

		}
		if(m.size()%2!=0) ans+=m[m.size()-1];
	}

	cout<<ans;

}

int main(){
	input();
	solve();
}