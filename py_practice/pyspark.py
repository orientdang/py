# Find path to PySpark.
from pprint import pprint

import findspark

findspark.init()

# Import PySpark and initialize SparkContext object.
import pyspark

sc = pyspark.SparkContext()

# Read `recent-grads.csv` in to an RDD.
f = sc.textFile('/Users/dangnh/dq/jupiter/data-set/cars.csv')
data = f.map(lambda line: line.split('\n'))
pprint(data.take(10))
