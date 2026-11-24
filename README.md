# One-Line Office Joke: 24-Hour Sprint

Entry for the make.fun competition
`u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162`.

## The entry

Running `main.py` (Python 3.13) writes exactly one line — a single joke about
office life, at most 200 characters — to `/output/entry.txt`.

> Our printer only ever jams in the hour before a deadline, so I started CC'ing it on my calendar invites — it still hasn't replied.

The joke treats the office printer as the most passive-aggressive colleague
in the building: it only ever breaks when it matters most, and inviting it to
the meeting changes nothing.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` validates its own output before writing: the joke must be a single
non-blank line of 1–200 characters, or it refuses to write anything.
