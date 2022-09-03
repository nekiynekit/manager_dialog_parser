from .common import preprocess


greets = [
    'Привет',
    'Здравствуйте',
    'Алло',
    ]

good = preprocess('Добрый')

good_anything = [
    'День',
    'Вечер',
    'Утро',
]

def normalize_greetings():
    global greets, good_anything
    greets = list(map(preprocess, greets))
    good_anything = list(map(preprocess, good_anything))

def detect_greeting(sentence: str) -> bool:
    words = list(map(preprocess, sentence.split()))
    for greet in greets:
        if greet in words:
            return True
    if good not in words:
        return False
    idx = words.index(good) + 1
    if idx < len(words) and words[idx] in good_anything:
        return True
    return False

def mark_greetings(monologue: list) -> list:
    normalize_greetings()
    verdict = [detect_greeting(sent) for sent in monologue]
    return verdict