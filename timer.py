import timeit

from book import section_1


def time_comparison(func_one, func_one_inputs, func_two, func_two_inputs):
    def func_one_timer():
        func_one(**func_one_inputs)

    def func_two_timer():
        func_two(**func_two_inputs)

    print(func_one.__name__, timeit.timeit(stmt=func_one_timer, number=10000))
    print(func_two.__name__, timeit.timeit(stmt=func_two_timer, number=10000))


func_inputs = {"one": "abcdefg", "two": "abcdefgh"}
time_comparison(
    func_one=section_1.check_permutation,
    func_one_inputs=func_inputs,
    func_two=section_1.check_permutation_no_libs,
    func_two_inputs=func_inputs,
)
