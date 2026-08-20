class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word.lower()

    def is_word_in(self, text):
        import string
        for char in string.punctuation:
            text = text.replace(char, ' ')
        words = text.lower().split()
        return self.word in words

class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        return self.is_word_in(story.get_title())

class AndTrigger(Trigger):
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2
    def evaluate(self, story):
        return self.t1.evaluate(story) and self.t2.evaluate(story)
