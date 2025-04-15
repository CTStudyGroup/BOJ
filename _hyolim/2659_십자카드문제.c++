#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int arr[4]={};
vector<vector<int>> vec;
vector<int> clockNum;
long cnt=0;
bool comp(vector<int> a,vector<int> b){
	for(int i=0;i<4;i++){
		if(a[i]<b[i]) return true;
		if(a[i]>b[i]) return false;
	}
	return false;
}

void input(){
	for(int i=0;i<4;i++){
		cin>>arr[i];
	}
}

void printCard(){
	cout<<"---card---\n";
	for(auto e:vec){
		for(auto v:e){
			cout<<v<<" ";
		}
		cout<<"\n";
	}
}

void makeCard(){
	for(int i=0;i<4;i++){
		vector<int> temp;
		for(int j=0;j<4;j++){
			int cur=(i+j)%4;
			temp.push_back(arr[cur]);
		}
		vec.push_back(temp);
	}

}

bool makeCard2(vector<int> v2){
	vector<vector<int>> vec2;
	for(int i=0;i<4;i++){
		vector<int> temp;
		for(int j=0;j<4;j++){
			int cur=(i+j)%4;
			temp.push_back(v2[cur]);
		}
		vec2.push_back(temp);
	}
	sort(vec2.begin(),vec2.end(),comp);
	if(v2!=*vec2.begin()) return true;
	return false;
}

void rec(int depth,vector<int> temp){
	if(depth==5){
		cnt++;

		// 해당 숫자가 가질 수 있는 가장 작은 시계수 찾기
		if(makeCard2(temp)) cnt--;
		if(temp==clockNum){
			cout<<cnt;
			exit(0);
		}
		return;
	}


	for(int i=1;i<=9;i++){
		temp.push_back(i);
		rec(depth+1,temp);
		temp.pop_back();
	}
}

void solve(){
	// 십자말카드에서 시계수 만들기
	makeCard();
	// printCard();
	sort(vec.begin(),vec.end(),comp);
	// printCard();
	clockNum=*vec.begin();
	// for(auto e:clockNum) cout<<e<<" ";

	// 모든 시계수 중에서 몇 번째인지 구하기
	vector<int> temp;
	rec(1,temp);
}

int main(){
	input();
	solve();
}