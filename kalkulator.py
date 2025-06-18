print("\nPreprost kalkulator")
print("Operacije: +, -, *, /")

st1 = float(input("Vnesite prvo številko: "))
operator = input("Vnesite operator: ")
st2 = float(input("Vnesite drugo številko: "))

if operator == "+":
    rezultat = st1 + st2
elif operator == "-":
    rezultat = st1 - st2
elif operator == "*":
    rezultat = st1 * st2
elif operator == "/":
    if st2 != 0:
        rezultat = st1 / st2
    else:
        print("Napaka: Z ničlo ni mogoče deliti!")
        rezultat = None
else:
    print("Napaka: Neveljaven operator!")
    rezultat = None

if rezultat is not None:
    print(f"Rezultat: {st1} {operator} {st2} = {rezultat}")