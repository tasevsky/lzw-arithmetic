import json
from argparse import ArgumentParser


def lzw_encode(input: str, dictionary: dict):
    encoded = []
    current_word = ""

    for char in input:
        current_word += char
        if current_word not in dictionary:
            dictionary[current_word] = len(dictionary) + 1
            encoded.append(dictionary[current_word[:-1]])
            current_word = char

    if current_word in dictionary:
        encoded.append(dictionary[current_word])

    return encoded


def lzw_decode(encoded_list, dictionary):
    reversed_dict = {int(v): k for k, v in dictionary.items()}
    decoded = []

    for code in encoded_list:
        decoded.append(reversed_dict[int(code)])

    return "".join(decoded)


def main(args):
    mapping = json.loads(args.mapping)
    if args.action == "encode":
        word = args.word
        print(lzw_encode(word, mapping))
    else:
        code = args.code
        print(lzw_decode(code, mapping))


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("action", choices=("encode", "decode"))

    parser.add_argument("--word")
    parser.add_argument("--code", nargs="*")
    parser.add_argument("--mapping", required=True)

    args = parser.parse_args()
    main(args)
