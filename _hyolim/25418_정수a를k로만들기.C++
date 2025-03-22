#include <iostream>
#include <queue>
using namespace std;

int num[1000001]={0,};
int a,k;
queue<int> q;

int main(){
	cin>>a>>k;
	num[k]=1;

	q.push(k);

	for(int temp=q.front();!q.empty();q.pop()){
		temp=q.front();
		if(temp==a) break;

		// 1 더하기
		int next=temp-1;
		if(next<=1000000&&next>=0){
			if(num[next]!=0 && num[next]<num[temp]+1) continue; // 이미 방문한거면 제외

			num[next]=num[temp]+1;
			q.push(next);
		}

		// 2 곱하기
		if(temp%2!=0) continue;
		next=temp/2;
		if(next<=1000000&&next>=0){
			if(num[next]!=0 && num[next]<num[temp]+1) continue; // 이미 방문한거면 제외


			num[next]=num[temp]+1;
			q.push(next);
		}

	}

	cout<<num[a]-1;

}