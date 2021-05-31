import calendar
import cProfile
import datetime as dt
import getpass
import multiprocessing
import os
import site
import socket
import sys
from math import pi
from os import listdir
from os.path import isfile, join
from pprint import pprint
from subprocess import call


def python_version():
    print('Python version', sys.version)
    print('Version info', sys.version_info)


def get_now():
    now = dt.datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')
    print(now_str)


def cal_circle_area():
    r = float(input("Input the radius of the circle : "))
    print("The area of the circle with radius " + str(r) + " is: " +
          str(pi * r**2))


def fname_lname():
    fname = input("input first name:")
    lname = input("input last name:")
    print(lname + ' ' + fname)


def gen_from_comma_numbers():
    values = input("Input some comma seprated numbers : ")
    lst = values.split(',')
    tp = tuple(lst)
    print('List : ', lst)
    print('Tuple : ', tp)


def print_calender():
    y = int(input("Input the year : "))
    m = int(input("Input the month : "))
    print(calendar.month(y, m))


def cal_datetime():
    f_date = dt.date(year=2020, month=11, day=24)
    l_date = dt.date(year=2021, month=5, day=24)
    delta = l_date - f_date
    print(delta.days)


def near_thousand(n):
    if abs(1000 - n) <= 100:
        print(True)
    elif abs(2000 - n) <= 100:
        print(True)
    else:
        print(False)


def larger_string(i_str, n):
    result = ""
    for _ in range(n):
        result += i_str
    print(result)


def get_diff(lst1, lst2):
    lst1 = set(lst1)
    lst2 = set(lst2)
    result = lst1.difference(lst2)
    return result


def sum_within_range(num1, num2):
    total = num1 + num2
    if total in range(15, 20):
        return 20
    else:
        return total


def locate_py_package():
    return site.getsitepackages()


def call_external_cmd():
    call(["ls", "-l"])


def get_curr_executing():
    print(__file__)
    print(os.path.realpath(__file__))


def count_cpu():
    return multiprocessing.cpu_count()


def list_dir():
    dir = '/Users/dangnh/py-practice'
    files = [f for f in listdir(dir) if isfile(join(dir, f))]
    return files


def print_without_newline():
    print('*', end="")
    print('\n')


def profiling_program():
    cProfile.run('test_profiling()')


def test_profiling():
    print(1 + 2)


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_envir():
    # Access all environment variables
    print('*----------------------------------*')
    print(os.environ)
    print('*----------------------------------*')
    # Access a particular environment variable
    print(os.environ['HOME'])
    print('*----------------------------------*')
    print(os.environ['PATH'])
    print('*----------------------------------*')


def get_curr_username():
    return getpass.getuser()


def find_local_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def terminal_size():
    import fcntl
    import struct
    import termios

    th, tw, hp, wp = struct.unpack(
        'HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)))
    return tw, th


def get_execution_time(func, *args, **kwargs):
    import time
    start = time.time()
    func(*args, **kwargs)
    end = time.time()
    return end - start


def get_absolute_file_path():
    current_file = str(__file__)
    return os.path.abspath(__file__)


def get_creation_time():
    import os.path
    import time
    print("Last modified: %s" % time.ctime(os.path.getmtime(__file__)))
    print("Created: %s" % time.ctime(os.path.getctime(__file__)))


def sort_file():
    import glob
    import os
    files = glob.glob('/Users/dangnh/py-practice/py_practice/*.py')
    files.sort(key=os.path.getmtime)
    print(files)


def get_cmd_args():
    import sys
    print("This is the name/path of the script:"), sys.argv[0]
    print("Number of arguments:", len(sys.argv))
    print("Argument List:", str(sys.argv))


def get_detail_module(module):
    return dir(module)


def find_avalable_buildin():
    import sys
    import textwrap

    module_name = ', '.join(sorted(sys.builtin_module_names))
    print(textwrap.fill(module_name, width=70))


def swap(a, b):
    a, b = b, a
    return a, b


def get_identity():
    print(str)
    oj1 = dict()
    oj2 = oj1
    print(id(oj1))
    print(id(oj2))


def clear_terminal():
    import os
    import time
    os.system('ls')
    time.sleep(2)
    os.system('clear')


def get_hostname():
    import socket
    host_name = socket.gethostname()
    print(host_name)


def print_url_content():
    URL = "google.com"
    from http.client import HTTPConnection
    conn = HTTPConnection(URL)
    conn.request("GET", '/')
    result = conn.getresponse()
    content = result.read()


def filter_negative_numbers():
    nums = [34, 1, 0, -23]
    filterd = list(filter(lambda x: x >= 0, nums))
    print(filterd)


def compute_products():
    from functools import reduce
    nums = [
        10,
        20,
        30,
    ]
    result = reduce(lambda x, y: x * y, nums)
    print(result)


def make_chunks(lst, num_chunks, s=0):
    chunk_list = list()
    len_lst = len(lst)
    result = [lst[i:i + num_chunks - 1] for i in range(0, len_lst, num_chunks)]
    for i in range(s, len_lst, num_chunks):
        start = i
        end = i + num_chunks
        chunk = lst[start:end]
        chunk_list.append(chunk)
    return chunk_list


def three_sum(lst):
    result = list()
    for i in range(len(lst)):
        chunks = make_chunks(lst, 3, i)
        for chunk in chunks:
            if sum(chunk) == 0 and len(chunk) == len(set(chunk)) == 3:
                result.append(chunk)
    return result


x = [1, -6, 4, 2, -1, 2, 0, -2, 0]
print(three_sum(x))
