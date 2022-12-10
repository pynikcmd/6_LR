#!/usr/bin/env python3
# -*- coding:utf-8 -*-

if __name__ == '__main__':
    word_1 = input('Введите первое слово: ')
    word_2 = input('Введите второе слово: ')
    word_3 = input('Введите третье слово: ')

    symbols = ''
    for i in word_1:
        for j in word_2:
            for g in word_3:
                if i == j == g and word_1.count(i) == 1 and word_2.count(j) == 1 and word_3.count(g) == 1:
                    symbols += i
    print("Общие буквы: ", symbols)
