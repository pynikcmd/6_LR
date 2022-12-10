#!/usr/bin/env python3
# -*- coding:utf-8 -*-

if __name__ == '__main__':
    text = input('Введите текст: ')
    s = text.split(".")
    count = 0
    flag = True

    for i, word in enumerate(s):
        count = word.count('и')
        if word.count('и') == 0:
            print("В тексте нет букв и")
        else:
            print("Количество и:", count)
