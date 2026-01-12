class TextAnalyzer:
    def __init__(self, text: str):
        self.text=text
        self.special_symbols=r"! / . , & @ # $ % & * ( ) _ + > <  ' 1 2 3 4 5 6 7 8 9 0 « » [ ] { } ; : \n".split(' ')

    def count(self):
        return f"Number of the words in the text is {len(self.text.split(' '))}"

    def letters_in(self):
        lower_text=self.text.lower()
        letters={}
        for letter in lower_text:
            if letter not in letters.keys():
                if letter in self.special_symbols:
                    continue
                letters[letter] = 1
            else:
                letters[letter]+=1
        return letters

    def popular_words(self):
        lower_text=self.text.lower().split(" ")
        popular_words={}
        for word in lower_text:
            new_word=word
            for symbol in self.special_symbols:
                if new_word.find(symbol)!=-1:
                    new_word=new_word.replace(symbol, '')
                else:
                    continue

            if new_word not in popular_words.keys():
                popular_words[new_word]=1
            else:
                popular_words[new_word]+=1
        return popular_words