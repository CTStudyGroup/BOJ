#include <iostream>
#include <algorithm>
#include <climits>
int dx[4] = { 0,0,-1,1 }; 
int dy[4] = { -1,1,0,0 }; 
int n; 
int map[10][10]; 
int visited[10][10]; 
int result = INT_MAX; 
using namespace std; 
void dfs(int sum, int cnt) {
	if (cnt == 3) {
		result = min(result, sum); return; 
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			int check = 0; 
			int nx, ny; 		
			for (int k = 0; k < 4; k++) {
				nx = j + dx[k]; 
				ny = i + dy[k]; 
				if (nx < 0 || nx >= n || ny < 0 || ny >= n)continue; 
				if (visited[ny][nx])continue; 
				check++; 
			}
			if (check == 4) {
				int ssum = map[i][j]; 
				for (int k = 0; k < 4; k++) {
					nx = j + dx[k];
					ny = i + dy[k];
					visited[ny][nx] = 1; 		
					ssum += map[ny][nx]; 
				}
				visited[i][j] = 1;
				sum += ssum; 
				cnt++; 
				dfs(sum, cnt); 
				sum -= ssum; 
				cnt--; 
				for (int k = 0; k < 4; k++) {
					nx = j + dx[k];
					ny = i + dy[k];
					visited[ny][nx] = 0;				
				}
				visited[i][j] = 0;
			
			}
		}
	}

}
int main() {
	cin >> n; 
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> map[i][j]; 
		}
	}
	dfs(0, 0);
	cout << result; 
}