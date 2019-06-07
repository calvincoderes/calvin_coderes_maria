var x = -4
var num1 = 1
var num2 = 0
// if number is NOT multiples of 3 and 5, and positive integer
if(x % 3 && x % 5 && x > 0) {
  // output the starting sequence as constant
  console.log(num2)
  for (var i = 1; i <= x; i++) {
    var nxt = num1 + num2
    num1 = num2
    num2 = nxt
    console.log(nxt)
  }
} else {
  if(x % 3 == 0 && x % 5 == 0) { // if number is multiples of 3 and 5,
    console.log('Maria Health')
  } else if (x % 3 == 0) { // if number is multiples of 3
    console.log('Maria')
  } else if (x % 5 == 0) { // if number is multiples of 5,
    console.log('Health')
  }
}