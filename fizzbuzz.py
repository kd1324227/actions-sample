
def fizzbuzz(n: int) -> str:
    """いわゆるFizzBuzz問題を解きます

    引数で渡された値に対し、以下のような文字列を返します。

    - nが3の倍数のときは"Fizz"
    - nが5の倍数のときは"Buzz"
    - nが3の倍数かつ5の倍数のときは"FizzBuzz"
    - それ以外のときはnをそのまま返します。

    >>> fizzbuzz(1)
    '1'

    >>> fizzbuzz(3)
    'Fizz'

    >>> fizzbuzz(5)
    'Buzz'

    >>> fizzbuzz(15)
    'FizzBuzz'
    """

    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    if n % 3 == 0:
        return 'Fizz'
    if n % 5 == 0:
        return 'Buzz'
    return str(n)

def runtest():
    print("テストを実施します")
    import doctest
    doctest.testmod()
    result = doctest.testmod()
    if result.failed == 0:
        print("すべてのテストに合格しました")
    else:
        print(f"{result.failed}個のテストに失敗しました")
        import sys
        sys.exit(1)



if __name__ == "__main__":
    runtest()
