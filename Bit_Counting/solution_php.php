<?php
  function countBits($n) {
    // php bitwise operator for
    // javascripts assignment operator
    $result = '';
    do {
      $result += $n & 1;
      $n >>= 1;
    } while($n > 0);
    return $result;
  }
?>
