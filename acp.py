class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.split()
        reversed_words = ' '.join(reversed(words))
        return reversed_words
if __name__ == "__main__":
    text = "Hello World! This is a test."
    reverser = StringReverser(text)
    print(reverser.reverse_words())
