<?php
$x = 15;
$num1 = 1;
$num2 = 0;
// if number is NOT multiples of 3 and 5, and a positive integer
if($x % 3 && $x % 5 && $x > 0) {
  // output 0 as start of sequence
  echo '0 ';
  for ($i = 1; $i <= $x; $i++) {
    $nxt = $num1 + $num2;
    $num1 = $num2;
    $num2 = $nxt;
    echo $nxt . "\n";
  }
} else {
  if($x % 3 == 0 && $x % 5 == 0) { // if number is multiples of 3 and 5,
    echo "Maria Health";
  } else if($x % 3 == 0) { // if number is multiples of 3
    echo "Maria";
  } else if($x % 5 == 0) { // if number is multiples of 5,
    echo "Health";
  }
}