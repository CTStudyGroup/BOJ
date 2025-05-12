#include<iostream>
using namespace std;

struct point_t{
    int y,x;
};

int n,ans;
int board[500][500]={0,};
int dx[4]={0,1,0,-1};
int dy[4]={-1,0,1,0};

int percent[9]={1,1,7,7,10,10,2,2,5};

int xdx[4][10]={
    {-1,1,-1,1,-1,1,-2,2,0,0},
    {-1,-1,0,0,1,1,0,0,2,1},
    {-1,1,-1,1,-1,1,-2,2,0,0},
    {1,1,0,0,-1,-1,0,0,-2,-1}
};
int ydy[4][10]={
    {0,0,1,1,2,2,1,1,3,2},
    {-1,1,-1,1,-1,1,-2,2,0,0},
    {0,0,-1,-1,-2,-2,-1,-1,-3,-2},
    {-1,1,-1,1,-1,1,-2,2,0,0}
};

void input(){
    cin>>n;
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            cin>>board[i][j];
}

void spread_sand(int y,int x,int dir){
    int ny=y+dy[dir];
    int nx=x+dx[dir];
    if(board[ny][nx]==0) return;

    int sand=board[ny][nx];
    int temp=sand;

    for(int i=0;i<9;i++){
        int sy=y+ydy[dir][i];
        int sx=x+xdx[dir][i];
        int amount=(temp*percent[i])/100;

        if(sy<0||sx<0||sy>=n||sx>=n)
            ans+=amount;
        else
            board[sy][sx]+=amount;

        sand-=amount;
    }

    int alpha_y=y+ydy[dir][9];
    int alpha_x=x+xdx[dir][9];

    if(alpha_y<0||alpha_x<0||alpha_y>=n||alpha_x>=n)
        ans+=sand;
    else
        board[alpha_y][alpha_x]+=sand;

    board[ny][nx]=0;
}

void solve(){
    int y=n/2;
    int x=n/2;
    int dir=0;
    int move_len=1;

    while(1){
        for(int k=0;k<2;k++){
            for(int i=0;i<move_len;i++){
                spread_sand(y,x,dir);
                y+=dy[dir];
                x+=dx[dir];

                if(y==0&&x==0){
                    cout<<ans;
                    return;
                }
            }
            dir=(dir+1)%4;
        }
        move_len++;
    }
}

int main() {
    input();
    solve();
    return 0;
}