from gtts import gTTS
import os

# The text that you want to convert to audio
mytext = 'Welcome to Global Hack Week!'
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("mpg321 welcome.mp3")
