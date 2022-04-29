import sys
import io
import cgi
from django.shortcuts import render

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
form = cgi.FieldStorage()
search = {form.getvalue('q')}

pc_index = {'PC', 'pc', 'Pc', 'パソコン', 'ラップトップ'}
python_index ={'Python', 'python', 'パイソン'}
python_1 = {'int', 'str', 'print', 'bin', 'oct', 'hex', '変数'}
python_2 = {'list', 'tuples', 'dictionaries', 'set', 'append', 'add', 'input', 'issubset', 'リスト'}
python_3 = {'if', 'elif', 'else', 'True', 'False', 'and', 'or', 'not', '条件分岐'}
python_4 = {'for', 'range', 'type', 'pass', 'while', 'break', 'continue', 'ループ'}
python_5 = {'def', 'import', 'pow', 'with', 'open', 'close', 'write', 'as', 'return', '関数'}
python_6 = {'class', 'init', 'self', 'from', 'クラス'}


def get_search(request):
    if search.issubset(pc_index) is True:
        return render(request, 'pc/pc_index.html',)
    elif search.issubset(python_index) is True:
        return render(request, 'python/python_index.html',)
    elif search.issubset(python_1) is True:
        return render(request, 'python/python#1.html',)
    elif search.issubset(python_2) is True:
        return render(request, 'python/python#2.html',)
    elif search.issubset(python_3) is True:
        return render(request, 'python/python#3.html',)
    elif search.issubset(python_4) is True:
        return render(request, 'python/python#4.html',)
    elif search.issubset(python_5) is True:
        return render(request, 'python/python#5.html',)
    elif search.issubset(python_6) is True:
        return render(request, 'python/python#6.html',)
    else:
        return render(request, 'app/index.html',)
