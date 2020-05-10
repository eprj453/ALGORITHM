function solution(arr) {

  var answer = -1;
  var numbers = arr
  while (true) {
    if (numbers.length === 1) {
      answer++;
      break
    }
    console.log(numbers)
    console.log(numbers.length)
    let temp = new Array()
    let num = 0;
    let seq = 0;
    for (let i = 0; i < numbers.length; i++) {
      let n = numbers[i];
      if (i == numbers.length-1) {
        if (num == n) {
          temp.push(++seq)
        } else {
          temp.push(seq)
          temp.push(1)

        }
        break;
      }
      else if (num == 0) {
        num = n;
        seq++;
      } else if (num == n) {
        seq++;
      } else {
        temp.push(seq)
        seq = 1;
        num = n;
      }
    }
    answer++;
    numbers = temp;
  }
  return ++answer;
}

// console.log(solution([1,1,3,3,2,2,4,5,1,1,1,3,3,3])) // 6
// console.log(solution([1,2,3])) // 3
// console.log(solution([2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 2] )) // 5
console.log(solution([2])) // 1

