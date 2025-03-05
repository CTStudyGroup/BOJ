#include <iostream>
#include <string>
#include <cmath>
using namespace std;

string str;
int a=0;
int answer=987654321;
void input(){
	cin>>str;
}

void solve(){
	// a의 개수 세기
	for(int i=0;i<str.length();i++){
		if(str[i]=='a') a++;
	}

	int temp=0;
	for(int i=0;i<str.length();i++){
		temp=0;
		for(int j=i;j<i+a;j++){
			if(str[j%str.length()]=='b') temp++;
		}
		answer=min(answer,temp);
	}
}

int main(){
	input();
	solve();
	cout<<answer;

}