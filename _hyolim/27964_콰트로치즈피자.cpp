#include <iostream>
#include <string>
#include <set>

using namespace std;

int n;
set<string> se;
string cheese="Cheese";
int sign=1;

int main(){
	int n;
	cin>>n;
	string s;

	for(int i=0;i<n;i++){
		cin>>s;
		if(s.length()<cheese.length()) continue;
		sign=1;

		for(int j=0;j<cheese.length();j++){
			if(s[s.length()-1-j]!=cheese[cheese.length()-1-j]) {
				sign=0;
				break;
			}
		}

		if(sign==1) se.insert(s);
		
	}

	if(se.size()>=4) cout<<"yummy";
	else cout<<"sad";

}