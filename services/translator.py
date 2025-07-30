from translatepy import Translator

def translate_text(text: str, target_lang: str = "en") -> str:
    translator = Translator()
    if target_lang == "auto":
        detected_lang = translator.language(text)
        print(f"Detected language: {detected_lang.result}")
        result = translator.translate(text, "en")
    else:
        result = translator.translate(text, target_lang)

    return result.result