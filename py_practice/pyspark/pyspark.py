import os
from pprint import pprint

import findspark

findspark.init()
# Import PySpark and initialize SparkContext object.
import pyspark

sc = pyspark.SparkContext()
cwd = os.path.dirname(__file__)


def get_dailyshow():
    PATH_DATA = cwd + '/daily_show.tsv'
    raw_data = sc.textFile(PATH_DATA)
    data = raw_data.map(lambda line: line.split('\t'))
    data = data.map(lambda x: (x[0], 1))
    data = data.reduceByKey(lambda x, y: x + y)
    return data


def filter_year(line):
    if line[0] == 'YEAR':
        return False
    return True


def pipeline(raw_data):
    daily_show = raw_data.filter(lambda line: line[1] != '').map(
        lambda line: (line[1], 0)).reduceByKey(lambda x, y: x + y)

    return daily_show


def read_hamlet():
    PATH_DATA = cwd + '/hamlet.txt'
    raw_data = sc.textFile(PATH_DATA)
    data = raw_data.map(lambda line: line.split('\t'))
    return data


def filter_hamlet_speaks(arr_line):
    if 'HAMLET' in arr_line:
        return True
    return False


def format_id(line):
    id = line[0].split('@')[1]
    result = list()
    result.append(id)
    if len(line) > 1:
        for ele in line[1:]:
            result.append(ele)
    return result


def remove_unuse_info(line):
    pass


def fix_pipe(line):
    if '|' in line:
        line.remove('|')
    return line


def dq_fix_pipe(line):
    results = list()
    for l in line:
        if l == "|":
            pass
        elif "|" in l:
            fmtd = l.replace("|", "")
            results.append(fmtd)
        else:
            results.append(l)
    return results


hamlet = read_hamlet()
# Format id (only contain id without hamlet@)
hamlet = hamlet.map(lambda line: format_id(line))

# Remove elements that don't have any words
hamlet = hamlet.filter(lambda line: len(line) > 1)

# Remove blank space within element
hamlet = hamlet.map(lambda line: [ele for ele in line if ele != ''])
hamlet = hamlet.map(lambda line: [ele for ele in line if ele != '|'])
pprint(hamlet.take(10))
