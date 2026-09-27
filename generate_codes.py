import secrets

CHARS = "ABCDEFGHJKMNPQRSTUVWXYZ23456789"


def generate_code(year: int) -> str:
    blocks = [
        "".join(secrets.choice(CHARS) for _ in range(4))
        for _ in range(4)
    ]
    return f"{year}-" + "-".join(blocks)


def generate_codes(year: int, count: int) -> list[str]:
    codes = set()

    while len(codes) < count:
        codes.add(generate_code(year))

    return list(codes)


def main():
    year = int(input("年を入力してください: "))
    count = int(input("生成する個数を入力してください: "))

    if count <= 0:
        print("生成数は1以上にしてください。")
        return

    codes = generate_codes(year, count)

    filename = f"codes_{year}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(codes))

    print(f"{count}個生成しました。")
    print(f"保存先: {filename}")


if __name__ == "__main__":
    main()