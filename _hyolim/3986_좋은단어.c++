#include <iostream>
#include <stack>

using namespace std;

// stack을 사용해서 1번 스택의 top이 2번 stack의 top과 같을 경우 제거
// 다를 경우, 2번 stack에 넣기
// 끝났을 때 2번 stack이 비어있을 경우 ++;
int n;
int answer=0;
void solve(string str){
	stack<int> s1;
	stack<int> s2;

	for(int i=0;i<str.length();i++){
		s1.push(str[i]);
	}

	while(!s1.empty()){
		int t=s1.top();
		if(s2.empty()){
			s2.push(t);
		}else{
			if(t==s2.top()){
				s2.pop();
			}else{
				s2.push(t);
			}
		}

		s1.pop();
	}

	// 다 끝났을 때, s2가 empty면 answer++
	if(s2.empty()) answer++;
}

int main(){
	cin>>n;
	for(int i=0;i<n;i++){
		string str;
		cin>>str;
		solve(str);
	}
	cout<<answer;

}