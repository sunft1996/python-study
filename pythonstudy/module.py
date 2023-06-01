export_var_1 = 1

class PublicClass:
    def __init__(self):
        print("This is a public class.")

def _private_function():
    print("This is a private function.")
    
class _PrivateClass:
    def __init__(self):
        print("This is a private class.")

# 定义了all，外部导入时只能用这些变量
__all__ = [
    'export_var_1',
    'PublicClass',
]