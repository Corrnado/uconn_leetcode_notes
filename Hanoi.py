# Simple problem of dynamic programming: "The tower of Hanoi"
def hano(n):
    # solve(5, 0, 1)
    def solve(k, a ,b):
        if k == 1:
            print('%d -> %d' % (a,b))
            return 
        c = 3-a-b
        solve(k-1, a, c)
        print('%d -> %d' % (a, b))
        solve(k-1, c, b)
    solve(n, 0, 2)

if __name__ == 'main':
	hano(5)