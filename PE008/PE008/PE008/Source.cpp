#include <iostream>
#include <queue>

using namespace std;

int foo(int n, int k, string num) {
  int p = 1;
  int p_max = 0;
  queue<char> tobeRemoved;

  for (size_t i = 0; i < n; i++) {
    char c = num[i];
    if (c != '0') {
      char c_num = c - 48;
      p *= c_num;
      tobeRemoved.push(c_num);

      if (tobeRemoved.size() > k) {
        p /= tobeRemoved.front();
        tobeRemoved.pop();
      }

      if (tobeRemoved.size() == k) {
        if (p > p_max)
          p_max = p;
      }
    }else{
      p = 1;
      queue<char>().swap(tobeRemoved);
    }
  }

  return p_max;
}


int main() {
  int t = 1;
  //cin >> t;
  for (int a0 = 0; a0 < t; a0++) {
    int n = 10;
    int k = 5;
    //cin >> n >> k;
    string num = "3675356291";
    //cin >> num;

    cout << foo(n, k, num) << endl;
  }
  return 0;
}