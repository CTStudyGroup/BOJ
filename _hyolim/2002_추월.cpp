#include <iostream>
#include <queue>
#include <string>
#include <vector>

using namespace std;

int n;
vector<string> inV;
vector<string> outV;
bool isIn[10001];
long ans=0;

int main(){
	cin>>n;
	for(int i=0;i<n;i++){
		string temp;
		cin>>temp;
		inV.push_back(temp);
	}

	for(int i=0;i<n;i++){
		string temp;
		cin>>temp;
		outV.push_back(temp);
	}

	int ip=0;
	int op=0;

	while(ip<n&&op<n){
		while(isIn[ip]) ip++;
		// cout<<inV[ip]<<" "<<outV[op]<<"\n";
		// 둘이 같을 때
		if(inV[ip]==outV[op]){
			ip++;
			op++;
			continue;
		}
		ans++;
		// 둘이 다를 때, output이 input에 있는지 확인
		for(int i=ip;i<n;i++){
			if(inV[i]==outV[op]){
				isIn[i]=true;
				op++;
				break;
			}
		}
	}

	cout<<ans;
}