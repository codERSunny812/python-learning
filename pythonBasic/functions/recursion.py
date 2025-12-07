def fun(n):

    if n <= 0:
        print("Recursion ends")
        return
    else:
        print("Recursion at n =", n)
        fun(n - 1)


fun(5)