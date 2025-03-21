#include <iostream>
#include <string>
#include <stack>

using namespace std;

string str;
stack<int> s;

// 맨 처음에 0 넣어놓기 마지막에 s.top으로 계산하도록
// 괄호가 여러개 나와서 스택 써야할듯
// ( : 0 추가
// 문자열 : 뒤에 숫자가 있는지 확인 후 top에 추가
// ) : 뒤에 숫자가 오는지 확인 후 계산해서 top에 넣기

int main(){
	cin>>str;
	s.push(0);

	for(int i=0;i<str.length();i++){
		// (
		if(str[i]=='(') s.push(0);

		// 문자열
		if(str[i]>='A'&&str[i]<='Z'){
			int temp=s.top();
			s.pop();

			int val=1;

			if(str[i+1]>='0'&&str[i+1]<='9'){ // 숫자가 올 경우
				val=str[i+1]-'0';
			}
			if(str[i]=='H') s.push(temp+1*val);
			if(str[i]=='C') s.push(temp+val*12);
			if(str[i]=='O') s.push(temp+val*16);
		}


		// )
		if(str[i]==')'){
			int val=1;
			int temp=s.top();
			s.pop();
			int ans=s.top();
			s.pop();

			if(i!=str.length()-1){
				if(str[i+1]>='0'&&str[i+1]<='9'){ // 숫자가 올 경우
					val=str[i+1]-'0';
				}
			}
			s.push(ans+temp*val);			
		}
		// cout<<str[i]<<" "<<s.top()<<"\n";

	}
	cout<<s.top();
}