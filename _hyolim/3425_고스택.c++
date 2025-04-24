#include <iostream>
#include <stack>
#include <vector>
#include <string>
#include <cmath>
#define MAX 1000000000
using namespace std;

stack<long> s;
vector<string> order;
int n;

void reset(){
	order.clear();
	while(!s.empty()) s.pop();
}

void input(){
	while(1){
		string temp;
		cin>>temp;

		if(temp=="END") return;
		if(temp=="QUIT") exit(0);
		if(temp=="NUM"){ // NUM은 숫자로 추가
			cin>>temp;
			order.push_back(temp);
		}else{
			order.push_back(temp);
		}
	}

}


void solve(long temp){
	s.push(temp);

	for(auto e:order){
		if(e=="POP"){
			if(s.empty()){
				cout<<"ERROR\n";
				return;
			}
			s.pop();
		}

		else if(e=="INV"){
			if(s.empty()){
				cout<<"ERROR\n";
				return;
			}
			long t=s.top();
			s.pop();
			s.push(-t);
		}

		else if(e=="DUP"){
			if(s.empty()){
				cout<<"ERROR\n";
				return;
			}
			s.push(s.top());
		}

		else if(e=="SWP"){
			if(s.empty()){
				cout<<"ERROR\n";
				return;
			}
			long first=s.top();
			s.pop();

			if(s.empty()){
				cout<<"ERROR\n";
				return;
			}
			long second=s.top();
			s.pop();

			s.push(first);
			s.push(second);

		}

		else if(e=="ADD"){
			if(s.empty()){
				cout<<"ERROR\n";
				return;
			}
			long first=s.top();
			s.pop();

			if(s.empty()){
				cout<<"ERROR\n";
				return;
			}
			long second=s.top();
			s.pop();

			if(abs(first+second)>MAX){
				cout<<"ERROR\n";
				return;
			}
			s.push(first+second);
		}

		else if(e=="SUB"){
			if(s.empty()){
				cout<<"ERROR\n";
				return;
			}
			long first=s.top();
			s.pop();

			if(s.empty()){
				cout<<"ERROR\n";
				return;
			}
			long second=s.top();
			s.pop();

			if(abs(second-first)>MAX){
				cout<<"ERROR\n";
				return;
			}

			s.push(second-first);
		}

		else if(e=="MUL"){
			if(s.empty()){
				cout<<"ERROR\n";
				return;
			}
			long first=s.top();
			s.pop();

			if(s.empty()){
				cout<<"ERROR\n";
				return;
			}
			long second=s.top();
			s.pop();

			if(second!=0){
				if(abs(first) > MAX / abs(second)){
					cout<<"ERROR\n";
					return;
				}
			}

			s.push(first*second);
		}

		else if(e=="DIV"){
			if(s.size() < 2){
				cout<<"ERROR\n";
				return;
			}
			long divisor = s.top(); s.pop();   // 제수
			long dividend = s.top(); s.pop();  // 피제수
			if(divisor == 0){
				cout<<"ERROR\n";
				return;
			}
			long res = abs(dividend) / abs(divisor);
			if ((dividend < 0) ^ (divisor < 0)) res = -res;
			s.push(res);
		}


else if(e=="MOD"){
	if(s.size() < 2){
		cout<<"ERROR\n";
		return;
	}
	long divisor = s.top(); s.pop();   // 제수
	long dividend = s.top(); s.pop();  // 피제수
	if(divisor == 0){
		cout<<"ERROR\n";
		return;
	}
	long res = abs(dividend) % abs(divisor);
	if (dividend < 0) res = -res;
	s.push(res);
}

		else{
			long tempnum=stoi(e);
			if(abs(tempnum)>MAX){
				cout<<"ERROR\n";
				return;
			}
			s.push(tempnum);
		}
	}

	if(s.empty()){
		cout<<"ERROR\n";
		return;		
	}
	long answer=s.top();
	s.pop();
	if(s.empty()){
		cout<<answer<<"\n";
	}else{
		cout<<"ERROR\n";
	}
}

int main(){
	
	while(1){
		reset();
		input();

	// for(auto e:order){
	// 	cout<<e<<" ";
	// }
		cin>>n;
		for(int i=0;i<n;i++){
			int temp;
			cin>>temp;
			solve(temp);
		}
		cout<<"\n";

	}

}