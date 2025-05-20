#include <iostream>
#include <vector>

using namespace std;

int n;
int board[21][21]={0,};
long sum=0;
long answer=987654211;

void printB(){
	cout<<"--board--\n";
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			cout<<board[i][j]<<" ";
		}
		cout<<"\n";
	}
}

// 1-base
void input(){
	cin>>n;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			cin>>board[i][j];
			sum+=board[i][j];
		}
	}
	// printB();
}

long section1(int x,int y,int d1,int d2){
	int tempx,tempy;
	long s=0;
	//사각형 부분
	for(int i=1;i<x;i++){
		for(int j=1;j<=y;j++){
			tempx=i;
			tempy=j;
			// cout<<tempx<<", "<<tempy<<"| ";
			s+=board[tempx][tempy];
		}
	}
	// cout<<"*";
	// 삼각형 부분
	for(int i=0;i<d1;i++){
		for(int j=1;j<y-i;j++){
			tempx=x+i;
			tempy=j;
			// cout<<tempx<<", "<<tempy<<"| ";
			s+=board[tempx][tempy];
		}
	}
	return s;
}


long section2(int x,int y,int d1,int d2){
	int tempx,tempy;
	long s=0;
	//사각형 부분
	for(int i=1;i<x;i++){
		for(int j=y+1;j<=n;j++){
			tempx=i;
			tempy=j;
			// cout<<tempx<<", "<<tempy<<"| ";
			s+=board[tempx][tempy];
		}
	}
	// cout<<"*";
	// 삼각형 부분
	for(int i=0;i<=d2;i++){
		for(int j=y+i+1;j<=n;j++){
			tempx=x+i;
			tempy=j;
			// cout<<tempx<<", "<<tempy<<"| ";
			s+=board[tempx][tempy];
		}
	}
	return s;
}


long section3(int x,int y,int d1,int d2){
	int tempx,tempy;
	long s=0;
	//삼각형 부분
	for(int i=0;i<=d2;i++){
		for(int j=1;j<y-d1+i;j++){
			tempx=d1+x+i;
			tempy=j;
			// cout<<tempx<<", "<<tempy<<"| ";
			s+=board[tempx][tempy];
		}
	}
	// cout<<"*";
	// 사각형 부분
	for(int i=x+d1+d2+1;i<=n;i++){
		for(int j=1;j<y-d1+d2;j++){
			tempx=i;
			tempy=j;
			// cout<<tempx<<", "<<tempy<<"| ";
			s+=board[tempx][tempy];
		}
	}
	return s;
}

long section4(int x,int y,int d1,int d2){
	int tempx,tempy;
	long s=0;
	//삼각형 부분
	for(int i=0;i<d1;i++){
		for(int j=y+d2-i;j<=n;j++){
			tempx=d2+x+1+i;
			tempy=j;
			// cout<<tempx<<", "<<tempy<<"| ";
			s+=board[tempx][tempy];
		}
	}
	// cout<<"*";
	// 사각형 부분
	for(int i=x+d2+1+d1;i<=n;i++){
		for(int j=y-d1+d2;j<=n;j++){
			tempx=i;
			tempy=j;
			// cout<<tempx<<", "<<tempy<<"| ";
			s+=board[tempx][tempy];
		}
	}
	return s;
}

long calc(vector<long> s){
	long maxn=0;
	long minn=987654321;

	for(auto e:s){
		maxn=max(maxn,e);
		minn=min(minn,e);
	}
	return maxn-minn;
}

void solve(){
	// 1. 구획을 나눌 경계를 정한다.
	for(int x=1;x<=n-1;x++){
		for(int y=1;y<=n-1;y++){
			for(int d1=1;d1<n;d1++){ //경계의 길이
				for(int d2=1;d2<n;d2++){
					if(d1+d2+x>n) continue;
					if(1>y-d1) continue;
					if(y+d2>n) continue;
					// cout<<"x: "<<x<<" y: "<<y<<" d1: "<<d1<<" d2: "<<d2<<"\n";
					long s1=section1(x,y,d1,d2);
					long s2=section2(x,y,d1,d2);
					long s3=section3(x,y,d1,d2);
					long s4=section4(x,y,d1,d2);
					long s5=sum-s1-s2-s3-s4;
					vector<long> vec={s1,s2,s3,s4,s5};
					answer=min(answer,calc(vec));

				}
			}
		}
	}
	// 2. 각 선거구의 인구를 구한다.

	// 3. 가장 큰 값과 작은 값의 차이를 구해서 최솟값을 구한다.
}

int main(){
	input();
	solve();
	cout<<answer;
}