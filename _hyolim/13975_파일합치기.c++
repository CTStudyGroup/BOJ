#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;
int t;

int main(){
	cin>>t;
	while(t--){
		int k;
		long ans=0;
		cin>>k;
		priority_queue<long, vector<long>,greater<long>> q;
		for (int i = 0; i < k; ++i)
		{
			int a;
			cin>>a;
			q.push(a);
		}

		while(q.size()>1){
			long sum=q.top();
			q.pop();
			sum+=q.top();
			q.pop();
			ans+=sum;
			q.push(sum);
		}
		cout<<ans<<"\n";
	}
}