#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <cmath>
#include <iomanip>
using namespace std;

struct info{
	string s;
	float f;

	bool operator<(const info& other) const{
		return s<other.s;
	}
};

string str;
vector<string> vec;
vector<info> se;

void input(){
	while(getline(cin,str)){
		vec.push_back(str);

		if(cin.eof()==1) break;

	}
}

void printSE(){
	for(auto e:se){
		cout<<e.s<<" ";
		printf("%.4f",e.f*100);
		cout<<"\n";
	}
}
void solve(){


	sort(vec.begin(),vec.end());
	string last="";
	for(auto& e:vec){
		if(last!=e){
			info i={e,0.0};
			se.push_back(i);
			last=e;
		}
	}

	int summ=1;
	string temp=vec[0];
	int it=0;
	for(int i=1;i<vec.size();i++){

		if(temp!=vec[i]){
			se[it].f=(float)summ/vec.size();
			// cout<<summ<<" "<<vec.size()<<se[it].s<<" "<<se[it].f<<"\n";
			summ=1;
			temp=vec[i];
			it++;
			continue;
		}
		summ++;

	}
	if(summ!=0) se[it].f=(float)summ/vec.size();
	else se[it].f=(float)1.0/vec.size();

	printSE();
}

int main(){
	
	input();
	solve();
}