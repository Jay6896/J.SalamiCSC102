print("Design a flowchart and write a python program \nfor the following problems: \na)Simple Interest \nb)Compound Interest \nc)Annuity Plan")
print("\nSimple Interest: \nlet P = 500, let R = 5, let T = 3")
SimpleP = 500
SimpleR = 5
SimpleT = 3
SimpleA = SimpleP * (1 + (SimpleR / 100) * SimpleT)

print("The Amount is = ", SimpleA)

print("\nCompound Interest: \nlet P = 500, let R = 10, let N = 100, let NT = 2")
CompP = 500
CompR = 10
CompN = 100
CompNT = 2
CompA = CompP * ( 1 + (CompR / CompN)) ** CompNT

print("The Amount is = ", CompA)

print("\nAnnuity Plan: \nlet PMT = 200, let R = 5, let N = 100, let NT = 3")
AnnuPMT = 200
AnnuR = 5
AnnuN = 100
AnnuNT = 3
AnnuA = AnnuPMT * ( (((1 + (AnnuR / AnnuN)) ** (AnnuNT)) - 1) / (AnnuR / AnnuN))

print("The Annuity Plan is = ", AnnuA)


