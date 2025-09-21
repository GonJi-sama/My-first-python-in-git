class gong:
    def myfunc(a, b):
        length_a = len(a)

        for i in range(length_a):
            sum_val = a[i] + b[i]
            mul_val = a[i] * b[i]
            print(f"{i+1}.summation = {sum_val}\n  multiplication = {mul_val}")
        
        return 0