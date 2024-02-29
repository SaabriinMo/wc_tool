import argparse
import wc_tool
import sys


def argparse_ccwc():
    parser = argparse.ArgumentParser(description="wc tool")
    parser.add_argument("-c", action="store_true", help="gets the byte count")
    parser.add_argument("-l", action="store_true",help="outputs number of lines in file")
    parser.add_argument("-w", action="store_true", help="outputs number of words in files")
    parser.add_argument(
        "-m", action="store_true", help="outputs number of characters in files"
    )
    parser.add_argument("file", nargs="?", type=str)
    return parser.parse_args()


def output(args):
    result = []
    if args.c:
        result.append(wc_tool.wc_byte_count(args.file))
    if args.l:
        result.append(wc_tool.wc_line_count(args.file, ))
    if args.w:
        result.append(wc_tool.wc_word_count(args.file))
    if args.m:
        result.append(wc_tool.wc_char_count(args.file))

    if not any([args.c, args.l, args.w, args.m]):
        result.extend([args.file, wc_tool.wc_byte_count(args.file), wc_tool.wc_line_count(args.file, ),
                       wc_tool.wc_word_count(args.file)])

    return " ".join(map(str, result))


def main():
    args = argparse_ccwc()
    if args.file:
        ccwc = output(args)
        print(" ", ccwc)
    else:
        results = []
        content = sys.stdin.buffer.read()
        if "-c" in sys.argv[1:]:
            results.append(len(content))
        if "-l" in sys.argv[1:]:
            results.append(content.count(b'\n'))
        if "-w" in sys.argv[1:]:
            results.append(len(content.split()))
        if not any([args.c, args.l, args.w, args.m]):
            results.extend([len(content), content.count(b'\n'), len(content.split())])
        print("  ", " ".join(map(str, results)))


if __name__ == "__main__":
    main()
