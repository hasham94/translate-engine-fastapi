from translatepy import Translator

def translate_text(text: str, target_lang: str = "en") -> str:
    translator = Translator()
    result = translator.translate(text, target_lang)
    return result.result