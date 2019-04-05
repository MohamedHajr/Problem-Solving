# Python program for KMP Algorithm
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    # create lps[] that will hold the longest prefix suffix
    # values for pattern

    j = 0  # index for pat[]

    # Preprocess the pattern (calculate lps[] array)
    lps = computeLPSArray(pat, M)

    i = 0  # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            print("Found pattern at index " + str(i-j))
            j = lps[j-1]

        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1


def computeLPSArray(pat, M):
    lps = [0] * M  # lps[0] is always 0
    j = 0  # length of the previous longest prefix suffix
    i = 1
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if j != 0:
                j = lps[j-1]
            else:
                lps[i] = 0
                i += 1
    return lps


txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt)

# This code is contributed by Bhavya Jain
