#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

string answer="";
int check[29]={0,};

int main(){
	string str;
	cin>>str;
	answer=str;

	sort(str.begin(),str.end());
	int n=str.length();

	// 먼저 가능한건지 확인
	for(int i=0;i<n;i++){
		check[str[i]-'A']++;
	}

	int checknum=1;
	char mid;
	for(int i=0;i<26;i++){
		if(check[i]%2!=0) {
			mid=(char)(i+'A');
			checknum--;
		}
		if(checknum<0){
			cout<<"I'm Sorry Hansoo";
			exit(0);
		}
	}

	int answeri=0;
	for(int i=0;i<n-1;i++){
		if(str[i]==str[i+1]){
			answer[answeri]=str[i];
			answer[n-1-answeri]=str[i+1];
			answeri++;
			i++;
		}
	}
	if(n%2==1){
		answer[n/2]=mid;
	}
	cout<<answer;
}