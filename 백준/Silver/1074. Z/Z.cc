#include <iostream>
using namespace std;

long long order = 0;
void ZSearch(int startrow, int startcol, int endrow, int endcol, int r, int c)
{
	int midrow, midcol;
	long long arrsize = (long long)endrow - (long long)startrow + 1;
	if (startrow == endrow && startcol == endcol)
	{

	}
	else
	{
		midrow = (startrow + endrow) / 2;
		midcol = (startcol + endcol) / 2;
		if (midrow >= r)
		{
			if (midcol >= c)
			{
				ZSearch(startrow, startcol, midrow, midcol, r, c);
			}
			else
			{
				order += arrsize * arrsize / 4;
				ZSearch(startrow, midcol + 1, midrow, endcol, r, c);
			}
		}
		else
		{
			if (midcol >= c)
			{
				order += arrsize * arrsize / 4 * 2;
				ZSearch(midrow + 1, startcol, endrow, midcol, r, c);
				
			}
			else
			{
				order += arrsize * arrsize / 4 * 3;
				ZSearch(midrow + 1, midcol + 1, endrow, endcol, r, c);
			}
		}
	}
}

int main(void)
{
	int N, r, c; cin >> N >> r >> c;
	int size = 1;
	int power = N;
	for (; power--;)
	{
		size *= 2;
	}

	ZSearch(0, 0, size - 1, size - 1, r, c);
	cout << order;
	return 0;
}