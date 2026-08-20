def get_word_score(word, n):
    word = word.lower()
    first_part = sum(SCRABBLE_LETTER_VALUES.get(c, 0) for c in word)
    second_part = max(1, 7 * len(word) - 3 * (n - len(word)))
    return first_part * second_part

def is_valid_word(word, hand, word_list):
    word = word.lower()
    temp_hand = hand.copy()
    
    # Check if word is in list (handling wildcards)
    possible_words = []
    if '*' in word:
        for v in 'aeiou':
            possible_words.append(word.replace('*', v))
    else:
        possible_words.append(word)
        
    if not any(w in word_list for w in possible_words):
        return False
        
    # Check if hand has enough letters
    for char in word:
        if temp_hand.get(char, 0) > 0:
            temp_hand[char] -= 1
        else:
            return False
    return True
