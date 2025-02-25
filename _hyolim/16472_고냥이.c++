#include <iostream>
#include <set>
#include <string>

using namespace std;

int n;
string str;
set<char> s;
int maxS=0;

void input(){
	cin>>n;
	cin>>str;

}

void solve(){
	int p1=0,p2=0;
	// int w=0;
	while(p1<str.length()){

		// for(int i=p1;i<=p2;i++){
		// 	cout<<str[i];
		// }
		// cout<<"\n";
		// 만약 p2가 가르키는 것을 넣어도, 최대 문자열을 넘지 않는다면 한 칸 더 옮기기
		s.insert(str[p2]);
		// cout<<s.size();
		if(s.size()<=n){
			if(p2>=str.length()-1) break;
			p2++;
		}else{
			// 넘는다면 그것이 최대이기 때문에 갱신
			if(maxS<(p2-p1)){
				// cout<<p1<<" "<<str[p1]<<" "<<p2<<str[p2]<<"\n";
				maxS=p2-p1;
			}

			// p1에 해당하는 문자가 있으면 지우면 안됨
			bool sig=true;
			for(int i=p1+1;i<=p2;i++){
				if(str[i]==str[p1]){
					sig=false;
				}
			}
			if(sig) s.erase(str[p1]);
			
			p1++;
		}
		// 	cout<<"&";
		// for(auto e:s){
		// 	cout<<e<<" ";
		// }
		// cout<<maxS;
		// w++;
	}
	if(s.size()<=n){
		if(maxS<(p2-p1)){
			// cout<<p1<<" "<<str[p1]<<" "<<p2<<str[p2]<<"\n";
			maxS=p2-p1+1;
		}
	}
}

int main(){
	input();
	solve();
	cout<<maxS;
}