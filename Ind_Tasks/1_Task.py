#!/usr/bin/env python3
# -*- coding:utf-8 -*-

if __name__ == '__main__':
    print("Верно ли, что в тексте идут подряд 5 одинаковых символов")
    text = input('Введите текст: ')
    s = text.replace(' ', '')
    count = 1
    end_index = 0
    pred = ''

    for i, word in enumerate(s):
        if s[i] == pred:
            pred = s[i]
            count += 1
            if count == 5:
                print("Да, верно")
                break
        if s[i] != pred:
            pred = s[i]
            count = 1
        end_index = i
    if (end_index+1) == len(s):
        print("Не верно")
