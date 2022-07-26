import re
import unicodedata

import soundfile as sf

from vietTTS.hifigan.mel2wave import mel2wave
from app.config import FLAGS
from vietTTS.nat.text2mel import text2mel

def nat_normalize_text(text):
    text = unicodedata.normalize("NFKC", text)
    text = text.lower().strip()
    sil = FLAGS.special_phonemes[FLAGS.sil_index]
    text = re.sub(r"[\n.,:]+", f" {sil} ", text)
    text = text.replace('"', " ")
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[.,:;?!]+", f" {sil} ", text)
    text = re.sub("[ ]+", " ", text)
    text = re.sub(f"( {sil}+)+ ", f" {sil} ", text)
    return text.strip()

def generate_voice(text,output,sample_rate=16000,silence_duration=-1,lexicon_file=None):
    try:
        text = nat_normalize_text(text)
        mel = text2mel(text, lexicon_file, silence_duration)
        wave = mel2wave(mel)
        sf.write(str(output), wave, samplerate=sample_rate)
        return output
    except Exception as e:
        print(e)
        return None


