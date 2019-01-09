"""
Provides common supporting modules to all programs.
This modules will help to measure the time performance of all the programs or modules or function.
It is a standard decorator which can be used for any function irrespective of the function argument.
"""

from functools import wraps
import time


def func_execution_time(func):
    """
    This decorator returns the execution time of a function.

    Args:
        func (func_type): The function name to be decorated.

    Return:
        func_type : Returns wrapper_func_execution
    """
    @wraps(func)  # It preserves attributes of function i.e. function name and docstring  on the returned function.
    def wrapper_func_execution(*args, **kw):
        """
        Wrapping function

        Args:
            args (int): No of argument to be decorated.
            kw (argument_type): Argument to be decorated.

        Return:
            return_type_of_original_function:Result
        """
        start_time = time.perf_counter_ns()
        result = func(*args, **kw)
        end_time = time.perf_counter_ns()

        print('%r  is taking %2.2f nano Second' % (func.__name__, (end_time - start_time)))
        return result
    return wrapper_func_execution
