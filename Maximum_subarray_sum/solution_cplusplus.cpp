#include <vector>

using namespace std;

int maxSequence(const vector<int>& arr) {
  int sum = 0;
  if (arr.empty()) { return 0; } // return empty array
  int all_positive = count_if(arr.begin(), arr.end(), [](int a) {
    return (a > 0); // count the positives
  });
  if (arr.size() == static_cast<std::vector<int>::size_type>(all_positive)) {
    // if size is equal, then return sum of all positives
    for (int i : arr) {
      sum += i;
    }
  } else {
    // kadanes algorithm
    int max_now = 0, max_total = 0;
    for (int i : arr) {
      max_now += i;
      if (max_now < 0) {
        max_now = 0;
      }
      if (max_total < max_now) {
        max_total = max(max_total, max_now);
      }
    }
    return max_total;
  }
  return sum;
}
