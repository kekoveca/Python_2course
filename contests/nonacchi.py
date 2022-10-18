def nonn(n):
    nums = [0]*8 + [1]
    if n in range(1,10):
        return(nums[n - 1])
    for i in range(9, n):
        s = sum(nums)
        nums.append(s)
        nums.pop(0)
    return(nums[-1])

print(nonn(int(input())))