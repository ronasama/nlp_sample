from nltk.corpus import wordnet

print(wordnet.synsets('tokyo'))

# tokyoの同義語グループを確認する
wordnet.synsets('tokyo') # ->'tokyo.n.01'
tokyo = wordnet.synset('tokyo.n.01')

# tokyoの定義を確認する
print(tokyo.definition())

# tokyoの同義語グループループに存在する単語を確認する
print(tokyo.lemma_names())

# kyotoとosakaosakaの類似語グループを確認
print(wordnet.synsets("kyoto")) # ->'kyoto.n.01'
print(wordnet.synsets("osaka")) # ->'osaka.n.01'

# kyotoやosakaとの類似度を確認する
kyoto = wordnet.synset('kyoto.n.01')
osaka = wordnet.synset('osaka.n.01')
print(tokyo.path_similarity(osaka)) # ->0.25
print(tokyo.path_similarity(kyoto)) # ->0.25
print(kyoto.path_similarity(osaka)) # ->0.33
