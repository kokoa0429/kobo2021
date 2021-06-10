import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    y = np.sum(w*x) + b
    #あとは自分で    

def NAND(x1, x2):

def OR(x1, x2):

def XOR(x1, x2): 

if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        out = AND(xs[0], xs[1])
        print(str(xs) + " -> " + str(out))
