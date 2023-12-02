#!/usr/bin/env python3

import os
import requests
from datetime import datetime

COOKIE = os.environ.get("COOKIE")
DAY = datetime.today().day

if not COOKIE:
    raise ValueError("Missing COOKIE environment variable")

print(f"Getting input for day {DAY}...")

response = requests.get(
    url=f"https://adventofcode.com/2023/day/{DAY}/input",
    cookies={"session": COOKIE},
    headers={
        "User-Agent": "https://github.com/japiirainen/aoc-2023 by joona.piirainen@gmail.com"
    },
)

if response.status_code != 200:
    raise ValueError(f"Got error response: {response.status_code}")

with open("in", "w", encoding="utf-8") as f:
    print("Writing input to file: `in` in CWD")
    f.write(response.text)

print("Done!")
