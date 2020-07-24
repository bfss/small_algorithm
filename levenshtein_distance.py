"""
计算两个字符串的最小编辑距离,也叫Levenshtein distance
本质是动态规划DP table
参考资料：https://leetcode-cn.com/problems/edit-distance/solution/bian-ji-ju-chi-by-leetcode-solution/
"""
def levenshtein_distance(input_str='bfss', target_str='ssbf'):
    m, n = len(input_str) + 1, len(target_str) + 1
    if m == 0:
        return n
    if n == 0:
        return m
    # m行n列
    # 下面这种方式是浅复制，有问题
    """
    matrix0 = [[0]*n]*m
    print(matrix0[0].__repr__)
    print(matrix0[1].__repr__)
    """
    matrix = [[0 for i in range(0, n)] for j in range(0, m)]
    for i in range(0, m):
        matrix[i][0] = i
    for j in range(0, n):
        matrix[0][j] = j

    for i in range(0, m):
        for j in range(0, n):
            if i != 0 and j != 0:
                if input_str[i-1] == target_str[j-1]:
                    t = 0
                else:
                    t = 1
                temp_min = min(matrix[i - 1][j] +1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + t) 
                matrix[i][j] =  temp_min

    print(matrix)
    print(matrix[m-1][n-1])

if __name__ == '__main__':
    levenshtein_distance()