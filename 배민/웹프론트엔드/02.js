function solution(arr) {
  answer = 0
  const numberSet = new Set();
  for (let i = 0; i < arr.length; i++) {
    var string = new String(arr[i])
    // var convertString = string.split('').sort().join('')
    console.log(string.sort())
    // if (!numberSet.has(convertString)) {
    //   numberSet.add(convertString)
    //   answer++;
    // }
    
  }
  return answer;
}

console.log(solution([112, 1814, 121, 1481, 1184]))
// console.log(solution([123, 456, 789, 321, 654, 987]))
// console.log(solution([1, 2, 3, 1, 2, 3, 4]))
// console.log(solution([123, 234, 213, 432, 234, 1234, 2341, 12345, 324]))