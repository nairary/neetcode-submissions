class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        c_len = len(matrix)-1
        r_len = len(matrix[0])-1
        
        c_l = 0
        c_r = len(matrix)-1
        
        while (c_l < c_r-1):
            c_m = (c_l+c_r)>>1
            print(matrix[c_m][r_len])
            if (matrix[c_m][r_len] == target):
                return True
            if (matrix[c_m][r_len] < target):
                c_l = c_m
            elif (matrix[c_m][r_len] > target):
                c_r = c_m
        
        flatten = []
        for i in range(c_l, c_r+1):
            flatten.extend(matrix[i])

        r_l = 0
        r_r = len(flatten)-1

        print(c_l, c_r)
        print(flatten)
        while (r_l <= r_r):
            r_m = (r_l+r_r)>>1
            print(f"r_l: {r_l} r_r: {r_r} r_m: {r_m} value: {flatten[r_m]}")
            if (flatten[r_m] == target):
                return True
            elif (flatten[r_m] < target):
                r_l = r_m+1
            else:
                r_r = r_m-1
        return False