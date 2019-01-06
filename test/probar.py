import time


l = 50
start = time.perf_counter()
print('开始执行'.center(l//2,'-'))
for i in range(l+1):
    a = '*'*i
    b = '.'*(l-i)
    c = i/l*100
    print('\r{:3.0f}%{}->{}{:3.2f}'.format(c, a, b, time.perf_counter()-start), end='')
    time.sleep(0.1)
print("\n"+"打印结束".center(l//2, '-'))