#include<iostream>
#include<cmath>

using namespace std;

long long primeList[10001];
int maxKnownPrimeIdx;

bool IsPrime(long long m) {

	for (int j = 1; j <= maxKnownPrimeIdx; j++) {
		if (m % primeList[j] == 0) {
			return false;
		}
	}
	return true;
}


long long foo(long long n)
{
	if (n > maxKnownPrimeIdx) {
		// search the maxKnownPrimeIdx+1 to nth prime
		long long start = primeList[maxKnownPrimeIdx] + 2;

		do {
			if (IsPrime(start)) {
				maxKnownPrimeIdx++;
				primeList[maxKnownPrimeIdx] = start;
			}
			start += 2;
		}while (n > maxKnownPrimeIdx);
	}
	return primeList[n];
}




int main(){
	primeList[0] = 1;
	primeList[1] = 2;
	primeList[2] = 3;
	maxKnownPrimeIdx = 2;

	int t;
	cin >> t;
	for (int a0 = 0; a0 < t; a0++) {
		int n;
		cin >> n;

		cout << foo(n) << endl;
	}
	return 0;
}