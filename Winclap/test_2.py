def annograms(word):
    annograms = []
    
    word1 = list(word)
    word1.sort()
    word1 = ''.join(word1)
    
    words = [w.rstrip() for w in open('/Users/rodrigohofer/downloads/WORD.LST')] 
    for w in words: 
        word2 = w 
        w = list(w)
        w.sort()
        w = ''.join(w)
        if (word1 == w):
            annograms.append(word2) 

    return annograms
    

if __name__ == "__main__": 
    print(annograms("train")) 
    print('--') 
    print(annograms('drive')) 
    print('--') 
    print(annograms('python'))