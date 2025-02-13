#include <iostream>
#include <algorithm>
using namespace std;

int n;
int arr[1001];
int answer=0;
// 정렬 후 더하기
void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}

}

bool comparator(int a,int b){
	return a>b;
}

void solve(){
	sort(arr,arr+n,comparator);
	answer=0;
	int tempN=arr[0];
	for(int i=1;i<n;i++){
		answer+=arr[i];
		answer+=tempN;
	}
	cout<<answer;
}
int main(){
	input();
	solve();
}