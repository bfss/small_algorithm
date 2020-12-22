# -*- coding: utf-8 -*-
"""
用比较笨的办法分解质因数
比如输入45，输出3，5，5
输入28， 输出2，2，7
如果输入的是个素数，返回None
"""
def is_prime(number):
    """判断一个数是不是素数"""
    for i in range(2, int(number/2)+1):
        if number % i == 0:
            return False
    return True


def decompose(number, result_list):
    """使用递归的方式分解"""
    if is_prime(number):
        # 递归的终止条件：最后一个因数是素数
        result_list.append(number)
        return
    else:
        for i in range(2, int(number/2)+1):
            if number % i == 0:
                if is_prime(i):
                    result_list.append(i)
                    decompose(int(number/i), result_list)
                # 每次只取第一个遇见的素数因数，然后停止循环，避免重复输出
                break
    
    return result_list


if __name__ == '__main__':
    print(decompose(35, []))
    print(decompose(28, []))
    print(decompose(19, []))