#include <iostream>
#include <algorithm>

using namespace std;

int foo(int n) {
  // Find min and max of one side
  int min = 1; // obviously
  int max = (int)(n / (2 + sqrt(2))); // when two side equal

  int p_max = -1;
  for (int a = min; a <= max; a++) {
    // We known a and n now. Using:
    // 1) b = (N-a) - c
    // 2) c = sqrt(a*a+b*b)
    // ==> b = n * (n - 2 * a) / (2 * n - 2 * a)
    int b = n * (n - 2 * a) / (2 * n - 2 * a);
    int c = n - a - b;
    if (a * a + b * b == c * c) {
      int p = c * b * a;
      if (p > p_max) {
        p_max = p;
      }
    }
  }
  return p_max;
}


int main() {
  int t=1;
  //cin >> t;
  for (int a0 = 0; a0 < t; a0++) {
    int n = 12;
    //cin >> n;

    cout << foo(n) << endl;
  }
  return 0;
}