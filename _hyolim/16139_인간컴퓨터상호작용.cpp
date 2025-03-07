#include <iostream>
#include <string>

using namespace std;

string S;
int strl;
int t;
int arr[26][200001]={0,};

void input(){
	cin>>S;
	strl=S.length();

	for(int i=1;i<=strl;i++){
		for(int j=0;j<26;j++){
			arr[j][i]+=arr[j][i-1];
		}

		arr[S[i-1]-'a'][i]++;
	}
}

void  printarr(){
	for(int i=0;i<26;i++){
		cout<<(char)('a'+i)<<": ";
		for(int j=1;j<=strl;j++){
			cout<<arr[i][j]<<" ";
		}
		cout<<"\n";
	}
}

void solve(){
	// printarr();
	cin>>t;

	char a;
	int l,r;
	int cnt=0;

	while(t--){
		cin>>a>>l>>r;
		cout<<arr[a-'a'][r+1]-arr[a-'a'][l]<<"\n";
	}
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	input();
	solve();
}