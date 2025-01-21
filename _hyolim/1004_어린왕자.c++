#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

struct circle{
	int y;
	int x;
	int r;
};

int sy,sx;
int dy,dx;
int n;
int ans=0;
vector<circle> vec;

void reset(){
	vec.clear();
	ans=0;
}

void input(){
	cin>>sy>>sx>>dy>>dx;
	cin>>n;
	for(int i=0;i<n;i++){
		int y,x,r;
		cin>>y>>x>>r;
		circle c={y,x,r};
		vec.push_back(c);
	}
}

// 거리 구하기
double dis(int y1,int x1,int y2,int x2){
	return sqrt(pow(y2-y1,2)+pow(x2-x1,2));
}

bool inCircle(int y,int x,int cy,int cx,int r){
	return r>dis(y,x,cy,cx);
}

void solve(){
	// 원 안에 있는지 확인
	for(auto e:vec){
		if(inCircle(sy,sx,e.y,e.x,e.r)) ans++;
		if(inCircle(dy,dx,e.y,e.x,e.r)) ans++;
		if(inCircle(sy,sx,e.y,e.x,e.r) && inCircle(dy,dx,e.y,e.x,e.r)) ans=ans-2;

	}
}

void output(){
	cout<<ans<<"\n";
}

int main(){
	int t;
	cin>>t;	
	for(int i=0;i<t;i++){
		// cout<<"===========\n";
		reset();
		input();
		solve();
		output();
	}
}