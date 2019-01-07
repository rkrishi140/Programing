"""
Provides common supporting modules to all programs.

"""
import time
import functools
from Programing.Sorting_Module.sortinglog import my_logger


def toMeasureExecutionTime(func):
    """
    This is a decorator function that takes original function as an argument.
    Args:
        param1 (function_type):  Original function which is to be decorated

    Returns:
    function_type: Returns wrapper function i.e on hold
    """
    """ This wraps the metadata of the original function"""

    @functools.wraps(func)
    def wrapperOf_toMeasureExecutionTime_decorator(*args, **kwargs):
        """
        This is wrapping function that wrap up the task of to be decorated function.
        Args:
            param1 (args): no. of argument of the original function to be decorated
            param2 (kwargs): argument of the original function to be decorated.
        Returns:
        return_type_of_original_function: result of the original function

        """
        """ Execution time of this sorting is very fast i.e difference of time.time() is tends to zero. To get the
            significant figure using timer """
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        my_logger.info(func.__name__ + " is taking " + str((end - start) * 1000) + " mil seconds" + " and output list "
                                                                                                    "is {}".format(
            res))
        print(func.__name__ + " is taking " + str((end - start) * 1000) + " mil seconds" + " and output list "
                                                                                           "is {}".format(
            res))
        return res

    return wrapperOf_toMeasureExecutionTime_decorator
