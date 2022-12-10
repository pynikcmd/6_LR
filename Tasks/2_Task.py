#!/usr/bin/env puthon3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    word = input('введите слово: ')

    idx = len(word) // 2
    if len(word) % 2 == 1:
        # длина слова нечетная
        r = word[:idx]+word[idx+1:]
    else:
        # длина слова четная
        r = word[:idx-1]+word[idx+1:]

    print(r)
