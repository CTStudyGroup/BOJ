#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct p{
	int st;
	int end;

	bool operator<(const p& o)const{
		if(st==o.st){
			return end<o.end;
		}
		return st<o.st;
	}
};
int n,l;
vector<p> vec;
long answer=0;

void input(){
	cin>>n>>l;
	for(int i=0;i<n;i++){
		int st,end;
		cin>>st>>end;
		vec.push_back({st,end});
	}
}

void solve(){
	sort(vec.begin(),vec.end());

	int st=vec[0].st;
	int end=st;
	// 널빤지 최대 길이만큼 만들기
	while(end<vec[0].end){
		end+=l;
	}

	for(int i=1;st<end;i++){	
		// cout<<i<<" : ";
		// cout<<st<<" "<<end<<"\n";
		if(i>=vec.size()){
			answer+=(end-st)/l;
			return;
		}
		if(end>vec[i].st){
			while(end<vec[i].end){
				end+=l;
			}
		}else{
			answer+=(end-st)/l;
			// cout<<"*"<<answer<<" ";
			st=vec[i].st;
			end=st;
			while(end<vec[i].end){
				end+=l;
			}
		}
	}
	// cout<<st<<" "<<end;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	input();
	solve();
	cout<<answer;

}