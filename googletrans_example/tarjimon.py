from googletrans import Translator

tarjimon = Translator()
matn = "Salom, men dasturchiman."
tarjima = tarjimon.translate(text=matn, dest='ru', src='uz')
print(tarjima.text)
