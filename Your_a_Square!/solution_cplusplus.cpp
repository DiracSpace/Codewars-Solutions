#include <cmath>

bool is_square(int n)
{
  return (remainder(sqrt(n), 1) == 0) ? true : false;
}