#include <iostream>
#include <string>

using namespace std;

string a,b,c; 
bool sig=true;

void solve(int ap,int bp,int cp){
	if(cp==c.length()){
		sig=false;
		return;
	}

	if(a[ap]==c[cp]) solve(ap+1,bp,cp+1);
	if(b[bp]==c[cp]) solve(ap,bp+1,cp+1);
}

int main(){
	int t; cin>>t;
	for (int i = 0; i < t; ++i)
	{
		cin>>a>>b>>c;
		sig=true;
		cout<<"Data set "<<i+1<<": ";
		solve(0,0,0);
		if(sig) cout<<"no\n";
		else cout<<"yes\n";
	}
}