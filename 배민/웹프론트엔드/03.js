function solution(reqs) {
  answer = []
  var accountDict = {}
  for (let i = 0; i < reqs.length; i++) {
    let request = reqs[i].split(' ')
    let cmd = request[0];
    let account = request[1];
    let money = request[2];
    if (cmd == 'CREATE') { // 계좌 개설
      console.log('개설')
        if (accountDict[account] == undefined) {
          accountDict[account] = money
          answer.push(200)  
        } else { // 이미 있는 계좌라면
          answer.push(403)
        }
    } else if (cmd == 'DEPOSIT') { // 입금
      console.log('입금')
        if (accountDict[account] == undefined) {
          answer.push(404)
        } else {
          accountDict[account] += money
        }
    } else { // 출금
      console.log('출금')
      if (accountDict[account] == undefined) {
        answer.push(404)
      } else {
        var balance = accountDict[account]
        if (money > balance) {
          answer.push(403)
        } else {
          accountDict[account] -= money
          answer.push(200)
        }
      }
    }
  }
  return answer;
}

// console.log(solution(["DEPOSIT 3a 10000", "CREATE 3a 300000", "WITHDRAW 3a 150000", "WITHDRAW 3a 150001"]))
console.log(solution(["CREATE 3a 10000", "CREATE 3a 20000", "CREATE 2bw 30000"]))
// ac = {

// }

// console.log(ac['ss'])