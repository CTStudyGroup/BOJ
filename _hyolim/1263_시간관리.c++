#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int n;

// 늦게 끝나는 순서대로 정렬
// 뒤에서부터 확인하면서 최대로 미룰 수 있는 시간을 계산
// 이때, answer와 제출 시간 중 적은 쪽을 기준으로 계산
// answer가 음수면 끝
/*
4
3 5
8 5
10 15
5 20
*/
struct board{
	int t;
	int s;

	bool operator<(const board& other) const{
		if(s>other.s){
			return true;
		}
		if(s==other.s){
			return t<other.t;
		}
		return false;
	}
};

vector<board> vec;
int ans;
void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		int x,y;
		cin>>x>>y;
		board temp={x,y};
		vec.push_back(temp);
	}
}

void solve(){
	sort(vec.begin(),vec.end());
	ans=21e8;
	for(auto e:vec){
		// cout<<e.t<<" "<<e.s<<" ";
		int cal=min(ans,e.s);
			ans=cal-e.t;
		// cout<<cal<<" "<<ans<<"\n";

	}
	if(ans>21e7 || ans<0){
		cout<<"-1";
		return;
	}
	cout<<ans;
}

int main(){
	input();
	solve();
}