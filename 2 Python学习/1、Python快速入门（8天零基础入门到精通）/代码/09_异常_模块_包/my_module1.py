
__all__ = [
    'test_a'
]


def test_a(a, b):
    print(a + b)

def test_b(a, b):
    print(a - b)


# 内部测试执行，外部导入不执行
if __name__ == '__main__':
    test(2, 4)