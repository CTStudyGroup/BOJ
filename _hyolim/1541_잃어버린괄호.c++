#include <iostream>
#include <string>

using namespace std;

// string 넣으면 int로 변환해주는 함수 하나 만들기
// bool sig=true; 일 때 나오는 숫자들을 더함. 
// - 가 나오면 sig=false로 변환해서 뒤에 뭐가 나오든 그냥 뺌

bool sig=true;
string s;
int ans=0;

void input(){
	cin>>s;
}

int trans_string(string _s){
	int num=0;
	for(int i=0;i<_s.length();i++){
		num=num*10;
		num+=_s[i]-'0';
	}

	return num;
}

void solve(){
	string temp="";
	int temp_num=0;
	for(int i=0;i<s.length();i++){
		if(s[i]=='-'){
			temp_num=trans_string(temp);

			if(sig) ans+=temp_num;
			else ans-=temp_num;
			// cout<<temp_num<<"\n";

			sig=false;
			temp_num=0;
			temp="";
		}else if(s[i]=='+'){
			temp_num=trans_string(temp);

			if(sig) ans+=temp_num;
			else ans-=temp_num;
			// cout<<temp_num<<"\n";

			temp_num=0;
			temp="";
		}else{
			temp+=s[i];	
		}
	}


	// 마지막
	if(sig) cout<<trans_string(temp)+ans;
	else cout<<ans-trans_string(temp);
}

int main(){
	input();
	solve();


}