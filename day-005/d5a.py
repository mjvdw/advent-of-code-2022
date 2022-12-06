from aocd import get_data, submit
from rich.console import Console

YEAR = 2022
DAY = 5
PART = "a"


c = Console()
data = get_data(year=YEAR, day=DAY)
c.rule(f"Advent of Code {YEAR}-{DAY}{PART}")
####################################################################################

print(data)

####################################################################################
c.rule("Finished")

# submit(year=YEAR, day=DAY, part=PART, answer=answer)
