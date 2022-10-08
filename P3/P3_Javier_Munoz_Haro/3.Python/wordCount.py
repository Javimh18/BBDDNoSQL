import redis, sys, re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

path_to_lua = "/Users/javiermunoz/Universidad/Master/Segundo/BBDDNoSQL/P3/2.LUA/hello.lua"

a,b = 'áéíóúüñÁÉÍÓÚÜÑ','aeiouunAEIOUUN'
trans = str.maketrans(a,b)

def clean_file(path):
    f = open(path, "r")
    s = f.read()
    list_of_words =  re.sub(r'[^\w\s]','',s).translate(trans).split()
    list_of_words_no_stopwords = [word for word in list_of_words if not word in stopwords.words()]
    return list_of_words_no_stopwords

if __name__ == '__main__':

    if len(sys.argv) <= 1:
        print("ERROR:python <path_to_script> <path_to_file> ")
        exit(0)

    file = sys.argv[1]
    list_of_words = clean_file(file)
    r = redis.Redis(host="127.0.0.1", port=6379)
    ordered_set = "words"
    for word in list_of_words:
        res = r.zscore(ordered_set, word)
        if res is None:
            r.zadd(ordered_set, {word: 1})
        else:
            r.zadd(ordered_set, {word: (r.zscore(ordered_set, word) + 1)})
                 
    all_values_scores = r.zrange(ordered_set, 0, 9, desc=True, withscores=True)

    for tup in all_values_scores:
        print(tup[0].decode('ascii'), int(tup[1]), '\n')

    r.delete(ordered_set)