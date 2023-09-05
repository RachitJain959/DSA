# Given a sentence and a word find the max number of times the word is repeated in.
# The repeated words should be concatenated and next to each other
#
# Example 1:
# Input: -"popokpo", b-po"
# Output: 2
# Explanation: "po is repeated twice and concatenated as "popo" in "popokpo"-

def max_word_repetition(sentence, word):
    max_repetition = 0
    i = 0
    while i < len(sentence):
        if sentence[i:i + len(word)] == word:
            repetition = 1
            j = i + len(word)
            while j < len(sentence) and sentence[j:j + len(word)] == word:
                repetition += 1
                j += len(word)
            max_repetition = max(max_repetition, repetition)
            i = j
        else:
            i += 1
    return max_repetition


# Example usage:
input_sentence = "popokpo"
input_word = "po"
result = max_word_repetition(input_sentence, input_word)
print(result)  # Output: 2
