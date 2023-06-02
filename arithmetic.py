import json
from argparse import ArgumentParser


def arithmetic_encode(input, dicr):
    start = 0
    width = 1
    for char in input:
        p_start, p_end = dicr[char]
        start += width * p_start
        width *= p_end - p_start
    return [start, start + width]


def arithmetic_decode(value, dicr, input_length):
    output_string = ""
    for _ in range(input_length):
        for char, (p_start, p_end) in dicr.items():
            if p_start <= value < p_end:
                output_string += char
                value = (value - p_start) / (p_end - p_start)
                break
    return output_string


def main(args):
    mapping = json.loads(args.mapping)
    if args.action == "encode":
        word = args.word
        print(arithmetic_encode(word, mapping))
    else:
        length = int(args.input_length)
        value = float(args.value)
        print(arithmetic_decode(value, mapping, length))


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("action", choices=("encode", "decode"))

    parser.add_argument("--word")
    parser.add_argument("--mapping", required=True)
    parser.add_argument("--value")
    parser.add_argument("--input-length")

    args = parser.parse_args()
    main(args)
