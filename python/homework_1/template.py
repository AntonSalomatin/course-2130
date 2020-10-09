"""
    Ваша задача дописать функции, чтобы они проходили все тесты

    Именование функций проиходит по шаблону: `t{number_of_task}`. Пожалуйста не меняйте эти имена.

    Разрешается использовать только стандартные библиотеки языка.
"""



def t1(number):
    """
    Поправьте код что бы возвращаемое значение было ближайшим сверху, кратным к 20

    Пример: number=21 тогда нужно вернуть 40
    Пример: -5 -> 0

    """

    pass

    return (number+19) // 20 *20




def t2(string):
    """
    На вход подается набор слов разделенных пробелом, инвертируйте каждое слово.

    Пример: `abc abc abc` -> `cba cba cba`
    """
    pass
    return ' '.join(string[::-1].split()[::-1])


def t3(dictionary):
    """
    На вход подается словарь. Преорбазуйте его в строку по следующему шаблону 'key: value; key: value' и так далее

    """
    return '; '.join(f'{k}: {v}' for k, v in dictionary.items())
    pass

def t4(string, sub_string):
    """
    проверить есть ли в строке инвертированная подстрока
    """
    return sub_string[::-1] in string
    pass

def t5(strings):
        """
        На вход подается список строк,
        Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
        """
        q = []
        for k in strings:
            x = k.split(" ")
            a = int(x[0])
            b = int(x[1])
            c = int(x[2])
            d = int(x[3])
            if d == a * b * c:
                q.append(k)
        return q
        pass


def t6(string):
    """
    Предположим у вас есть строки содержащие `#` символ, который означает backspace (удаление предыдущего) обработаете
        такие строки

    "abc#d##c"      ==>  "ac"
    "abc##d######"  ==>  ""
    "#######"       ==>  ""
    ""              ==>  ""
    """
    output = ''
    for fuck in string:
        if fuck != '#':
         output += fuck
        else:
             output = output[:-1]
    return output
pass

def t7(lst):
    """
    На вход подается список элементов, найдите сумму уникальных элементов списка.

    Например: [4,5,7,5,4,8] -> 15 потому что 7 и 8 уникальны
    """
    try:
        list = []
        t = 0
        for k in lst:
            list.append(int(k))
            t += int(k)
        a = 0
        for i in range(len(list)):
            if list.count(list[i]) > 1:
                a += int(list[i])
            else:
                pass
        return t - a
    except ValueError:
        return 0
    pass


def t8(string):
    """
    Найдите все последовательности числев в строке и среди них найдите максимальное число
    gh12cdy695m1 -> 695
    """
    x = string
    a = 0
    i = 0
    l = []
    while i < len(x):
        try:
            a = a * 10 + int(x[i])
        except ValueError:
            a = 0
            l.append(a)
        l.append(a)
        i += 1
    out = max(l)
    return out
    pass


def t9(number):
    """
    Приведите число number к пятизначному виду.

    Т.е. для числа 5 верните `00005`
    """
    pass
    if len(str(number)) < 5:
        s = 5 - len(str(number))
        return '0' * s + str(number)
    #elif len(str(number)) > 5:
       # s = len(str(number)) - 5
       # return number / 10 ** s
    else:
        return str(number)


def t10(string):
    """
    Произведите смешивание цветов. Вам будет дана строка, необходимо смешать все пары цветов и вернуть результируюший
        цвет

    Комбинации цветов:    G G     B G    R G   B R
    Результирующий цвет:   G       R      B     G

    R R G B R G B B  <- ввод
     R B R G B R B
      G G B R G G
       G R G B G
        B B R R
         B G R
          R B
           G  <-- вывод

    """


    def new_col(col1, col2):
        if col1 == col2:
            new = col1
        elif col1+col2 == 'BG' or col2+col1 == 'BG':
            new = 'R'
        elif col1+col2 == 'RG' or col2+col1 == 'RG':
            new = 'B'
        else:
            new = 'G'
        return new

    if len(string) != 1:
        new_cols = ''
        for i in range(len(string)-1):
            new_cols += new_col(string[i], string[i+1])
        return t10(new_cols)

    else:
        return string


def t11(lst):
    """
    Вам дам список из целых чисел. Найдите индекс числа такого, что левая и правая части списка от него равны
        Если такого элемента нет - верните -1. Если вы нашли два элемента -> верните тот, который левее.
    [1,2,3,5,3,2,1] = 3
    [1,12,3,3,6,3,1] = 2
    [10,20,30,40] = -1
    """


    for i in range(len(lst)):
        if sum(lst[:i]) == sum(lst[i+1:]):
            return i
    return int(-1)



def t12(lst):
    """
    На вход подается список строк вида `Что-то происходит бла бла бла +7495 123-45-67` содержащие номер телефона.
        Используя regex выражения запишите всевозможноые комбинации телефонов, например программа должна корректно
        работать с 790112345678 или 890112345678
    Вход: [`Что-то происходит бла бла бла +7495 123-45-67`]
    Выход: [`84951234567`]

    """
    import re
    s = {}
    for i in range(len(lst)):
        s[i] = re.findall(r'\d+', lst[i])
    r = list(s.values())
    t = {}
    o = ''
    for j in range(len(r)):
        for i in r[j]:
            o += i
            t[j] = o
        o = ''
    v = {}
    for m in range(len(list(t.values()))):
        if list(t.values())[m][0] == '7':
            v[m] = '8' + list(t.values())[m][1:]
        else:
            v[m] = list(t.values())[m]

    return list(v.values())
    pass


def t13(number_1, number_2):
    """
    Сложите два числа по элементно:
        248
       +208
        4416
    """
    pass

    s = ''
    while max(number_1, number_2) > 0:
        s = str(number_1 % 10 + number_2 % 10) + s
        number_1 = number_1 // 10
        number_2 = number_2 // 10
    if s != '':
        return int(s)
    return int(0)


def t14(string):
    """
    Преобразуйте математическое выражение (символьное) в буквенное выраэение

    Для операций используйте следующую таблицу
        { '+':   'Plus ',
          '-':   'Minus ',
          '*':   'Times ',
          '/':   'Divided By ',
          '**':  'To The Power Of ',
          '=':   'Equals ',
          '!=':  'Does Not Equal ' }
    Примеры:
        4 ** 9 -> Four To The Power Of Nine
        10 - 5 -> Ten Minus Five
        2 = 2  -> Two Equals Two
    """
    pass
    mydict = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five',
            '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '10': 'Ten','+':   ' Plus ',  '-':   ' Minus ',
          '*':   ' Times ',
          '/':   ' Divided By ',
          '**':  ' To The Power Of ',
          '=':   ' Equals ', '!=':  ' Does Not Equal '}
    f = ''
    s = string.split(' ')
    for i in s:
        if i in mydict.keys():
            f += mydict.get(i)
    return f



def t15(lst):
    """
    Найдите сумму элементов на диагоналях

    [[ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]]
    Результат: 30
    """
    s = 0
    i = 0
    for raw in lst:
        s += raw[i] + raw[-(1-i)]
        i +=1
    return s
    pass