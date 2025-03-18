#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

struct Base36{
	int c; // 해당 숫자의 실제 값
	int d[52]; // 자릿수별로 이 숫자가 몇 번 등장했는지 기록
	Base36() : c(0){
		fill(d,d+52,0);
	}
};

Base36 base[36],r; // 각 숫자가 입력에서 몇 번 등장했는지 자리별로 기록, 모든 입력수를 합산한 최종 결과

void Mul(Base36 &res, const Base36 &a, int m){ // a*m = res
	int carry=0;
	for(int i=0;i<52;i++){
		res.d[i]=a.d[i]*m+carry;
		carry=res.d[i]/36;
		res.d[i]%=36;
	}
}

bool cmp(int a,int b){
	Base36 ta,tb;

	Mul(ta,base[a],35-base[a].c); // a를 'Z'로 바꾸면 생기는 이득을 ta에 넣음
	Mul(tb,base[b],35-base[b].c);
	for(int i=51;i>=0;i--){
		if(ta.d[i]>tb.d[i]) return true; // 이득이 큰 순서대로 정렬
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

    // Z로 변환한 값 더하기
    int carry=0;
    for(int i=0;i<52;i++){
    	int t=carry;
    	for(int j=0;j<36;j++){
    		t+=base[j].c*base[j].d[i];
    	}
    	r.d[i]=t%36;
    	carry=t/36;
    }

    // 출력하기
    bool sig=false;
    for(int i=51;i>=0;i--){
    	if(sig||r.d[i]!=0||i==0){
    		if(r.d[i]<10) cout<<(char)(r.d[i]+'0');
    		else cout<<(char)(r.d[i]-10+'A');
    		sig=true;
    	}
    }
}
