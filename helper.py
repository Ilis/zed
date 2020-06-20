def words_order(text: str, words: list) -> bool:
    return [w for w in text.split() if w in words] == words


if __name__ == '__main__':
    print("Example:")
    print(words_order('hi hi hi hi here', ['hi', 'here']))
