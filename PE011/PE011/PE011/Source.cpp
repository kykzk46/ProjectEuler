#include <iostream>
#include <queue>
#include <algorithm>
#include <fstream>

using namespace std;

// The main algorithm is same as PE008
long long foo(int n, int k, vector<int> array) {
  long long p = 1;
  long long p_max = 0;
  queue<char> tobeRemoved;

  for (size_t i = 0; i < n; i++) {
    int num = array[i];
    if (num != 0) {
      p *= num;
      tobeRemoved.push(num);

      if (tobeRemoved.size() > k) {
        p /= tobeRemoved.front();
        tobeRemoved.pop();
      }

      if (tobeRemoved.size() == k) {
        if (p > p_max)
          p_max = p;
      }
    }
    else {
      p = 1;
      queue<char>().swap(tobeRemoved);
    }
  }

  return p_max;
}

int main() {
  vector<int>updown(420);
  vector<int>leftright(420);
  vector<int>upleftrightdown(440);
  vector<int>uprightleftdown(440);

  ifstream myfile("input00.txt");
  if (!myfile.is_open())
    return 0;


  for (int i = 0; i < 20; i++) {
    for (int j = 0; j < 20; j++) {
      int num;
      //cin >> num;
      myfile >> num;
      cout << num << " ";

      leftright[i * 21 + j] = num;
      updown[j * 21 + i] = num;

      int s1 = i + j;

      if (s1 < 20)
      {
        s1 = (s1 + 2 + 2) * (s1 + 2 - 2 + 1) / 2;
        s1 = s1 - 1 - (j + 1);// to idx
      }
      else
      {
        s1 = 38 - s1;
        s1 = (s1 + 2 + 2) * (s1 + 2 - 2 + 1) / 2;
        s1 = 230 + (s1 - 1 - (19 - j + 1));
      }
      uprightleftdown[s1] = num;


      int jj = (19 - j);
      int s2 = jj + i;
      if (s2 < 20)
      {
        s2 = (s2 + 2 + 2) * (s2 + 2 - 2 + 1) / 2;
        s2 = s2 - 1 - (jj + 1);// to idx
      }
      else
      {
        s2 = 38 - s2;
        s2 = (s2 + 2 + 2) * (s2 + 2 - 2 + 1) / 2;
        s2 = 230 + (s2 - 1 - (19 - jj + 1));
      }
      upleftrightdown[s2] = num;
    }
  }

  int p1 = foo(420, 4, leftright);
  int p2 = foo(420, 4, updown);
  int p3 = foo(420, 4, upleftrightdown);
  int p4 = foo(420, 4, uprightleftdown);

  cout << max(p1, max(p2, max(p3, p4))) << endl;
  return 0;
}