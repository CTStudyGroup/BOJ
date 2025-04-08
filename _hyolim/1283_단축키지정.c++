#include <iostream>
#include <vector>

#include <string>

using namespace std;

int n;
vector<pair<string, int>> vec; // 문자, 괄호 인덱스
int check[28]={0,};

void printVec(){
	for(auto e:vec){
		cout<<e.first<<" "<<e.second<<"\n";
	}
}

void input(){
	cin>>n;

	for(int i=0;i<=n;i++){
		string temp;
		getline(cin,temp);
		if(temp!="") vec.push_back({temp,-1});
	}
	// printVec();
}

int trans(char t){
	if(t>='A'&&t<='Z') return t-'A';
	else if(t==' ') return -1;
	else return t-'a';
}

void solve(){
	for(int i=0;i<n;i++){
		string temp=vec[i].first;


		// 1. 맨 왼쪽 확인하기
		int intT=trans(temp[0]);
		if(!check[intT]){
			check[intT]=1;
			vec[i].second=0;
			continue;
		}

		// 띄워쓰기가 있는지 확인
		for(int j=0;j<temp.length()-1;j++){
			if(temp[j]==' '){
				intT=trans(temp[j+1]);
				if(!check[intT]){
					check[intT]=1;
					vec[i].second=j+1;
					break;
				}
			}
		}
		if(vec[i].second!=-1) continue;

		// // 왼쪽부터 차례대로 알파벳을 보면서 
		for(int j=0;j<temp.length();j++){
			intT=trans(temp[j]);
			if(intT==-1) continue;
			if(!check[intT]){
				check[intT]=1;
				vec[i].second=j;
				break;
			}
		}
	}
}

void output(){
	for(int i=0;i<vec.size();i++){
		string temp=vec[i].first;
		int idx=vec[i].second;

		if(idx==-1){
			cout<<temp<<"\n";
			continue;
		}else{
			for(int j=0;j<temp.length();j++){
				if(j==idx){
					cout<<"["<<temp[j]<<"]";
				}else{
					cout<<temp[j];
				}
			}
			cout<<"\n";
		}
	}
}

int main(){
	input();
	solve();
	output();
}