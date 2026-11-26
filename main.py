# u-motasimfuad-texts-from-your-future-self-dd44595e entry (Python 3, standard library only):
# writes one funny text message from the writer's future self to
# $MAKEFUN_OUTPUT_DIR/entry.txt (default /output). No trailing newline:
# the entry is exactly the line.
import os

LINE = "Hey, it's you from 2039. The password manager you keep putting off? It holds 412 logins, Dave from IT reset the master password twice, and your 2FA app outlived two phones. Future me is locked out."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(path, line):
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)


def main():
    assert 1 <= len(LINE) <= 200, "entry line must be 1-200 chars"
    assert LINE.strip(), "entry line must not be only whitespace"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    write_entry(os.path.join(OUTPUT_DIR, "entry.txt"), LINE)


if __name__ == "__main__":
    main()
