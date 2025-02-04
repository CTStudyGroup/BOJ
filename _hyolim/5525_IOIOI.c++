#include <iostream>
#include <string>

using namespace std;

// IOI 개수 세기 개수가 n이 되면 ++
int n;
string s;
int m;
int ans=0;

void input(){
    cin>>n>>m>>s;
}

void solve(){
    int i=-1;
    int k=0;
    while(i<=m){
        i++;
        if(s[i]=='O') continue;
        if(s[i+1]=='O' && s[i+2]=='I'){
            k++;
            if(k==n){
                ans++;
                k--;
            }
            i++;
        }else{
            k=0;
        }
    }
}

int main(){
    input();
    solve();
    cout<<ans;
}