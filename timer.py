import timeit

from book import section_1


def time_comparison(func_one, func_two, func_inputs):
    def func_one_timer():
        func_one(**func_inputs)

    def func_two_timer():
        func_two(**func_inputs)

    print(func_one.__name__, timeit.timeit(stmt=func_one_timer, number=10000))
    print(func_two.__name__, timeit.timeit(stmt=func_two_timer, number=10000))


time_comparison(
    func_one=section_1.palindrome_permutation_no_itertools,
    func_two=section_1.palindrome_permutation,
    func_inputs={"input_string": "Foo Foo Bob"},
)
