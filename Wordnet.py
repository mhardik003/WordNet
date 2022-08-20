import nltk
from nltk.corpus import wordnet

word = "good"
synset = wordnet.synsets(word)
print(synset)
# [Synset('good.n.01'), Synset('good.n.02'), Synset('good.n.03'), Synset('commodity.n.01'),
#  Synset('good.a.01'), Synset('full.s.06'), Synset('good.a.03'), Synset('estimable.s.02'), Synset('beneficial.s.01'), Synset('good.s.06'), Synset('good.s.07'), Synset('adept.s.01'), Synset('good.s.09'), Synset('dear.s.02'), Synset('dependable.s.04'), Synset('good.s.12'), Synset('good.s.13'), Synset('effective.s.04'), Synset('good.s.15'), Synset('good.s.16'), Synset('good.s.17'), Synset('good.s.18'), Synset('good.s.19'), Synset('good.s.20'), Synset('good.s.21'), Synset('well.r.01'), Synset('thoroughly.r.02')]
print(synset[4].definition())
# having desirable or positive qualities especially those suitable for a thing specified
print(synset[4].hypernyms())
# []
print(synset[4].hyponyms())
# []
print(synset[4].lemmas()[0].antonyms())
# [Lemma('bad.a.01.bad')]
print(synset[4].examples())
# ['good news from the hospital', 'a good report card', 'when she was good she was very very good', 'a good knife is one good for cutting', 'this stump will make a good picnic table', 'a good check', 'a good joke', 'a good exterior paint', 'a good secretary', 'a good dress for the office']


