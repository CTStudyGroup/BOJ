#include <iostream>
#include <string>
#include <vector>

using namespace std;

string str;
long maxanswer=-1;
long minanswer=987654321;

void solve(string temp,long cnt){
	// 현재 temp에서 홀수 개수 구하기
	for(int i=0;i<temp.length();i++){
		if((temp[i]-'0')%2==1) cnt++;
	}
	// cout<<"$ "<<temp<<","<<cnt<<"\n";

	// 한자리 수일 경우 return
	if(temp.length()==1){
		// cout<<"--한자리-- : "<<cnt<<"\n";
		// 지금까지 홀수 개수 비교하기
		if(maxanswer<cnt) maxanswer=cnt;
		if(minanswer>cnt) minanswer=cnt;
		return;
	}

	vector<int> vec;
	// 잘라서 새로운 수 만들기 - 3개
	if(temp.length()==2){
		vec.push_back(stoi(temp.substr(0,1)));
		vec.push_back(stoi(temp.substr(1,2)));
		
		long num=0;
		// cout<<"--두자리--\n";
		for(auto e:vec){
			// cout<<e<<" ";
			num+=e;
		}
		// cout<<"\n";

		solve(to_string(num),cnt);
		vec.pop_back();

	}else{
		for(int i=1;i<temp.length()-1;i++){
			vec.push_back(stoi(temp.substr(0,i)));
			for(int j=1;j<temp.length()-i;j++){
				vec.push_back(stoi(temp.substr(i,j)));
				vec.push_back(stoi(temp.substr(i+j,temp.length()-i-j)));
				// cout<<"--세자리--\n";
				long num=0;
				// vector에 있는 값
				for(auto e:vec){
					// cout<<e<<" ";
					num+=e;
				}
				// cout<<"\n";
				solve(to_string(num),cnt);
				vec.pop_back();
				vec.pop_back();
			}
			vec.pop_back();
		}
	}


	// 새로운 수 재귀로 또 보내기
}

int main(){
	cin>>str;
	solve(str,0);
	cout<<minanswer<<" "<<maxanswer;
}