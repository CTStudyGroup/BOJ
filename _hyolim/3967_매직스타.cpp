#include <iostream>
#include <string>
#include <vector>
#include <cstring>

using namespace std;

vector<int> arr;
int linkedL[6][4]={{1,3,6,8},{1,4,7,11},{2,3,4,5},{8,9,10,11},{2,6,9,12},{5,7,10,12}};
int v[13]={0,};

void input(){

	// arr 채우기
	for(int i=0;i<13;i++){
		arr.push_back(0);
	}

	int tempi=1;
	for(int i=0;i<5;i++){
		string str;
		cin>>str;
		for(int j=0;j<str.length();j++){
			if(str[j]=='.') continue;

			if(str[j]=='x') {
				tempi++;
				continue;
			}

			else arr[tempi]=str[j]-'A'+1;
			v[str[j]-'A'+1]++;
			tempi++;
		}
	}

}

void output(vector<int> ar){
	cout<<"...."<<(char)(ar[0]+'A'-1)<<"....\n";
	cout<<"."<<(char)(ar[1]+'A'-1)<<"."<<(char)(ar[2]+'A'-1)<<"."<<(char)(ar[3]+'A'-1)<<"."<<(char)(ar[4]+'A'-1)<<".\n";
	cout<<".."<<(char)(ar[5]+'A'-1)<<"..."<<(char)(ar[6]+'A'-1)<<"..\n";
	cout<<"."<<(char)(ar[7]+'A'-1)<<"."<<(char)(ar[8]+'A'-1)<<"."<<(char)(ar[9]+'A'-1)<<"."<<(char)(ar[10]+'A'-1)<<".\n";
	cout<<"...."<<(char)(ar[11]+'A'-1)<<"....\n";

}

void checkMagicStar(vector<int> vec){
	// for(auto e:vec){
	// 	cout<<e<< " ";
	// }
	// cout<<"\n";
	for(int i=0;i<6;i++){
		int sum=0;
		for(int j=0;j<4;j++){
			// cout<<linkedL[i][j]<<" "<<vec[linkedL[i][j]]<<"\n";
			sum+=vec[linkedL[i][j]-1];
		}
		// cout<<sum<<" ";
		if(sum!=26){
			// cout<<"\n";
			return;
		}
	}

	output(vec);
	exit(0);
}

void func(int idx,vector<int> vec){
	if(idx>12){
		// 매직스타 되는지 확인
		checkMagicStar(vec);
		return;
	}

	if(arr[idx]){ //이미 들어있을 경우
		vec.push_back(arr[idx]);
		func(idx+1,vec);
	}else{ // 새로 넣어야할 경우
		for(int i=1;i<=12;i++){
			if(v[i]) continue; // 방문했으면 X
			v[i]=1;
			vec.push_back(i);
			func(idx+1,vec);
			vec.pop_back();
			v[i]=0;
		}
	}
}

void solve(){
	// 조합 만들기
	vector<int> vec;
	func(1,vec);
}



int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	input();
	solve();
}