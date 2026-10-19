nums = [2,1, 1, 4, 4, 4]
dic = {}
k = 2
for num in nums:
    dic[num] = 1 + dic.get(num, 0)

ordemNums = [[] for i in range(len(nums) + 1)]
print(ordemNums)
for key, value in dic.items():
    ordemNums[value].append(key)
print(ordemNums)

res = []
for i in range(len(ordemNums) - 1, 0, -1): 
    if len(res) == k:
        print(res)
    elif ordemNums[i] != 0:
        print('a', i)
        res.append(ordemNums[i])

