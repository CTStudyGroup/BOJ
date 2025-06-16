#include <iostream>

using namespace std;


long solve(int a,int b,int c){
	long arr[21][21][21]={0,};
	//1. a,b,c가 전부 0 이하일 경우 1을 반환한다		
	//2. a,b,c 중 하나라도 20보다 크면 w(20,20,20) 을 반환한다.
	//3. a<b && b<c이면 w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c) 를 반환한다.
	//4. 아니라면 다음을 반환한다. w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

	if(a<=0||b<=0||c<=0) return 1;

	if(a>20||b>20||c>20){
		a=20;
		b=20;
		c=20;
	}

	for (int i = 0; i <= 20; ++i)
	{
		for (int j = 0; j <= 20; ++j)
		{
			arr[0][i][j]=1;
			arr[i][0][j]=1;
			arr[i][j][0]=1;
		}
	}

	for (int i = 1; i <= a; ++i)
	{
		for (int j = 1; j <= b; ++j)
		{
			for (int k = 1; k <= c; ++k)
			{
				if(i<j&&j<k){
					arr[i][j][k]=arr[i][j][k-1]+arr[i][j-1][k-1]-arr[i][j-1][k];
				}else{
					arr[i][j][k]=arr[i-1][j][k]+arr[i-1][j-1][k]+arr[i-1][j][k-1]-arr[i-1][j-1][k-1];
				}
			}
		}
	}
		

	return arr[a][b][c];
}

int main(){
	int a,b,c;
	while(1){
		cin>>a>>b>>c;
		if(a==-1&&b==-1&&c==-1) break;
		cout<<"w("<<a<<", "<<b<<", "<<c<<") = "<<solve(a,b,c)<<"\n";;
	}
}