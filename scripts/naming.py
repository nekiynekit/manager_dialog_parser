from scripts.common import preprocess, analyzer, intro_words


def get_name(introduce: str) -> str or None:
    words = list(map(preprocess, introduce.split()))
    for intro in intro_words:
        for idx, word in enumerate(words):
            if word != intro or idx + 1 == len(words):
                continue
            next_word = words[idx + 1]
            for item in analyzer.parse(next_word):
                if 'Name' in item.tag:
                    return next_word
    return None

def extract_names(introduces: list) -> list:
    names = [get_name(intro) for intro in introduces]
    return names