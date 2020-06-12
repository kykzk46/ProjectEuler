#include <sstream>
#include <iostream>

using namespace std;

long long AbsoluteSumGeneral(long long  n){
	long long sum = 0;
	for (int j = 1; j <= n; j++) {
		for (int i = 1; i < j; i++) {
			sum += i * j;
		}
	}
	return 2 * sum;
}

long long AbsoluteSum(long long n) {

	long long s1 = n*(n + 1)*n*(n + 1) / 4;
	long long  s2 = n*(n + 1)*(2 * n + 1) / 6;
	return  s1 - s2;
}

int main(){
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        int n;
        cin >> n;
		cout << AbsoluteSum(n) << endl;
    }
    return 0;
}
