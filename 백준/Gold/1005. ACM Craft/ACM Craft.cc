#include <iostream>
#include <vector>
using namespace std;
#define NMAX 1000

int T;
int *N;
int *K;
int *W;
int** D;
vector<int>** adj;
int** info;
int* ans;

void Input()
{
	cin >> T;
	N = new int[T];
	K = new int[T];
	W = new int[T];
	D = new int*[T];
	adj = new vector<int>*[T];
	info = new int* [T];
	ans = new int[T];
	for (int i = 0; i < T; i++)
	{
		D[i] = new int[NMAX+2];
		adj[i] = new vector<int>[NMAX + 2];
		info[i] = new int[NMAX + 2];

		cin >> N[i] >> K[i];
		for (int j = 1; j <= N[i]; j++)
		{
			cin >> D[i][j];
			info[i][j] = 0;
		}
		for (int j = 0; j < K[i]; j++)
		{
			int x, y;
			cin >> x >> y;
			adj[i][y].push_back(x);
		}
		cin >> W[i];
	}
}

int MinTime(int t, int start)
{
	if (info[t][start] == 1)
	{
		return D[t][start];
	}
	else
	{
		info[t][start] = 1;
		int max = 0;
		int add = 0;
		for (int i = 0; i < adj[t][start].size(); i++)
		{
			add = MinTime(t, adj[t][start][i]);
			if (add > max)
			{
				max = add;
			}
		}
		D[t][start] += max;
		return D[t][start];
	}
}

void Output()
{
	for (int i = 0; i < T; i++)
	{
		cout << ans[i] << '\n';
	}
}

int main()
{
	Input();
	for (int i=0; i<T; i++)
	{
		ans[i] = MinTime(i, W[i]);
	}
	Output();
	return 0;
}