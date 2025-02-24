#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int n;
struct score{
	long s;
	char c;

	bool operator<(const score &other)const{
		if(s>other.s){
			return true;
		}
		return false;
	}
};
vector<string> vec;

score sc[26];
long arr[26]={0,};
void input(){
	cin>>n;
	while(n--){
		string temp;
		cin>>temp;
		vec.push_back(temp);
	}

	for(int i=0;i<26;i++){
		sc[i].s=0;
		sc[i].c=(char)(i+'A');
	}
}

void solve(){
	// 점수 매겨서 점수 순으로 
	for(auto e:vec){
		for(int i=0;i<e.length();i++){
			sc[e[i]-'A'].s+=pow(10,(e.length()-i));
		}
	}

	sort(sc,sc+26);
	long temp=9;
	// 점수 출력
	for(int i=0;i<26;i++){
		if(!sc[i].s) continue;
		arr[sc[i].c-'A']=temp;
		temp--;
	}

}

void output(){
	long answer=0;
	long temp=0;
	for(auto e:vec){
		for(int i=0;i<e.length();i++){
			temp*=10;
			temp+=arr[e[i]-'A'];
		}
		// cout<<temp<<" ";
		answer+=temp;
		temp=0;
	}
	cout<<answer;
}
int main(){
	input();
	solve();
	output();
}