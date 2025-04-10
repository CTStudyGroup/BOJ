#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int n;
int arr[500001]={0,};
vector<int> pending;
long answer=0;
int main(){
	cin>>n;
	for(int i=0;i<n;i++){
		int x;
		cin>>x;
		if(arr[x]) pending.push_back(x);
		else arr[x]=x;
	}

	sort(pending.begin(),pending.end());
	int idx=1;
	for(auto e: pending){
		for(int i=idx;i<=n;i++){
			if(!arr[i]){
				answer+=abs(i-e);
			} 
		}
	}
	cout<<answer;
}