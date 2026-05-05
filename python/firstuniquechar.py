# Input: "aabbcdeff"
# Output: "c"
s = input("enter the strings:")
z =list(s)
#freq.get(key, default_value)
freq ={}
for i in s:
    freq[i] = freq.get(i,0)+1
    print(freq)

'''
    how .get() works in dictionary?
    Ans:
    dict.get(key, default) means:

    If key exists → return value
    If not → return default

    
'''
for ch in s:
    if freq[ch] == 1:
        print(ch)
        break
