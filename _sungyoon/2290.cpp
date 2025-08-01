#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x;
    string s;
    vector<int> v;
};

int dx[] = {-1, 0, 1, 0, 1, -1, -1, 1};
int dy[] = {0, 1, 0, -1, -1, 1, -1, 1};
int arr[10][7] = {
    {1,1,1,0,1,1,1},
    {0,0,1,0,0,1,0}, 
    {1,0,1,1,1,0,1},
    {1,0,1,1,0,1,1}, 
    {0,1,1,1,0,1,0}, 
    {1,1,0,1,0,1,1}, 
    {1,1,0,1,1,1,1}, 
    {1,0,1,0,0,1,0}, 
    {1,1,1,1,1,1,1}, 
    {1,1,1,1,0,1,1}, 
};
int s;
string n;

void monitor(char c, int idx){
    int x = c-'0';
    if(idx%3==0){
        cout << " ";
        if(arr[x][idx]==1){for(int i=0; i<s; i++) cout << "-"; }
        else {for(int i=0; i<s; i++) cout << " "; }
        cout << "  ";
    }
    else{
        if(arr[x][idx]==1){cout << "|";}
        else cout << " ";
        if(idx%3==1) {for(int i=0; i<s; i++) cout << " ";}
        else cout << " ";
    }
}

void solve() {
    for(int j=0; j<n.size(); j++){
        monitor(n[j],0);
    }
    cout << "\n";
    for(int a=0; a<s; a++){
        for(int j=0; j<n.size(); j++){
            for(int i=1; i<3; i++){
                monitor(n[j],i);
            }
        }
        cout << "\n";
    }
    for(int j=0; j<n.size(); j++){
        monitor(n[j],3);
    }
    cout << "\n";
    for(int a=0; a<s; a++){
        for(int j=0; j<n.size(); j++){
            for(int i=4; i<6; i++){
                monitor(n[j],i);
            }
        }
        cout << "\n";
    }
    for(int j=0; j<n.size(); j++){
        monitor(n[j],6);
    }
    cout << "\n";
}

void input() {
    cin >> s >> n;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
