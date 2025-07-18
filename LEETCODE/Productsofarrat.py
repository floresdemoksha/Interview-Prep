
nums = [1, 2, 3, 4]
pref = [1]
aux = [1]
k, l = 1, 1
for i in range(1, len(nums)):
    k = nums[i-1]*k
    pref.append(k)
print(pref)
for j in range(len(nums), 1, -1):
    l = nums[j-1]*l
    aux.append(l)
print(aux)
aux.reverse()
suf = aux
print(suf)


res = [x*y for x, y in zip(suf, pref)]

print(res)
