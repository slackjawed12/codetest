#include <iostream>
using namespace std;

int main(void)
{
	double R;
	cin >> R;

	double S = R * R;
	cout << fixed;
	cout.precision(6);
	cout << S * 3.14159265358979323846 << '\n';
	cout << R*R*2<<'\n';

	return 0;
}