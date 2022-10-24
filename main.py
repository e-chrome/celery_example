import time

from tasks import hard_function


def main():
    async_result_1 = hard_function.apply_async(args=[1, 2])
    async_result_2 = hard_function.apply_async(args=[2, 2])
    async_result_3 = hard_function.apply_async(args=[3, 2])
    async_result_4 = hard_function.apply_async(args=[4, 2])
    async_result_5 = hard_function.apply_async(args=[5, 2])

    result_1 = async_result_1.get()
    result_2 = async_result_2.get()
    result_3 = async_result_3.get()
    result_4 = async_result_4.get()
    result_5 = async_result_5.get()
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)
    print(result_5)


if __name__ == '__main__':
    start = time.time()
    print(start)
    main()
    print(time.time() - start)


