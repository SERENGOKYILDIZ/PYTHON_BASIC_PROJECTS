import pandas

file = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in file.iterrows()}

secim = input("Bir isim giriniz\n")

secim_list = [value for n in secim for (key, value) in nato_dict.items() if key.lower() == n.lower()]
print(secim_list)


