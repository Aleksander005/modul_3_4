def single_root_words(root_word, *other_word):
    same_words = [] # Создайте внутри функции пустой список same_words, который пополнится нужными словами
    for word in other_word:
        if (root_word.lower() in word.lower() or
                word.lower() in root_word.lower()):
            same_words.append(word)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'AbLe', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
