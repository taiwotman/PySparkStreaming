from word_count.word_count_algo import WordCountAlgorithm
from pyspark.sql.functions import udf

def main():
   
    a = WordCountAlgorithm()
    a.template_method()


if __name__ == "__main__":
    main()