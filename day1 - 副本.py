#1 利用动态数组解决数据存放问题
"""编写一段代码，要求输入一个整数N，用动态数组A来存放2~N之间所有5或7的倍数，输出该数组。"""
def f1(n):
    if n<5:
        return []
    res=[]
    for i in range(5,n+1):
        if i%5==0 or i%7==0:
            res.append(i)
    return res
test=100
a=f1(test)
print(a)

#2. 托普利茨矩阵问题
"""如果一个矩阵的每一方向由左上到右下的对角线上具有相同元素，那么这个矩阵是托普利茨矩阵。
给定一个M x N的矩阵，当且仅当它是托普利茨矩阵时返回True。
eg
输入:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]

输出: True"""
def f2(mn):
    m=len(mn)
    n=len(mn[0])
    for i in range(m):
        for j in range(n):
            if i+1<m and j+1<n:
                if mn[i+1][j+1]!=mn[i][j]:
                    return False
    return True
test2=[
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
test3=[[1,2,4,4],
  [5,1,2,3],
  [9,5,1,2]]
print(f2(test2))
print(f2(test3))

#3.三数之和
"""
给定一个包含 n 个整数的数组nums，判断nums中是否存在三个元素a，b，c，使得a + b + c = 0？找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
def f3(nums):
    res=[]
    if len(nums)<3:
        return []
    nums.sort()
    l=0
    for i in range(len(nums)):
        if nums[i]>0:
            return res
        if nums[i]==0 or nums[i]>nums[i-1]:
            l=i+1
            r=len(nums)-1
            while r>l:
                if nums[i]+nums[l]+nums[r]==0:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l+1]==nums[l]:
                        l+=1
                    while l<r and nums[r-1]==nums[r]:
                        r-=1
                    l+=1
                    r-=1
                elif nums[i]+nums[l]+nums[r]<0:
                    l+=1
                else:
                    r-=1
    return res
nums = [-1, 0, 1, 2, -1, -4]
print(f3(nums))

"""
特判，对于数组长度 n，如果数组为 null 或者数组长度小于 3，返回 []。
对数组进行排序。
遍历排序后数组：

若 nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于 0，直接返回结果。
对于重复元素：跳过，避免出现重复解
令左指针 L=i+1，右指针 R=n−1，当 L<R 时，执行循环：

当 nums[i]+nums[L]+nums[R]==0，执行循环，判断左界和右界是否和下一位置重复，去除重复解。并同时将 L,R 移到下一位置，寻找新的解
若和大于 0，说明 nums[R] 太大，R 左移
若和小于 0，说明 nums[L] 太小，L 右移

"""