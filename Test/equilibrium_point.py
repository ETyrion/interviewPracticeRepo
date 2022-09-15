class Solution:
    # Complete this function

    # Function to find equilibrium point in the array.
    def equilibriumPoint(self, A, N):
        # Your code here
        #arr_sum = sum(A)
        if N == 1:
            return N
        else:
            for i in range(N):
                l_sum = sum(A[:i+1])
                r_sum = sum(A[i:])
                if (r_sum == l_sum):
                    return i+1

s = Solution()
list1 = [1,3,5,2,2]
print(s.equilibriumPoint(list1, 5))