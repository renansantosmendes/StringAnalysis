import io
from pyjarowinkler import distance
from string_analysis import StringAnalysis

stream = io.StringIO("Hello, there!\nHow are you today?\nYes, you over there.")
sa = StringAnalysis(stream)
word = 'youu'
print(sa.get_most_similar_word(word))
