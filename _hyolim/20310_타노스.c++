#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

string s;

// 근데 굳이 DP로 안해도 되는 이유가 어차피 가장 빠른 문ㄴ자열은 00111 막 이런 식일텐데
int main(){
	cin>>s;

	int cnt0=0;
	int cnt1=0;

	for(auto e:s){
		if(e=='0') cnt0++;
		else cnt1++;
	}

	cnt0/=2;
	cnt1/=2;

	for(int i=0;i<s.length();i++){
		// 처음에 0일 경우 그냥 출력, 1일 경우 cnt1이 남아있으면 출력하지 않고 Cnt1만 없애기
		if(s[i]=='1'){
			if(cnt1>0) --cnt1;
			else cout<<s[i];
		}else{
			if(cnt0>0){
				cnt0--;
				cout<<s[i];
			}
		}
		
	}
}