import streamlit as st

def levenshtein_distance(s1, s2):
    rows = len(s1) + 1
    cols = len(s2) + 1

    dp = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        dp[i][0] = i

    for j in range(cols):
        dp[0][j] = j

    for i in range(1, rows):
        for j in range(1, cols):
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = 1

            dp[i][j] = min(
                dp[i - 1][j] + 1,        # xóa
                dp[i][j - 1] + 1,        # chèn
                dp[i - 1][j - 1] + cost  # thay thế
            )

    return dp[-1][-1]

def load_vocab(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
        vocabs = sorted(word.lower() for word in words)
        return vocabs

vocabs = load_vocab('./word_net.txt')

st.title('word correction')
word_input = st.text_input('your input word')

if st.button('compute'):
    distances = dict()
    for vocab in vocabs:
        distance = levenshtein_distance(word_input, vocab)
        distances[vocab] = distance
    sorted_distance = dict(sorted(distances.items(), key= lambda x: x[1]))
    correct_word = list(sorted_distance.keys())[0]
    st.write(correct_word)

    col1, col2 = st.columns(2)
    col1.write(vocabs)
    col2.write(sorted_distance)
