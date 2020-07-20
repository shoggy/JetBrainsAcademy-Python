import sys

import requests
from bs4 import BeautifulSoup

URL_TEMPLATE = 'https://context.reverso.net/translation/{}/{}'
HEADERS_USER_AGENT = {'User-Agent':
                          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/83.0.4103.106 Safari/537.36"}

languages = {
    "Arabic",
    "German",
    "English",
    "Spanish",
    "French",
    "Hebrew",
    "Japanese",
    "Dutch",
    "Polish",
    "Portuguese",
    "Romanian",
    "Russian",
    "Turkish"
}


def normalize_text(s: str) -> str:
    return s.replace('"', '').replace("'", '').replace('.', '').strip()


def translate(fr: str, to: str, w: str) -> str:
    translate_dir = f"{fr}-{to}".lower()
    result = ''

    url = URL_TEMPLATE.format(translate_dir, w)
    try:
        resp = requests.get(url, headers=HEADERS_USER_AGENT)
        if not resp:
            return f"Sorry, unable to find {w}"
    except requests.exceptions.ConnectionError:
        return "Something wrong with your internet connection"
    soup = BeautifulSoup(resp.content, "html.parser")
    translation_words = [normalize_text(x.text)
                         for x in soup.select(".translation.dict")]
    translation_phrases = [x.text.strip()
                           for x in soup.select(".example .text")]

    result += 'Context examples:\n\n'
    result += f'{to_lang.capitalize()} Translations:\n'
    for _, s in zip(range(5), translation_words):
        result += s + '\n'
    result += '\n'
    result += f'{to_lang.capitalize()} Examples:\n'
    for _, s, t in zip(range(5),
                       translation_phrases[::2],
                       translation_phrases[1::2]):
        result += f'{s}:\n{t}\n\n'
    return result


def check_language(lang: str) -> bool:
    if lang.capitalize() not in languages and lang != 'all':
        print(f"Sorry, the program doesn't support {lang}")
        return False
    return True


args = sys.argv
if len(args) < 4:
    raise AttributeError("3 params required")
from_lang = args[1].lower()
to_lang = args[2].lower()
word = args[3]

if check_language(from_lang) and check_language(to_lang):
    with open(f"{word}.txt", "w", encoding='utf-8') as fout:
        if to_lang != 'all':
            translation = translate(from_lang, to_lang, word)
            print(translation)
            fout.write(translation)
        else:
            for to_lang in (v for v in languages if v != from_lang):
                translation = translate(from_lang, to_lang, word)
                print(translation)
                fout.write(translate(from_lang, to_lang, word))
                if translation.startswith("Something wrong") or \
                        translation.startswith("Sorry, unable to find"):
                    break
