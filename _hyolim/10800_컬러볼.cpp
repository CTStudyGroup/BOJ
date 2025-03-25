#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct ball{
	int w;
	int c;
	int idx;
};

int ans[200021]={0,};
int C[200021]={0,}; // 특정 색 공들의 크기 합
int S[200021]={0,}; // 특정 크기 공들의 크기 합
int n;

bool cmp(ball &a, ball &b){
	if(a.w==b.w) return a.c<b.c;
	return a.w<b.w;
}

int main(){
	vector<ball> v;
	
	cin>>n;
	for(int i=0;i<n;i++){
		int w,c;
		cin>>c>>w;
		v.push_back({w,c,i});
	}
	sort(v.begin(),v.end(),cmp);

	int sum=0; // 모든 공 크기 합

	for(int i=0;i<n;i++){
		int w=v[i].w;
		int c=v[i].c;
		int idx=v[i].idx;

		C[c]+=w;
		S[w]+=w;
		sum+=w;

		ans[idx]=sum-C[c]-S[w]+w;
		if(i!=0&&(v[i-1].c==c)&&(v[i-1].w==w)) ans[idx]=ans[v[i-1].idx];

	}

	for(int i=0;i<n;i++) cout<<ans[i]<<"\n";
}