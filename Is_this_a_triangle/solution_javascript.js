function isTriangle(a,b,c) {
  // Triangle inequality theorem
   if ((a + b) > c && (b + c) > a && (a + c) > b) {
     return true;
   } else {
     return false;
   }
}
