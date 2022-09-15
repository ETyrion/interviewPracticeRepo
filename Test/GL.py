import self as self


class Solution:
    def get_pairs_count(self, arr, n, k):
        count =0
        res=[]
        while arr:
            num = arr.pop()
            num_to_find = k - num
            if num_to_find in arr:
                count = count+1

        return count

    arr = [1,2,4,5,3,2,4,6]
    n = 8
    k = 7

    total_pairs = get_pairs_count(self, arr, n, k)
    print(total_pairs)


