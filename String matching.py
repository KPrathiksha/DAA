def stringMatching(words):
    ans = []
    
    for i, s in enumerate(words):
        if any(i != j and s in t for j, t in enumerate(words)):
            ans.append(s)
    
    return ans

words = ["mass", "as", "hero", "superhero"]
print(stringMatching(words))  
