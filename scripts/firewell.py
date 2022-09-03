from scripts.common import preprocess


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

def normalize_firewells():
    global do, vsego
    do = list(map(preprocess, do))
    vsego = list(map(preprocess, vsego))

def detect_firewell(sentence: str) -> bool:
    words = list(map(preprocess, sentence.split()))
    bye_struct = {
        'до': do,
        preprocess('всего'): vsego,
    }
    for word_1, words_2 in bye_struct.items():
        for word_2 in words_2:
            for idx, word in enumerate(words):
                if word != word_1 or idx + 1 == len(words):
                    continue
                if word_2 == words[idx + 1]:
                    return True
    return False

def mark_firewells(monologue: list) -> list:
    normalize_firewells()
    verdict = [detect_firewell(sent) for sent in monologue]
    return verdict