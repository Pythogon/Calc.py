import time
print("""

=====+++=====
 Welcome to
  Calc.py!
=====+++=====

""")
while True:
    time.sleep(1)
    inp = input("Please enter an equation to calculate! Use 'ans' for last time's answer. X = *, ÷ = / : ")
    ans = eval(inp)
    time.sleep(1)
    print(inp,"=",ans)
