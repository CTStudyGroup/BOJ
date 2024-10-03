#include <iostream>
#include <set>

using namespace std;

long n; //n개의 정수
set<long> s; // 
long m; // m개의 확인하는 수


void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		int temp;
		cin>>temp;
		s.insert(temp);
	}

}

void print(){
	cout<<n<<"\n";
	for(auto i : s){
		cout<<i<<" ";
	}
	cout<<"\n";
}

void solve(int num){

	if(s.lower_bound(num)!=s.end() && *s.lower_bound(num)==num){
		cout<<"1\n";
	}
	else{
		cout<<"0\n";
	}
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	input();
	// print();
	cin>>m;
	for(int i=0;i<m;i++){
		int temp;
		cin>>temp;
		solve(temp);
	}
}