#include <iostream>

using namespace std;

int n,k;
int arr[300000]={0,};
int visited[100002]={0,};
long answer=0;
int main(){
    cin>>n>>k;
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    int en=0;
    int st=0;

    for(int st=0;st<n;st++){
        while(en<n&&visited[arr[en]]<k){
            visited[arr[en]]++;
            en++;
        }
        if(answer<en-st) answer=en-st;
        if(en==n) break;
        visited[arr[st]]--;
    }
    cout<<answer;
}