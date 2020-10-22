#include <cmath>

bool narcissistic( int value )
{
  int base = value;
  int result = 0, numberOfDigits = int(log10(value) + 1);

  while (value)
  {
    result += pow(value % 10, numberOfDigits);
    value /= 10;
  }
  
  return (result == base) ? true : false;
}