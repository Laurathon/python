def print_upper_words(words):
    """Return list of words in Uppercase"""

    for word in words:
      print(word.upper())

def words_start_with(words):
    """Return list of words that start with an e or E """

    for word in words:
      if word.startswith("e") or word.startswith("E"):
        print(word.upper())

def words_start_with2(words, beginwith):
    """Return list of words that start with a certain letter"""

    for word in words:
      for letter in beginwith:
        if word.startswith(letter) or word.startswith(letter.upper()):
          print(word.upper())
     


      

