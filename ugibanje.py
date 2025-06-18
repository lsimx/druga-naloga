print("Igra ugibanja števil")
print("Razmišljam o številu med 1 in 10 ...")

import random
skrivna_st = random.randint(1, 10)

st = int(input("Vnesite število (1-10): "))

if st == skrivna_st:
    print("Čestitamo, uganili ste!")
else:
    print(f"Nepravilno, številka je bila {skrivna_st}")