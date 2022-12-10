#!/usr/bin/env python3
# -*- coding:utf-8 -*-

if __name__ == '__main__':
    text = input('Введите текст: ')
    s = text.strip()

    maxi = -1
    index = -1

    for val in s:
        if val.isdigit():
            if int(val) > maxi:
                maxi = int(val)
                index = s.index(val)

    if maxi == -1 and index == -1:
        print("В строке нет цифр")
    else:
        print(f"Max: {maxi}, index: {index}")
