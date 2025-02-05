#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

vector<int> pman;
vector<int> mman;
vector<int> pwoman;
vector<int> mwoman;

int n;
int ans=0;

bool compare(int x,int x2){
	return abs(x)<abs(x2);
}

void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		int temp;
		cin>>temp;
		if(temp>0) pman.push_back(temp);
		if(temp<0) mman.push_back(abs(temp));
	}
	for(int i=0;i<n;i++){
		int temp;
		cin>>temp;
		if(temp>0) pwoman.push_back(temp);
		if(temp<0) mwoman.push_back(abs(temp));
	}
}

void solve(){
	// 절댓값 기준으로 정렬
	sort(pman.begin(),pman.end());
	sort(mman.begin(),mman.end());
	sort(pwoman.begin(),pwoman.end());
	sort(mwoman.begin(),mwoman.end());

	// 남자가 양수일 때, 여자가 더 키 커야함 이때, 여자는 음수여야함
	int ep=0;
	int ew=0;
	while(ep<pman.size() && ew<mwoman.size()){
		if(abs(pman[ep])<abs(mwoman[ew])){
			ans++;
			ep++;
		}
		ew++;
	}

	ep=0;
	ew=0;
	// 남자가 음수일 때, 여자가 더 키 작아야함, 이때 여자는 양수여야함	
	while(ep<mman.size()&& ew<pwoman.size()){
		if(abs(mman[ep])>abs(pwoman[ew])){
			ans++;
			ew++;

		}
		ep++;

	}

	cout<<ans;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	input();
	solve();
}