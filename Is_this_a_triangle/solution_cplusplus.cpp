namespace Triangle {
  bool isTriangle(long a, long b, long c) {
    return ((a + b) > c && (b + c) > a && (a + c) > b) ? true : false;
  }
};
