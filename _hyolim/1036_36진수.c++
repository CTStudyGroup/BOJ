#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

struct Base36{
	int c;
	int d[52];
	Base36() : c(0){
		fill(d,d+52,0);
	}
};

Base36 base[36],r;

void Mul(Base36 &res, const Base36 &a, int m){
	int carry=0;
	for(int i=0;i<52;i++){
		res.d[i]=a.d[i]*m+carry;
		carry=res.d[i]/36;
		res.d[i]%=36;
	}
}

bool cmp(int a,int b){
	Base36 ta,tb;

	Mul(ta,base[a],35-base[a].c);
	Mul(tb,base[b],35-base[b].c);
	for(int i=51;i>=0;i--){
		if(ta.d[i]>tb.d[i]) return true;
		if(ta.d[i]<tb.d[i]) return false;
	}
	return false;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    int idx[36];

    for(int i=0;i<36;i++){
    	base[i].c=i;
    	idx[i]=i;
    }

    cin>>n;
    while(n--){
    	string s;
    	cin>>s;

    	for(int i=0;i<s.length();i++){
    		if(s[i]<'A') s[i]=s[i]-'0';
    		else s[i]=s[i]-'A'+10;
    	}
    	for(int i=0;i<s.length();i++){
    		base[s[s.length()-i-1]].d[i]++;
    	}
    }

    sort(idx,idx+35,cmp);

    cin>>k;

    for(int i=0;i<k;i++){
    	base[idx[i]].c=35;
    }

    int carry=0;
    for(int i=0;i<52;i++){
    	int t=carry;
    	for(int j=0;j<36;j++){
    		t+=base[j].c*base[j].d[i];
    	}
    	r.d[i]=t%36;
    	carry=t/36;
    }

    bool sig=false;
    for(int i=51;i>=0;i--){
    	if(sig||r.d[i]!=0||i==0){
    		if(r.d[i]<10) cout<<(char)(r.d[i]+'0');
    		else cout<<(char)(r.d[i]-10+'A');
    		sig=true;
    	}
    }
}
