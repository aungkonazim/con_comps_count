# P2-Bigdata
Connected Component Count

**Configuration**

We used apache spark prebuilt version from pip.  

Please run `pip install -r requirements.txt` to install the dependencies

The spark context that we used had the following properties

[('spark.rdd.compress', 'True'),
 ('spark.serializer.objectStreamReset', '100'),
 ('spark.ui.showConsoleProgress', 'true'),
 ('spark.submit.deployMode', 'client'),
 ('spark.driver.memory','5g'),
 ('spark.num.executor','10'),
 ('spark.executor.cores','1'),
 ('spark.worker.memory','32g')]

**Note**

Please note that you need to change the environment variable with the version of python you are using
 
` import os
 os.environ["PYSPARK_PYTHON"]="python3.6"` (assuming python3.6 is your python version)

Change these two lines of code accordingly

**Exceution**

Main code is in "main2.py" file

Please run the code in terminal with the filepaths as input arguments

Run the one of the following lines in terminal 

`python3.6 main2.py 

or 

spark-submit main2.py
`
If you need to change the directory of the files please change it inside the code.



**Results**

The code runs for both the smaller and bigger dataset provided.

Run it for the bigger dataset with a cluster(approx 10 nodes) if possible.(Takes around 3 minutes)

The number of connected component for the bigger graph is 676 as given in the output '`CCRes`' file.
For smaller dataset it is 2


**Algorithm Description**

No help from any library is taken here.

The pseudocode is given below

**PseudoCode:**

    1. For each edge produce two key-value pairs (since undirected graph)
    
    2. Reduce the mapped pairs to generate the (nodeID,neighborList) format
    
    3. Transform each (nodeID,neighborList) to (transformedNodeID,uniqueNeighborList) where
     transformedNodeID is the minimum of all the nodes in neighborList and nodeID. uniqueNeighborList 
     is the unique set of neighborList
    
    4. Merge two pairs with the same transformedNodeID (reduceByKey does it)
         
    5. If the number of pairs of (transformedNodeID,uniqueNeighborList) is same from the previous iteration then stop.
    It is same as the number of components
    
    4. Using FlatMapping produce the edge list from the transformed pairs


**Proof**

At the end of the data each component is reduced to a collection of (key,value) pairs where key is the minimum nodeID of the
component and value contains the list of nodes in that component



