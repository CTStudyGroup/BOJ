#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int n;
vector<string> ve;
set<string> s;
int cnt=0;

void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		string temp; cin>>temp;
		ve.push_back(temp);
	}
}

void solve(){
	vector<string> vec=ve;
	sort(vec.begin(),vec.end());
	// for(auto e:vec){
	// 	cout<<e<<" ";
	// }

	// 정렬해놓고 앞뒤가 얼마나 같은지 확인하면서 가면 됨
	for(int i=0;i<n-1;i++){
		string temp1=vec[i];
		string temp2=vec[i+1];
		int tempcnt=0;
		for(int j=0;j<min(temp1.length(),temp2.length());j++){
			if(temp1[j]==temp2[j]) tempcnt++;
			else break;
		}

		if(tempcnt>cnt&&temp1!=temp2){
			cnt=tempcnt;
			s.clear();
			s.insert(temp1);
			s.insert(temp2);
		}
		if(tempcnt==cnt&&temp1!=temp2){
			cnt=tempcnt;
			s.insert(temp1);
			s.insert(temp2);
		}
	}
}

void output(){
	// 앞쪽에 있는걸 먼저 출력하도록 해야
	int idx=0;
	for(int i=0;i<n;i++){
		if(s.find(ve[i])!=s.end()){
			cout<<ve[i]<<"\n";
			idx=i;
			break;
		}
	}

	// temp와 cnt만큼 같은 애 찾기
	for(int i=idx+1;i<n;i++){
		int tempcnt=0;
		for(int j=0;j<cnt;j++){
			if(ve[idx][j]==ve[i][j]) tempcnt++;
			else break;
		}
		// cout<<tempcnt;
		if(tempcnt==cnt){
			cout<<ve[i];
			return;
		}	

	}
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	input();
	solve();
	output();
}