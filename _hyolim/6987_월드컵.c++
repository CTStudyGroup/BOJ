#include <iostream>

using namespace std;

// 승리와 패는 다 더했을 때 같아야한다.
// 무승부는 나중에 생각..

int arr[6][3];

void printA(){
	cout<<"----------------\n";
	for(int i=0;i<6;i++){
		for(int j=0;j<3;j++){
			cout<<arr[i][j]<<" ";
		}
		cout<<"\n";
	}

}

void input(){
	for(int i=0;i<6;i++){
		for(int j=0;j<3;j++){
			cin>>arr[i][j];
		}
	}
	// printA();
}

bool solve(){
	// 행마다 합이 5가 아니면 안된다
	for(int i=0;i<6;i++){
		int rowsum=0;
		for(int j=0;j<3;j++){
			rowsum+=arr[i][j];
		}
		if(rowsum!=5) return false;
	}

	// 0 번째 열을 전부 더하고, 2번째 열을 전부 더해서 같은지 확인
	int s1=0;
	int s2=0;

	for(int i=0;i<6;i++){
		s1+=arr[i][0];
		s2+=arr[i][2];
	}
	// cout<<s1<<" "<<s2<<"\n";
	if(s1!=s2) return false;

	// 무승부 처리
	int temp=arr[0][1];
	arr[0][1]=0;
	for(int i=1;i<6;i++){
		if(!arr[i][1]) continue; // 0이면 넘어가기
		// temp에 숫자가 남아있을 경우
		temp=abs(temp-arr[i][1]); // temp 갱신
		arr[i][1]=0;
	}
	if(temp!=0) return false;

	return true;
}

int main(){
	for(int i=0;i<4;i++){
		input();
		cout<<solve()<<" ";
	}

}