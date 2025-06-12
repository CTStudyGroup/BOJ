#include <iostream>
#include <string>
#include <stack>

using namespace std;

struct press{
	int x;
	int n;
	int lastnum;
};

string input_str;
stack<press> st;


int main(){
	cin>>input_str;

	st.push({1,0,0});

	for(auto e:input_str){
		// cout<<"---e: "<<e<<"\n";
		// if(!st.empty()) cout<<st.top().x<<" "<<st.top().str<<"\n";
		// cout<<"size: "<<st.size()<<"\n";

		if(e=='('){
			press temp=st.top();
			st.pop();
	
			// cout<<" *"<<temp.str<<" ";
			int xtemp=temp.lastnum;
			temp.n=temp.n-1;
			st.push(temp);
			st.push({xtemp,0,0});
		}
		else if(e==')'){
			press temp=st.top();
			st.pop();

			press temp2=st.top();
			st.pop();

			temp2.n=temp2.n+(temp.x*temp.n);
			st.push(temp2);
		}
		else{
			press temp=st.top();
			temp.n=temp.n+1;
			temp.lastnum=e-'0';
			st.pop();
			st.push(temp);
		}
	}

	cout<<st.top().n;
}