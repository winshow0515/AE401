# -*- coding: utf-8 -*-


string1="我在外層"

def func():
    string1="我在內層"
    print(string1)

print(string1)
func()
print(string1)
