#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

struct person{
	int s;
	int e;

	bool operator<(const person& other) const{
		if(s<other.s) return true;
		else{
			return false;
			if(e<other.e) return true;
		}
		return false;
	}
};

struct name{
	int e;
	int num;
    bool operator<(const name &other) const {
        if (e < other.e) return true;
        if (e > other.e) return false;
        return num < other.num;
    }
};

int n;
vector<person> vec;
priority_queue<name> pq;
priority_queue<int> left_seats;
int cnt[100001]={0,};                                    

void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		int s,e;
		cin>>s>>e;
		person p={s,e};
		vec.push_back(p);
	}
}

void solve(){
	sort(vec.begin(),vec.end());
	// for(auto e:vec){
	// 	cout<<e.s<<" "<<e.e<<"\n";
	// }

	int seat=0;
	for(int i=0;i<vec.size();i++){
		// 다음으로 들어오는 사용자의 시작시간과 이용중이 ㄴ사용자의 끝나는 시간을 비교
		// 다음 사용자가 들어오기 전에 끝난 사용자가 있으면, 자리 번호를 저장하고 pq에서 제거
		// 찾기
		while(!pq.empty()){
			if(-pq.top().e<=vec[i].s){
				left_seats.push(-pq.top().num);
				pq.pop();
			}
			else break;
		}
		if(left_seats.empty()){
			pq.push({-vec[i].e,seat});
			cnt[seat++]++;
		}else{
			// 빈자리가 있을 때
			int temp_seat=-left_seats.top();
			pq.push({-vec[i].e,temp_seat});
			cnt[temp_seat]++;
			left_seats.pop();
		}
	}
	cout<<seat<<"\n";
	 for(int i=0; i<seat; i++)
        cout << cnt[i] << " ";
       
}


int main(){
	input();
	solve();

}