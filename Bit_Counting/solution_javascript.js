var countBits = function(n) {
  var result = 0;
  do {
    result += n & 1;
    n >>= 1;
  } while(n > 0);
  return result;
};
