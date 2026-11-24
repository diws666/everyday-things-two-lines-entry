"""make.fun bounty entry generator: everyday thing explained in two lines."""

import os

LINE1 = (
    "A traffic light is like a referee in a game where cars are the players "
    "and nobody is allowed to argue with the whistle."
)
LINE2 = (
    "It works because the colors really do mean stop and go, like a "
    "referee's calls; it leaves out that drivers sometimes ignore the whistle "
    "anyway."
)

LINES = [LINE1, LINE2]


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(LINES))


if __name__ == "__main__":
    main()
