fn = 0
fn1 = 1
for n in range(0, 13):
    fn2 = fn1+fn
    fn = fn1
    fn1 = fn2
print("Nombre de couples après 13 mois :", fn)

fn = 0
fn1 = 1
n = 0
while fn < 1000000000:
    fn2 = fn1+fn
    fn = fn1
    fn1 = fn2
    n = n+1
print("Nombre de mois pour avoir 1 000 000 000 de couples :", n)
