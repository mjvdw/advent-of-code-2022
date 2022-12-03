from rich.console import Console
from aocd import get_data, submit
import time
import string
from enum import Enum, auto, IntEnum

YEAR = 2022
DAY = 3
PART = "a"


c = Console()
start_time = time.perf_counter()
data = get_data(year=YEAR, day=DAY)
c.rule(f"Advent of Code {YEAR}-{DAY}{PART}")
####################################################################################

parsed = [(i[:len(i)//2], i[len(i)//2:]) for i in data.strip().split("\n")]
common_items = [next(iter((set(j[0]) & set(j[1])))) for j in parsed]
priorities = [string.ascii_letters.index(
    k)+1 for k in common_items if k.islower]

answer = sum(priorities)
print(answer)

####################################################################################
c.rule("Finished")

submit(year=YEAR, day=DAY, part=PART, answer=answer)
