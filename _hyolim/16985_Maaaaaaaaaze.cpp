#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct point_t{
	int y;
	int x;
	int z;
};

vector<vector<int>> board[5];
int visited[5]={0,};
int direct[6][3]={{0,0,1},{0,1,0},{1,0,0},{0,0,-1},{0,-1,0},{-1,0,0}};
long answer=987654321;

void printB(vector<vector<int>> b[5]){
	cout<<"==========board=========\n";
	for(int i=0;i<5;i++){
		for(int j=0;j<5;j++){
			for(int k=0;k<5;k++){
				cout<<b[i][j][k]<< " ";
			}
			cout<<"\n";
		}
		cout<<"--------------------\n";
	}
}

void printRB(vector<vector<int>> b){
	cout<<"======rotateBoard======\n";
	for(int i=0;i<5;i++){
		for(int j=0;j<5;j++){
			cout<<b[i][j]<<" ";
		}
		cout<<"\n";
	}
}

void input(){
	for(int i=0;i<5;i++){
		vector<vector<int>> tempvec;
		for(int j=0;j<5;j++){
			vector<int> temp;
			for(int k=0;k<5;k++){
				int x;
				cin>>x;
				temp.push_back(x);

			}
			tempvec.push_back(temp);
		}
		board[i]=tempvec;
	}
	// printB(board);
}

int bfs_3d(vector<vector<int>> maze[5], point_t start, point_t end) {
    queue<point_t> q;
    q.push({start.y, start.x, start.z});       

    point_t temp;
    int v[5][5][5] = {0,};
    v[start.z][start.y][start.x] = 1;          

    while(!q.empty()){
        temp = q.front(); 
        q.pop();

        for(int i=0;i<6;i++){
            int ny = temp.y + direct[i][0];
            int nx = temp.x + direct[i][1];
            int nz = temp.z + direct[i][2];

            if(ny<0||ny>4||nx<0||nx>4||nz<0||nz>4) continue;
            if(v[nz][ny][nx]) continue;
            if(!maze[nz][ny][nx]) continue;

            v[nz][ny][nx] = v[temp.z][temp.y][temp.x] + 1;
            q.push({ny, nx, nz});
        }
    }

    int dist = v[end.z][end.y][end.x];     
    return dist ? dist - 1 : 0;  
}

vector<vector<int>> rotateB(vector<vector<int>> b){
	vector<vector<int>> tempB;
	for(int i=0;i<5;i++){
		vector<int> temp;
		for(int j=0;j<5;j++){
			temp.push_back(b[4-j][i]);
		}
		tempB.push_back(temp);
	}
	// printRB(tempB);
	return tempB;
}

void makeMaze(int depth,vector<vector<int>> maze[5]){
    if(depth == 5){
        static point_t corners[4][2] = {
            {{0,0,0},{4,4,4}},
            {{0,0,4},{4,4,0}},
            {{0,4,0},{4,0,4}},
            {{0,4,4},{4,0,0}},
        };
        for (int i=0; i<4; i++){
            point_t s = corners[i][0];
            point_t e = corners[i][1];

            if (!maze[s.z][s.y][s.x] || !maze[e.z][e.y][e.x]) continue;
            int dist = bfs_3d(maze, s, e);
            if(dist && answer > dist) answer = dist;
        }
        return;
    }

	for(int i=0;i<5;i++){
		if(visited[i]) continue;
		vector<vector<int>> RB=board[i];
		visited[i]=true;
		for(int j=0;j<4;j++){
			if(j>0) RB=rotateB(RB); // 어차피 4번 돌면 마지막에 원상태가 됨
			maze[depth]=RB;
			makeMaze(depth+1,maze);
		}
		visited[i]=false;
	}
}

void solve(){
	vector<vector<int>> maze[5];
	makeMaze(0,maze);
}

int main(){
	input();
	solve();
	if(answer==987654321) cout<<-1;
	else cout<<answer;
}