#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;


int r,c,k;
vector<vector<int>> vec;

void input(){
	cin>>r>>c>>k;
	for(int i=0;i<3;i++){
		vector<int> tempvec;

		for(int j=0;j<3;j++){
			int temp; cin>>temp;
			tempvec.push_back(temp);
		}
		vec.push_back(tempvec);
	}
}

vector<int> cal(vector<int> v){
	map<int,int> m;
	for(auto e:v){
		if(e==0) continue;
		m[e]++;
	}

	// 정렬
	vector<pair<int,int>> v2(m.begin(),m.end());
	sort(v2.begin(),v2.end(),[](auto& a,auto& b){
		if(a.second==b.second){
			return a.first<b.first;
		}
		return a.second<b.second;
	});

	vector<int> temp;
	for(auto e:v2){
		if(temp.size()>=100) return temp;
		temp.push_back(e.first);
		temp.push_back(e.second);
	}

	return temp;
}




void solve(){
	for(int t=0;t<=100;t++){

		if (r-1<vec.size() && c-1<vec[0].size() && vec[r-1][c-1] == k) {
		    cout << t;
		    exit(0);
		}	
		// r 연산 하나
		int maxSize=0;
		vector<vector<int>> newVec;

		if(vec.size()>=vec[0].size()){
			for(int i=0;i<vec.size();i++){
				vector<int> temp=cal(vec[i]);
				if(maxSize<temp.size()) maxSize=temp.size();

				newVec.push_back(temp);
			}

			// 0 채우기 
			for(int i=0;i<newVec.size();i++){
				for(int j=newVec[i].size();j<maxSize;j++){
					newVec[i].push_back(0);
				}
			}

			vec=newVec;
		}

		// c 연산 하나
		else{
			for(int i=0;i<vec[0].size();i++){
				vector<int> invec;
				for(int j=0;j<vec.size();j++){
					invec.push_back(vec[j][i]);
				}

				vector<int> temp=cal(invec);
				if(maxSize<temp.size()) maxSize=temp.size();

				newVec.push_back(temp);
			}

			// 0 채우기 
			for(int i=0;i<newVec.size();i++){
				for(int j=newVec[i].size();j<maxSize;j++){
					newVec[i].push_back(0);
				}
			}

			vec.clear();
			for(int j=0;j<newVec[0].size();j++){ // 열
				vector<int> temp;
				for(int i=0;i<newVec.size();i++){ // 행
					temp.push_back(newVec[i][j]);
				}
				vec.push_back(temp);
			}

		}

		// cout<<"-----\n";
		// for(auto e:vec){
		// 	for(auto w:e){
		// 		cout<<w<<" ";
		// 	}
		// 	cout<<"\n";
		// }

	}
	cout<<"-1";
}

int main(){
	input();
	solve();
}