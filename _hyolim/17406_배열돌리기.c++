#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n,m,k;
vector<vector<int>> a;
vector<vector<int>> rVec;
long ans=99987654321;
bool visited[6];
void printB(vector<vector<int>> b){
	cout<<"--------a--------\n";
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cout<<b[i][j]<<" ";
		}
		cout<<"\n";
	}
}

// 1base
void input(){
	cin>>n>>m>>k;
	for(int i=1;i<=n;i++){
		vector<int> temp;
		for(int j=1;j<=m;j++){
			int x;
			cin>>x;
			temp.push_back(x);
		}
		a.push_back(temp);
	}
	// printB(a);
	for(int i=0;i<k;i++){
		int r,c,s;
		cin>>r>>c>>s;
		vector<int> v;
		v.push_back(r);
		v.push_back(c);
		v.push_back(s);

		rVec.push_back(v);
	}
}

vector<vector<int>> rotate(int y1,int x1,int y2,int x2,vector<vector<int>> b){
	// temp

	int j=0;
	for(int j=0;j<min((y2-y1)/2,(x2-x1)/2);j++){
		int temp=b[y1+j][x1+j];

		for(int i=y1+j;i<y2-j;i++){
			b[i][x1+j]=b[i+1][x1+j];
		}

		for(int i=x1+j;i<x2-j;i++){
			b[y2-j][i]=b[y2-j][i+1];
		}

		for(int i=y2-j;i>y1+j;i--){
			b[i][x2-j]=b[i-1][x2-j];
		}

		for(int i=x2-j;i>x1+j;i--){
			b[y1+j][i]=b[y1+j][i-1];
		}
		// cout<<"\n";
		b[y1+j][x1+1+j]=temp;
	}

	return b;
	// printB(b);
}

long minA(vector<vector<int>> v){
	long answer=987654321;
	for(auto e:v){
		long sum=0;
		for(auto w:e){
			sum+=w;
		}
		if(sum<answer) answer=sum;
	}
	return answer;
}

void solve(int depth,vector<vector<int>> v){
	if(depth==k){
		int value=minA(v);
		if(ans>value) ans=value;
		return;
	}

	for(int i=0;i<k;i++){
		if(visited[i]) continue;
		visited[i]=true;
		int r=rVec[i][0];
		int c=rVec[i][1];
		int s=rVec[i][2];
		solve(depth+1,rotate(r-s-1,c-s-1,r+s-1,c+s-1,v));
		visited[i]=false;
	}

}

int main(){
	input();
	solve(0,a);
	cout<<ans;

}