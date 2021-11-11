import sys
import DZ_4_2

command = sys.argv[1]
list = DZ_4_2.currency_rates(command)
print(f"на {list[0]} 1 {list[1]} {list[2]} рублей")