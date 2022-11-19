import googletrans
from googletrans import Translator
translator = Translator()
result = translator.translate('Привет, это работа студента ИКБО-24-20 Постнова Никиты')
print("\n")
print(result.origin)#Вывод оригинального текста
print("\n")
print(result.text)#Перевод,по умолчнию английский 
print("\n")