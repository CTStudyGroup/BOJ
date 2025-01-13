/*
temp=1; 
반대는 불가능 
vector에 넣고, vector가 빌 때까지 다 뺀 후에 남아있는 애들이
순서대로 남아있는지 확인 후 남아있으면 Nice, 아니면 Sad
-----
stack에서 빼서 갈 수 있다는 점을 간과함
*/

#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int n;
vector<int> vec;
stack<int> s;
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
	while(!vec.empty()){
		// 둘 중에 하나 비교해서 temp랑 같을 경우 지우기
		// vec 먼저 비교
		if(temp==*vec.begin()){
			temp++;
			vec.erase(vec.begin());
		}else{
			if(!s.empty()){
				// s 비교
				if(temp==s.top()){
					temp++;
					s.pop();
				}
				// 다를 경우 줄 서있는거 스택으로 빼기
				else{
					s.push(*vec.begin());
					vec.erase(vec.begin());

				}
			}else{
				s.push(*vec.begin());
				vec.erase(vec.begin());

			}

		}
	}
}

void output(){
	// 남은 스택 확인하기
	while(!s.empty()){
		if(temp!=s.top()){
			cout<<"Sad";
			exit(0);
		}
		temp++;
		s.pop();
	}
	cout<<"Nice";
}

int main(){
	input();
	solve();
	output();
}
