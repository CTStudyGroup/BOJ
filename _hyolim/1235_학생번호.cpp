#include <iostream>
#include <string>

using namespace std;

string stu[1001];
int n;
int len=0;

void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>stu[i];
	}
	len=stu[0].length();
}

int solve(){
	string temp1;
	string temp2;
	for(int i=len-1;i>=0;i--){
		bool sig=true;
		for(int j=0;j<n;j++){ // 사람
			
			for(int k=j+1;k<n;k++){
				temp1=stu[j].substr(i,len);
				temp2=stu[k].substr(i,len);
				if(temp1==temp2) sig=false;

			}
		}
		if(sig) return len-i;
	}
	return len;
}

int main(){
	input();
	cout<< solve();
}