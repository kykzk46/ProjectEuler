#include<iostream>
#include<vector>
#include<cmath>

using namespace std;

vector<long long> primeList;


int BinarySearch(long long target, vector<long long> sortedArray){
	int left = 1;
	int right = sortedArray.size()-1;
	while (left < right) {
		int mid = (left + right) / 2;

		if (target < sortedArray[mid]) {
			right = mid;
		} else {
			left = mid + 1;
		}
	}

	return left;
}
/***********************************************************************
* Using quotion to check prime is too slow
***********************************************************************/
bool IsPrime(long long m) {
	long long max = (long long)ceil(sqrt(m));
	int maxIdx = primeList.size() - 1;

	if (primeList[maxIdx] > max) {
		maxIdx = BinarySearch(max, primeList);
	}

	for (int j = 1; j <= maxIdx; j++) {
		if (m % primeList[j] == 0) {
			return false;
		}
	}

	return true;
}

long long findPrimeBelow(long long n)
{
	if (n > primeList.back()) {
		// search the maxKnownPrimeIdx+1 to nth prime
		long long start = primeList.back() + 2;

		do {
			if (IsPrime(start)) {
				primeList.push_back(start);
			}
			start += 2;
		} while (n > primeList.back());
	}

	long long sum = 0;
	int i = 1;
	while (primeList[i] <= n) {
		sum += primeList[i];
		i++;
	}

	return sum;
}
/***********************************************************************
* Using quotion to check prime is too slow
***********************************************************************/

#define N_max 1000001
bool isNotPrime[N_max];
vector<long long> primeList2;
vector<long long> sumPrimeList;

void SieveOfEratosthenes() {
	isNotPrime[0] = 1;
	isNotPrime[1] = 1;
	primeList2.push_back(1);
	sumPrimeList.push_back(0);

	for (int i = 0; i < N_max; i++) {
		if (!isNotPrime[i]) {
			primeList2.push_back(i);
			sumPrimeList.push_back(sumPrimeList.back() + i);

			int j = i + i;
			while (j < N_max) {
				isNotPrime[j] = 1;
				j += i;
			}
		}
	}
}


long long findPrimeBelow2(long long n)
{
	int idx = BinarySearch(n, primeList2);
	return sumPrimeList[idx-1];
}



int main() {
	primeList.push_back(1);
	primeList.push_back(2);
	primeList.push_back(3);

	SieveOfEratosthenes();
	int t;
	cin >> t;
	for (int a0 = 0; a0 < t; a0++) {
		int n;
		cin >> n;
		cout << findPrimeBelow2(n) << endl;
	}
	return 0;
}