#include <iostream>
#include <stack>

using namespace std;

int n;
stack<pair<int,int>> s; // 점수, 시간
long answer=0;

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin>>n;
	for(int i=0;i<n;i++){
		int x,a,t;
		cin>>x;

		if(x!=0){
			cin>>a>>t;
			s.push({a,t});
			// cout<<a<<" "<<t<<"\n";
		}

		if(!s.empty()){
			int tempa,tempb;
			tempa=s.top().first;
			tempb=s.top().second;
			s.pop();

			s.push({tempa,tempb-1});
			// cout<<"*"<<s.top().first<<" "<<s.top().second<<"\n";

			if(s.top().second == 0) {
				// cout<<"&"<<s.top().first<<" "<<s.top().second<<"\n";

				answer+=s.top().first;
				s.pop();
			}
		}
	}
	cout<<answer;
}