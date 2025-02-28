#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct point_t{
	int y;
	int x;
};

int n,k;
vector<point_t> vec;

int dis=98765432;

void input(){
	cin>>n>>k;
	for(int i=0;i<n;i++){
		int y,x;
		cin>>y>>x;
		point_t temp={y,x};
		vec.push_back(temp);
	}

}

// 최대 거리 구하기
int check(vector<point_t> shelter){
	int maxD=-1;

	for(auto e:vec){
		int minD=98765432;
		for(auto f:shelter){
			if(e.y==f.y&&e.x==f.x) {
				minD=0;
				break;
			}
			minD=min(minD,abs(f.y-e.y)+abs(f.x-e.x));
		}
		maxD=max(maxD,minD);
	}

	return maxD;
}

void solve(int depth, vector<point_t> shelter,int idx){
	if(depth==k){
		dis=min(dis,check(shelter));
		return;
	}
	for(int i=idx;i<vec.size();i++){
		shelter.push_back(vec[i]);
		solve(depth+1,shelter,i+1);
		shelter.pop_back();
	}
}

int main(){
	vector<point_t> shelter;
	input();
	solve(0,shelter,0);
	cout<<dis;
}