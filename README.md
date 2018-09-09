# Pyspark Streaming

An example PySpark project.

The project uses pyenv and pytest.  It also demonstrates how to generate egg files.

Here is a link to a blog post that explains how this application was built.

_Url:_ [Creating a PySpark project with pytest, pyenv, and egg files](https://medium.com/@mrpowers/creating-a-pyspark-project-with-pytest-pyenv-and-egg-files-d2709eb1604c)

**Upgrade python**

    curl https://bootstrap.pypa.io/get-pip.py | python


**Running Spark job with spark-submit on Command line**

    mkdir ./dist
    cp ./src/main.py ../dist/
    cd ./src && zip -x main.py -r ../dist/wordcount .

    source venv/bin/activate





**To run this PySpark Streaming application, execute the following command from your $SPARK_HOME folder:**

    ./bin/spark-submit wordcount.py localhost 9999

**In terms of how you time this, one the command line, start with:**

    nc -lk 9999

**Then, start typing your events, for example:**

For the first second, type

        apple apple apple

For the second second, type
    
        orange orange apple

Wait a second; for the fourth second, type
    
        mango mango mang


**Reference**

https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#creating-streaming-dataframes-and-streaming-datasets
