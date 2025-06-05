#include <iostream>

using namespace std;

// 똑같이 유니온파인드 문제
int n;
int parent[1000001];
int parentcnt[1000001];

int getParent(int x){
	if(parent[x]==x) return x;
	return parent[x]=getParent(parent[x]);
}
void unionParent(int a, int b){
	int ra = getParent(a);
	int rb = getParent(b);
	if(ra == rb) return;

	if(ra > rb) {
		parent[ra] = rb;
		parentcnt[rb] += parentcnt[ra];
	} else {
		parent[rb] = ra;
		parentcnt[ra] += parentcnt[rb];
	}

}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin>>n;
	for (int i = 0; i <= 1000000; ++i)
	{
		parent[i]=i;
		parentcnt[i]=1;
	}
	for (int i = 0; i < n; ++i)
	{
		char c;
		int a,b;
		cin>>c;
		if (c=='I')
		{
			cin>>a>>b;
			unionParent(a,b);
		}else{
			cin>>a;
			// for (int j = 0; j < n; ++j)
			// {
			// 	cout<<parent[j]<<" "<<parentcnt[j]<<"\n";
			// }
			cout<<parentcnt[getParent(a)]<<"\n";
		}
	}
}