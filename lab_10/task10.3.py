import matplotlib.pyplot as plt
vowels = "аеєиіїоуюя"
with open("/Users/marina/Desktop/PythonLabs/lab_10/lab10_3.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

freq = {}
for i in range(len(text)):
    for j in range(len(vowels)):
        if text[i] == vowels[j]:
            letter = vowels[j]
            freq[letter] = freq.get(letter, 0) + 1
            break
    
sortedVowels = sorted(freq.keys())
counter = [freq[v] for v in sortedVowels]
plt.bar(sortedVowels, counter)
plt.xlabel("Голосні")
plt.ylabel("Частота")
plt.title("Гістограма голосних")

plt.savefig("lab10_3hist.png")
plt.show()
