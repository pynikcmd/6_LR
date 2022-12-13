#!/usr/bin/env python3
# -*- coding:utf-8 -*-

if __name__ == '__main__':
    print("Верно ли, что в тексте идут подряд 5 одинаковых символов")
    text = input('Введите текст: ')
    s = text.replace(' ', '')
    count = 1
    end_index = 0
    pred = ''
    flag = False

    for i in s:
        if i == pred:
            pred = i
            count += 1
            if count == 5:
                print("Да, верно")
                flag = True
        if i != pred:
            pred = i
            count = 1
        if flag:
            break

    if not flag:
        print("Не верно")
