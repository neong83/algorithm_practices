from typing import Dict

text = (
    "Suppose we have a set of English text documents "
    "and wish to rank which document is most relevant to the query, "
    "the brown cow . A simple way to start out is by eliminating "
    "documents that do not contain all three words  the brown, and cow, "
    "but this still leaves many documents"
)

exclude_words = ["the", "a", "by", "to", "and", "of", ",", ".", "is"]


# first attempt
# key in dict is O(1)
def convert_list_into_dict(word_list) -> Dict:
    exclusion = {}
    for i in word_list:
        exclusion[i] = ""
    return exclusion


def get_most_repeated_phases(content, exclusion) -> (str, int):
    word = None
    max_count = 0

    exclusion_dict = convert_list_into_dict(exclusion)
    word_dicts = {}

    for i in content.split(" "):
        if i in exclusion_dict.keys():
            continue

        if i in word_dicts.keys():
            word_dicts[i] += 1
        else:
            word_dicts[i] = 1

        if word_dicts[i] > max_count:
            max_count = word_dicts[i]
            word = i

    return (word, max_count)


print(get_most_repeated_phases(text, exclude_words))

# second attempts

word_cout = {}
splited_text = text.replace(",", "").replace(".", "").split(" ")
for w in splited_text:
    if w in exclude_words or len(w) == 0:  # this is O(n)
        continue

    key = w.strip().lower()
    if key in word_cout.keys():
        word_cout[key] += 1
    else:
        word_cout[key] = 1

for word, count in word_cout.items():
    print(f"word={word}, count={count}")
