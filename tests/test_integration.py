from calculator.basic_operations import add
from calculator.advanced_operations import sine

def test_combined_operation():
    result = add(2, sine(0))
    assert result == 2
