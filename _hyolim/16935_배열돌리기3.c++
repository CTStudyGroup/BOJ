#include <iostream>
#include <vector>

using namespace std;

int n,m,r;
vector<vector<int>> vec;

void printVec(vector<vector<int>> invec){
	// cout<<"---vec---\n";
	for(auto e:invec){
		for(auto v:e){
			cout<<v<<" ";
		}
		cout<<"\n";
	}
}

void input(){
	cin>>n>>m>>r;
	for(int i=0;i<n;i++){
		vector<int> v;
		for(int j=0;j<m;j++){
			int temp; cin>>temp;
			v.push_back(temp);
		}
		vec.push_back(v);
	}
	// printVec(vec);
}

void c1(){
	vector<vector<int>> temp;
	for(int i=n-1;i>=0;i--){
		temp.push_back(vec[i]);
	}
	vec=temp;
}

void c2(){
	vector<vector<int>> temp;
	for(int j=0;j<n;j++){
		vector<int> t;
		for(int i=m-1;i>=0;i--){
			t.push_back(vec[j][i]);
		}
		temp.push_back(t);
	}

	vec=temp;
}

void c3(){
	vector<vector<int>> temp;
	for(int i=0;i<m;i++){
		vector<int> t;
		for(int j=n-1;j>=0;j--){

			t.push_back(vec[j][i]);
		}
		temp.push_back(t);
	}

	vec=temp;
	n=vec.size();
	m=vec[0].size();
}

void c4(){
	vector<vector<int>> temp;
	for(int i=m-1;i>=0;i--){
		vector<int> t;
		for(int j=0;j<n;j++){

			t.push_back(vec[j][i]);
		}
		temp.push_back(t);
	}

	vec=temp;
	n=vec.size();
	m=vec[0].size();
}

void c5(){
	vector<vector<int>> temp;
	int n2=n/2;
	int m2=m/2;

	// 4번을 1번 자리로
	for(int i=0;i<n2;i++){
		vector<int> t;
		for(int j=0;j<m2;j++){
			t.push_back(vec[n2+i][j]);
		}
		for(int j=0;j<m2;j++){
			t.push_back(vec[i][j]);
		}
		temp.push_back(t);
	}

	// 3번을 4번 자리로
	for(int i=0;i<n2;i++){
		vector<int> t;
		for(int j=0;j<m2;j++){
			t.push_back(vec[n2+i][m2+j]);
		}
		for(int j=0;j<m2;j++){
			t.push_back(vec[i][j+m2]);
		}
		temp.push_back(t);
	}
	vec=temp;
}

void solve(int tempr){
	if(tempr==1) c1();

	if(tempr==2) c2();

	if(tempr==3) c3();

	if(tempr==4) c4();

	if(tempr==5) c5();

	if(tempr==6){
		c5();
		c5();
		c5();
	}

}

int main(){
	input();
	for(int i=0;i<r;i++){
		int tempr; cin>>tempr;
		solve(tempr);
	}
	printVec(vec);
}