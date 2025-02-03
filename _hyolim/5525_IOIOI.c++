#include <iostream>
#include <string>

using namespace std;

string s;

int n;
int lens;
int ans=0;

void input(){
    cin>>n;
    cin>>lens;
    cin>>s;
}

// 전체 다 확인하는 함수
bool checkIOI(int idx){
    int i=0;

    while(i<n){
        if(s[idx+2*i]!='I'||s[idx+2*i+1]!='O') {
            return false;
        }
        i++;
    }

    if(s[idx+(2*n)]!='I') {
        return false;
    }
    return true;
}

// 양쪽만 확인하는 함수
bool checkS(int idx){
    // 양쪽 맞는지 확인
    if(s[idx+2*n-1]=='O' && s[idx+2*n]=='I'){
        return true;
    } 
    return false;
}

void solve(){
    int i=0;
    while(i<lens-2*n){
        if(checkIOI(i)) {
            // cout<<"i: "<<i<<"\n";
            i+=(2*n-1);
            ans++;
            // 하나 길게 맞는거 확인했으니 이제 양쪽만 확인하기
            while(checkS(i)){
                // cout<<i;
                i+=2;
                ans++;
            }
        }else{
            i++;

        }
    }
}

int main(){
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    input();
    solve();
    cout<<ans;
}