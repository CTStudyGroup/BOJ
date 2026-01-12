#include<iostream>
#include<algorithm>
using namespace std;

int parent[10001];
bool visit[10001];
int T, N, A, B, u, v;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	cin >> T;

	while (T--)
	{
		cin >> N;

		// 초기화
		for (int i = 1; i <= N; i++)
		{
			visit[i] = false;
			parent[i] = i;
		}

		// 간선정보 입력
		for (int i = 0; i < N - 1; i++)
		{
			cin >> A >> B;
			parent[B] = A;
		}

		// LCA 찾기
		cin >> u >> v;
		visit[u] = true;

		while (u != parent[u])
		{
			u = parent[u];
			visit[u] = true;
		}
		while (true)
		{
			if (visit[v])
			{
				cout << v << '\n';
				break;
			}
			v = parent[v];
		}

	}
}