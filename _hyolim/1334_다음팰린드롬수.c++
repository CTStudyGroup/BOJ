#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string n;

string solve(){
	int len=n.size();
	string left=n.substr(0,(len+1)/2);
	string temp=left;

	string rev=left.substr(0,len/2); // 짝수면 그대로, 홀수면 마지막 글자 제외
	reverse(rev.begin(),rev.end());
	temp+=rev;

	if(temp>n) return temp;

	int i=left.size()-1;
	// cout<<left;
	// cout<<i<<" "<<left[i]<<"\n";
	while(i>=0&&left[i]=='9'){
		left[i]='0';
		i--;
	}
	// cout<<i;

	// cout<<left<<" ";
	if(i<0) left='1'+left;
	else left[i]++;
	// cout<<left<<" ";

	if(temp=="9") return "11";
	temp=left;
	len=temp.length();
	rev=left.substr(0,len/2); // 짝수면 그대로, 홀수면 마지막 글자 제외
	reverse(rev.begin(),rev.end());
	temp+=rev;
	// cout<<rev<<" ";
	return temp;
}


int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin>>n;
	cout<<solve();
}