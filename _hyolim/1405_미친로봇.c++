#include <iostream>

using namespace std;

int n;
int visited[29][29]={0,};
int direct[4][2]={{0,1},{0,-1},{1,0},{-1,0}};
double per[4];

void input(){
	cin>>n;
	for(int i=0;i<4;i++){
		double temp;
		cin>>temp;
		per[i]=temp/100.0;
	}
}

double solve(int depth,int y,int x){
	if(depth==n) return 1.0;

	visited[y][x]=1;
	double r=0.0;

	for(int i=0;i<4;i++){
		int ny=y+direct[i][0];
		int nx=x+direct[i][1];

		if(visited[ny][nx]) continue;
		r=r+per[i]*solve(depth+1,ny,nx);
	}

	visited[y][x]=0;
	return r;
}

int main(){
	input();
	cout.precision(10);
	cout<<fixed<<solve(0,14,14);
}