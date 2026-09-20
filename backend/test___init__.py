import pytest
import __init__

def test_module_smoke():
    assert hasattr(__init__, '__name__')
