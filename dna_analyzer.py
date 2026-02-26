dna = input("Enter DNA sequence: ").upper()

length = len(dna)

a = dna.count("A")
t = dna.count("T")
g = dna.count("G")
c = dna.count("C")

gc_content = ((g + c) / length) * 100

print("\nSequence Length:", length)
print("A:", a)
print("T:", t)
print("G:", g)
print("C:", c)
print("GC Content: {:.2f}%".format(gc_content))