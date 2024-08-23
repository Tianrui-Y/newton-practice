x_0 = 1.0 #starting value
epsilon = 0.01 # used for calculating derivatives
stopping = 0.01 # stopping criteria for newton algorithm
func = lambda x: (x-2) ** 2
def diff(f,x,eps=epsilon):
    return (f(x+eps) - f(x)) / eps
def diff2(f,x,eps=epsilon):
    return (diff(f,x+eps,eps) - diff(f,x,eps)) / eps
def optimize(x0=x_0,f=func,eps=stopping):
    xt = x0
    while True:
        d = diff(f,xt) / diff2(f,xt)
        if abs(d) <= eps:
            break
        else:
            xt = xt - d
    print('Optimizing result is', xt,'.')