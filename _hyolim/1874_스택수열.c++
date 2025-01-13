#include <iostream>
#include <stack>
#include <vector>
#include <string>

using namespace std;

vector<int> vec;
vector<string> ans;
stack<int> s;
int n;
int temp=1;

void input(){
	cin>>n;

	for(int i=0;i<n;i++){
		int x;
		cin>>x;
		vec.push_back(x);
	}

}

void solve(){
	s.push(temp);
	ans.push_back("+");

	while(!vec.empty()){
		// temp가 n 초과하면 노
		if(temp>n){
			cout<<"NO";
			exit(0);
		}
		if(!s.empty()){
			// 스택 맨 위랑 비교하기
			if(s.top()==*vec.begin()){
				// 같을 경우 빼고, 다를 경우 더하기
				s.pop();
				vec.erase(vec.begin());
				ans.push_back("-");
			}
			else{
				temp++;
				s.push(temp);
				ans.push_back("+");
			}
		}else{
			temp++;
			s.push(temp);
			ans.push_back("+");
		}
	}
}

void output(){
	for(int i=0;i<ans.size();i++){
		cout<<ans[i]<<"\n";
	}
}

int main(){
	input();
	solve();
	output();

}