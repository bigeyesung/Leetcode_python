



def isAlienSorted(words, order):
        m = {c: i for i, c in enumerate(order)}
        words = [[m[c] for c in w] for w in words]
        for w1, w2 in zip(words, words[1:]):
            print(w1)
            print(w2)
            test = (w1 <= w2 for w1, w2 in zip(words, words[1:]))
            print(test)
            ret = all(test)

        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))



arr = [1,3,4]
arr.sort(reverse=True)

word = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

ret = isAlienSorted(word,order)
print(ret)