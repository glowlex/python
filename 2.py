#!/usr/bin/env python
from datetime import datetime
import functools, json

def log_duration(dec_func):
    @functools.wraps(dec_func)
    def end_func():
        start = datetime.now()
        data = dec_func()
        finish = datetime.now()
        print((finish-start).total_seconds())
        return data
    return end_func


@log_duration
def test1():
    i =0
    for x in range(0, 1000000):
        i+=1
    return i

def to_json(dec_func):
    @functools.wraps(dec_func)
    def end_func():
        data = dec_func()
        if isinstance(data, dict):
            return json.dumps(data)
        else:
            return data
    return end_func

@to_json
def test2():
    return {1:5, "a":4}


def ignore_exceptions(klas):
    #@functools.wraps(func)
    def end_func(func):
        def wrapped(arg):
            try:
                return func(arg)
            except klas:
                return None
        return wrapped
    return end_func


@ignore_exceptions(ZeroDivisionError)
def test3(arg):
    raise ZeroDivisionError
    #raise AttributeError
    return "succes"


class Cont:
    size = 0
    arr = []
    def __init__(self):
        pass

    def add(self, val):
        self.arr.append(val)
        self.size+=1

    def __setitem__(self, pos, val):
        if pos<=0 or pos>self.size:
            raise IndexError
        else:
            self.arr[pos-1] = val

    def __getitem__(self, pos):
        if pos<=0 or pos>self.size:
             raise IndexError
        else:
             return self.arr[pos-1]


def _main():
    print(test1())
    print(test2())
    print(test3("test3"))
    a = Cont()
    a.add(5)
    print(a[1])
    a.add(8)
    a[1]=22
    print(a[1])
    print(a[2])
    print(a[0])


if __name__ == "__main__":
    _main()
