import pytest


def mark_param_list(params: list,
                    mark_skip: list = [None],
                    mark_xfail: list = [None]):
    """
    Marks parameters in a list with pytest markers
    based on provided skip and xfail lists.
    """
    
    marked_param_list = [
        pytest.param(i, marks=pytest.mark.xfail) if i in mark_xfail
        else pytest.param(i, marks=pytest.mark.skip) if i in mark_skip
        else i
        for i in params
        ]
    
    return marked_param_list