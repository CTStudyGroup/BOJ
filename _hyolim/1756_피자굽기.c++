#include <iostream>

using namespace std;

int d,n;
long arr[300001]={0,};
long curidx;

void input(){
	arr[0]=9876543210987654;
	cin>>d>>n;
	for(int i=1;i<=d;i++){
		cin>>arr[i];
		if(arr[i-1]<arr[i]) arr[i]=arr[i-1];
	}
	curidx=d;
}

int solve(long temp){
	for(int i=curidx;i>=1;i--){
 		// cout<<arr[i]<<" "<<temp<<" \n";
		// 현재 있는 위치에 피자가 들어갈 수 있는지, 그러면 현재 위치를 한 칸 위로 옮기기
		if(arr[i]>=temp) return i;
	}
	// 만약 아무곳에도 들어갈 수 없다면, 실패
	return -1;
}

int main(){
	input();
	int answer=0;
	for(int i=0;i<n;i++){
		long temp; cin>>temp;
		answer=solve(temp);
		// cout<<answer<<"\n";  
		curidx=answer-1;
		if(answer==-1) {
			cout<<0; 
			exit(0);
		}
	}
	cout<<answer;
}