from numpy import matrix


#Time complexity: O(2^n): 2 to the power n
#Space complexity: O(n): Based on how much memory is used
def fibi(num, depth):
    print("depth: ", depth)
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibi(num-2, depth+1) + fibi(num-1, depth + 1)



# time: O(n)
# space: O(n)
def fibi_1(num):
    arr = [0]*(num+1)
    arr[0] = 0
    arr[1] = 1
    for ind in range(2,num+1):
        arr[ind] = arr[ind-1] + arr[ind-2]
    return arr[-1]

# time: O(n)
# space: O(1)
def fibi_2(num):
    first = 0
    second = 1
    third = 0
    for ind in range(2,num+1):
        third = first + second
        first = second
        second = third
    return third


# time:  O(log₂N)
# space: O(1)
def MatrixPower(mat, n):
  res = None
  temp = mat
  while True:
    if n & 1:
      if res is None: 
        res = temp
      else: 
        res = res * temp
    n >>= 1
    if n == 0: break
    temp = temp * temp
  return res

def FastFibonacci(n):
  
  if n < 2: 
    return n  # F(0) = 0, F(1) = 1
  mat = matrix([[1, 1], [1, 0]], dtype=object)
  mat = MatrixPower(mat, n - 1)
  tmp = mat[0, 1]
  return mat[0, 0]


# this is the template for MatrixPower
# https://stackoverflow.com/questions/38922606/what-is-x-1-and-x-1
def pow3(base,exponent):
    ans = 1
    while(exponent!=0):
        if (exponent&1): # the last bit is 1
            ans *= base
        base *= base
        exponent>>=1 # #右移动一位就是除以2
    return ans

if __name__ == "__main__":
    pow3(2,3)
    ret = fibi(5,1)
    ret = fibi_1(5)
    ret1 = FastFibonacci(5)
    print(ret)