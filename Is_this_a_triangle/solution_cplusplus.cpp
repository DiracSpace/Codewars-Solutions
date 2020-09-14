namespace Triangle {
  bool isTriangle(int aa, int bb, int cc) {
    long a = (long) aa;
    long b = (long) bb;
    long c = (long) cc;
    return ((a + b) > c && (b + c) > a && (a + c) > b) ? true : false;
  }
};
