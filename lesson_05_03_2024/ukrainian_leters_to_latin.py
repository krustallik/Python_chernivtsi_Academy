class UkrainianEnglishNameTranslator:
    def __init__(self):
        self.transliteration_map = {
            'а': 'a',
            'б': 'b',
            'в': 'v',
            'г': 'h',
            'ґ': 'g',
            'д': 'd',
            'е': 'e',
            'є': 'ye',
            'ж': 'zh',
            'з': 'z',
            'и': 'y',
            'і': 'i',
            'ї': 'i',
            'й': 'i',
            'к': 'k',
            'л': 'l',
            'м': 'm',
            'н': 'n',
            'о': 'o',
            'п': 'p',
            'р': 'r',
            'с': 's',
            'т': 't',
            'у': 'u',
            'ф': 'f',
            'х': 'kh',
            'ц': 'ts',
            'ч': 'ch',
            'ш': 'sh',
            'щ': 'shch',
            'ь': '',
            'ю': 'yu',
            'я': 'ya',
        }


    def translate(self, word):
        def translate_letter(letter):
            return self.transliteration_map.get(letter, letter)

        translated_letters = map(translate_letter, word)
        return ''.join(translated_letters)



translator = UkrainianEnglishNameTranslator()
print(translator.translate('євген'))
print(translator.translate('ольга'))
print(translator.translate('андрій'))
