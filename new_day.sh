
if [ $# -ne 2 ]; then
    echo "usage: $0 <day> <name>"
    exit 1
fi

mkdir day$1

mkdir day$1/part1
touch day$1/part1/$2.py
touch day$1/part1/$2_input.txt

mkdir day$1/part2
