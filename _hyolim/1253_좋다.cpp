#include <iostream>
#include <algorithm>
using namespace std;
// 이분탐색으로 하나의 숫자당 여러 개의 타겟값을 찾으면 된다.
// 그러니까 하나의 숫자에 다른 원소를 뺀 수를 타겟값으로 찾으면 된다.

int n;
long arr[3000];
int ans=0;
void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
}

void solve(){
	sort(arr,arr+n); // 정렬하고 이분탐색 시작
	for(long i=0;i<n;i++){
		long target=arr[i];
		int left=0;
		int right=n-1;

		while(left<right){
			if(left==i){
				left++;
				continue;
			}

			if(right==i){
				right--;
				continue;
			}

			long sum=arr[left]+arr[right];
			if(sum==target){
				ans++;
				break;
			}
			if(sum>target) right--;
			if(sum<target) left++;
		}
	}
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	input();
	solve();
	cout<<ans;
}
