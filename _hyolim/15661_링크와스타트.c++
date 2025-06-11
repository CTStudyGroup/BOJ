#include <iostream>
#include <vector>

using namespace std;

int n;
int s[20][20];

int calc(vector<int> team){
	int sum=0;
	for (int i = 0; i < team.size(); ++i)
	{
		for (int j = 0; j < team.size(); ++j)
		{
			if(i==j) continue;
			sum+=s[team[i]][team[j]];
		}
	}
	return sum;
}

int main(){
	cin>>n;
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < n; ++j)
		{
			cin>>s[i][j];
		}
	}

	int answer=987654321;
	for (int mask = 1; mask < (1<<n)-1; ++mask)
	{
		vector<int> start, link;
		for(int i=0;i<n;++i){
			if(mask&(1<<i)) start.push_back(i);
			else link.push_back(i);
		}

		int startsc=calc(start);
		int linksc=calc(link);
		answer=min(answer,abs(startsc-linksc));

	}
	cout<<answer;
}