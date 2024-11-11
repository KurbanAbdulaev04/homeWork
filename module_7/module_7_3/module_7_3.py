class WordsFinder:
    def __init__(self, *args):
        self.file_names = list(args)

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as file:
                f = file.read().lower()
                for j in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    f = f.replace(j, '')
                f = f.split()
                all_words[i] = f

        return all_words

    def find(self, word):
        result = {}
        for key, value in self.get_all_words().items():
            for i in value:
                if word.lower() == i:
                    result[key] = value.index(i) + 1 # прибавили один потому-что индекс начинается с нуля

        return result

    def count(self, word):
        result = {}
        for key, value in self.get_all_words().items():
            for i in value:
                if word.lower() == i:
                    result[key] = value.count(i)

        return result



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего





finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))
