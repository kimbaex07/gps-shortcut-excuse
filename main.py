import os

LINE = "Look, the map said shortcut and I trust the map more than I trust you \u2014 you still think north is \u2018that way\u2019. The cul-de-sac has lovely roses. You\u2019re welcome."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
