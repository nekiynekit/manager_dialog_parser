from locale import normalize
import pymorphy2 as pm2


analyzer = pm2.MorphAnalyzer()

def preprocess(word: str) -> str:
    return analyzer.parse(word)[0].normal_form

def normalize(words: list) -> list:
    return list(map(preprocess, words))

intro_words = [
    'я',
    'зовут',
    'имя',
    'это',
]
greets = [
    'Привет',
    'Здравствуйте',
    'Алло',
    ]
good_anything = [
    'День',
    'Вечер',
    'Утро',
]
do = [
    'свидания',
    'скорого',
    'завтра',
    'встречи',
    'скорой',
]
vsego = [
    'хорошего', 
    'доброго',
    'наилучшего',
]

good = preprocess('Добрый')
intro_words = normalize(intro_words)
greets = normalize(greets)
good_anything = normalize(good_anything)
do = normalize(do)
vsego = normalize(vsego)