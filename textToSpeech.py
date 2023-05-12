from gtts import gTTS

text = "This is Friday"
language = 'en'
output_file = "speech" + ".mp3"

tts = gTTS(text=text, lang=language, slow=False)
tts.save(output_file)

