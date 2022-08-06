# последовательность в которой первые два числа равны 0 и 1,
# а каждое последующее число равно сумме двух предыдущих чисел.

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


print(recur_fibo(10))  # 55
