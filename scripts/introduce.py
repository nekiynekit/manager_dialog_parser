from .common import preprocess, analyzer


intro_words = [
    'я',
    'зовут',
    'имя',
    'это',
]

def normalize_words():
    global intro_words
    intro_words = list(map(preprocess, intro_words))

def detect_introduce(sentence: str) -> bool:
    words = list(map(preprocess, sentence.split()))
    for intro in intro_words:
        if intro not in words:
            continue
        for idx, word in enumerate(words):
            if word != intro or idx == len(words):
                continue
            next_word = words[idx + 1]
            for item in analyzer.parse(next_word):
                if 'Name' in item.tag:
                    return True
    return False

def mark_introduces(monologue: list) -> list:
    normalize_words()
    verdict = [detect_introduce(sent) for sent in monologue]
    return verdict