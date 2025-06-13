#include <iostream>
#include <algorithm>

using namespace std;

int n,m;
int crane[51]={0,};
int box[10001]={0,};
bool fin[10001]={0,};

bool isfin(){
	for (int i = 0; i < m; ++i)
	{
		if(!fin[i]) return false;
	}
	return true;
}

void input(){
	cin>>n;
	for (int i = 0; i < n; ++i)
	{
		cin>>crane[i];
	}
	cin>>m;
	for (int i = 0; i < m; ++i)
	{
		cin>>box[i];
	}
}

void solve(){
	sort(crane,crane+n);
	sort(box,box+m);

	if(crane[n-1]<box[m-1]){
		cout<<-1;
		return;
	}

	int t=0;
	while(true){
		if(isfin()){
			cout<<t;
			return;
		}
		for(int i=n-1;i>=0;i--){
			for(int j=m-1;j>=0;j--){
				if(fin[j]) continue;
				if(crane[i]>=box[j]){
					fin[j]=true;
					break;
				}
			}
		}
		t++;
	}

}

int main(){
	// 정렬 후 본인보다 작은 박스를 그리디처럼 없앤다.
	input();
	solve();
}