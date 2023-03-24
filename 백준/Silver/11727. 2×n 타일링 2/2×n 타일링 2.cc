#include <iostream>
using namespace std;

int dp[1001] = { 0, 1, 3 };
int Tile(int num)
{
	for (int i = 3; i <= num; i++)
	{
		dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 10007;
	}
	return dp[num];
}

int main(void)
{
	int N;
	cin >> N;

	cout << Tile(N);

	return 0;
}