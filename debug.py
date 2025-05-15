def my_retry(func):
    def inner(*args,**kwargs):
        for i in range(5):
            func(*args,**kwargs)
        return inner

@my_retry
def test():
    print('123')
test()