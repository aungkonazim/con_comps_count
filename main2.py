import os
import sys
os.environ["PYSPARK_PYTHON"]="python3.6"
import pyspark
sc = pyspark.SparkContext('local[10]')
from pyspark.sql import SparkSession
spark = SparkSession(sc)
from pyspark.sql import functions as F
import itertools
def min_fm(x):
    return [(a,x[0]) for a in x[1]]+[(x[0],a) for a in x[1]]
data = sc.textFile('undirect.graph').map(
    lambda x:(int(x.split(' ')[0]),int(x.split(' ')[1]))).flatMap(
    lambda x:[(x[0],x[1]),(x[1],x[0])]).toDF(
    ['node','neighbor'])
data = data.groupby('node').agg(F.collect_list('neighbor'))
i = 0
checker = []
while True:
    data = data.rdd.map(tuple)
    data = data.flatMap(lambda x:min_fm(x)).toDF(['node','neighbor'])
    data = data.groupby('node').agg(F.collect_set('neighbor'))
    data = data.rdd.map(tuple)
    data = data.map(lambda x: (min([x[0]]+x[1]),list(set(x[1])))).toDF(['node','neighbor'])
    data = data.groupby('node').agg(F.collect_list('neighbor'))
    data = data.rdd.map(tuple)
    data = data.map(lambda x:(x[0],list(itertools.chain(*x[1])))).map(
        lambda x: (min([x[0]]+x[1]),list(set(x[1])))).toDF(['node','neighbor'])
    temp_count = data.count()
    if i==0:
        count = temp_count
        i+=1
    else:
        if temp_count==count and len(checker)>1:
            print('The number of connected components is',count)
            break
        elif temp_count==count:
            print('so far',temp_count)
            count = temp_count
            checker.append(True)
        else:
            print('so far',temp_count)
            count = temp_count
output_sentence = ''.join([str(count)])
with open('CCRes','w') as f:
    f.write(output_sentence)
    f.close()