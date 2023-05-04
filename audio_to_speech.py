from deepgram import Deepgram
import deepl

from config import DEEP_GRAM_AUTH_KEY, DEEPL_AUTH_KEY


def upload(audio_file):
    dg = Deepgram(DEEP_GRAM_AUTH_KEY)
    MIMETYPE = "mp3"
    options = {"punctuate": True, "model": "general", "tier": "enhanced"}
    source = {"buffer": audio_file, "mimetype": "audio/" + MIMETYPE}
    res = dg.transcription.sync_prerecorded(source, options)
    res = res["results"]["channels"][0]["alternatives"][0]["transcript"]
    return res
    # res = res.split(".")
    # ret = []
    # for sentence in res:
    #     ret.append(sentence + ".")
    # return ret


def translate_data(text_data, lang):
    translator = deepl.Translator(DEEPL_AUTH_KEY)
    data = ""
    for sentence in text_data.split("."):
        result = translator.translate_text(sentence + ".", target_lang=lang)
        data += result.text
    return data
