from translate import Translator

translator= Translator(to_lang="bn")
translation = translator.translate("This is a pen.")
print(translation)