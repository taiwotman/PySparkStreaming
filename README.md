# Pyspark Streaming

**An example PySpark project.**

The project demonstrate pyspark structured programming using template design pattern

**Upgrade python**

    curl https://bootstrap.pypa.io/get-pip.py | python


**Running Spark job with spark-submit on Command line**

    mkdir ./dist
    cp ./src/main.py ../dist/
    cd ./src && zip -x main.py -r ../dist/wordcount .

    source venv/bin/activate

**To run this PySpark Streaming application, execute the following command from your $SPARK_HOME folder:**

    ./bin/spark-submit wordcount.py localhost 9999

**To begin the streaming, on the command line, type the netcat commmand**

    nc -lk 9999

**Then, start typing your events, for example:**

For the first second, type

        apple apple apple

For the second second, type
    
        orange orange apple

Wait a second; for the fourth second, type
    
        mango mango mang


**Reference**

Structured Streaming Programming Guide: https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#creating-streaming-dataframes-and-streaming-datasets

Creating a PySpark project with pytest, pyenv, and egg files: https://medium.com/@mrpowers/creating-a-pyspark-project-with-pytest-pyenv-and-egg-files-d2709eb1604c
