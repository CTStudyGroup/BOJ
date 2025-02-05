#include <iostream>

using namespace std;

int t,n,m;

void input(){
	cin>>n>>m;

}

void solve(){
	int x1=1;
	int x2=1;
	int temp;
	int i=0;

	while(true){
		temp=(x1+x2)%m;
		x1=x2;
		x2=temp;

		// N번째가 1, N+1번째가 1이면 주기 시작
		if(x1==0 && x2==1){
			cout<<n<<" "<<i+2<<"\n";
			break;
		}

		i++;
	}
}

int main(){
	cin>>t;
	for(int i=0;i<t;i++){
		input();
		solve();
	}
}