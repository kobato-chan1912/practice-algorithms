def digitsProduct(product):
    def kt(arr):
        kq=1
        for i in arr:
            kq*=i
        return kq
    ls=[kt([int(v) for v in str(i)]) for i in range(1,4557)]
    for i in ls:
        if i==product:
            return [i for i in range(1,4557)][ls.index(i)]
    return -1
