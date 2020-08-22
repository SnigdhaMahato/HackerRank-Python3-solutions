def bitwise_and(n, k):
    maxab = 0
    for b in range(1, n+1):
        for a in range(1, b):
            p = a & b
            if k > p > maxab:
                maxab = p
                if (maxab == (k-1)):
                    return maxab          
    return maxab

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        nk = str(input()).split()
        n = int(nk[0])
        k = int(nk[1])
        print(bitwise_and(n, k))
