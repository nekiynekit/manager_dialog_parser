import pymorphy2 as pm2


analyzer = pm2.MorphAnalyzer()

def preprocess(word):
    return analyzer.parse(word)[0].normal_form