function isPrime(num) {
  var i = 2;
  var set = new Set();
  while (num != 1) {
    if (num % i === 0) {
      num = num / i;
      if (set.has(i)) {
        return false;
      } else {
        set.add(i);
      }
    } else {
      i++;
    }
  }
  return true
}

console.log(isPrime(4))