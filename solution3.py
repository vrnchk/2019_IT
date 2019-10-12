import numpy as np

def isInt(n):
    return int(n) == float(n)

def get_indices(N, n_batches, split_ratio):
    inds = np.array([0, 0, 0])
    tmp = 0
    for i in range(n_batches):
        inds[0] = tmp
        for i1 in range(tmp+1, N-1):
            inds[1] = i1
            inds[2] = split_ratio*(inds[1] - inds[0]) + inds[1]
            if isInt(inds[2]):
                tmp = N - 1 - inds[2]
                tmp = tmp / (n_batches - 1)
                if isInt(tmp):
                    break
        yield inds

def main():
    for inds in get_indices(100, 5, 0.25):
        print(inds)
    # expected result:
    # [0, 44, 55]
    # [11, 55, 66]
    # [22, 66, 77]
    # [33, 77, 88]
    # [44, 88, 99]

if __name__ == "__main__":
    main()