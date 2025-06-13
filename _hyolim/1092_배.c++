#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n,m;
vector<int> crane;
vector<int> box;


void input(){
	cin>>n;
	for (int i = 0; i < n; ++i)
	{
		int temp; cin>>temp;
		crane.push_back(temp);
	}
	cin>>m;
	for (int i = 0; i < m; ++i)
	{
		int temp; cin>>temp;
		box.push_back(temp);
	}
}

void solve(){
	sort(crane.begin(),crane.end());
	sort(box.begin(),box.end());

	if(crane.back()<box.back()){
		cout<<-1;
		return;
	}

	int t=0;
	while(!box.empty()){
		for(int i=crane.size()-1;i>=0;i--){
			for(int j=box.size()-1;j>=0;j--){
				if(crane[i]>=box[j]){
					box.erase(box.begin()+j);
					break;
				}
			}
		}
		t++;
	}
	cout<<t;

}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	// 정렬 후 본인보다 작은 박스를 그리디처럼 없앤다.
	input();
	solve();
}