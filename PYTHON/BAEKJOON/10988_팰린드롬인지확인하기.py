word = input()
left, right = (len(word)//2)-1, len(word)//2
if len(word) % 2 == 1:
    right+=1

res = 1
while left >= 0:
    if word[left] != word[right]:
        res = 0
        break
    left -= 1
    right += 1

print(res)
