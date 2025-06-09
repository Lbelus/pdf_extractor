import re
from pdf2image import convert_from_path
import pytesseract

def extract_total_from_pdf(pdf_path):
    pages = convert_from_path(pdf_path)
    for i, page in enumerate(pages):
        text = pytesseract.image_to_string(page)
        print(f"[DEBUG] Page {i+1} OCR Output:\n{text}\n")

        match = re.search(r"Total\s*:?\s*([\d.,]+)\s*(EUR|€)", text, re.IGNORECASE)
        if match:
            total_value = match.group(1)
            print(f"Total value found: {total_value} EUR")
            return total_value
    print("Total value not found.")
    return None

def longest_prefix_suffix(pattern):
    size = len(pattern) 
    lps = [None] * size
    lps[0]  = 0
    index   = 1
    length  = 0

    while index < size:
        if pattern[index] == pattern[length]:
            length += 1
            lps[index] = length
            index += 1
        else:
            if length  != 0:
                length = lps[length - 1]
            else:
                lps[index] = 0
                index += 1
    return lps


def kmp(text, pattern):
    matches = []
    pattern_len = len(pattern)
    text_len = len(text)
    if pattern_len == 0 or text_len < pattern_len:
        return matches
    lps = longest_prefix_suffix(pattern)

    index = 0
    jndex = 0
    
    while index < text_len:
        if text[index] == pattern[jndex]:
            index += 1
            jndex += 1
            if jndex == pattern_len:
                matches.append(index - jndex)
                jndex = lps[jndex - 1]
        elif jndex > 0:
            jndex = lps[jndex - 1]
        else:
            index += 1
    return matches
    
print(longest_prefix_suffix("a"))                # [0]           - single character
print(longest_prefix_suffix("aaaa"))             # [0, 1, 2, 3]  - repeated character
print(longest_prefix_suffix("abcdabca"))         # [0, 0, 0, 0, 1, 2, 3, 1]
print(longest_prefix_suffix("abcab"))            # [0, 0, 0, 1, 2]
print(longest_prefix_suffix("abcaby"))           # [0, 0, 0, 1, 2, 0]

# Basic match
print(kmp("ababcababcabc", "abc"))  # [2, 7, 10]

# Pattern at the beginning
print(kmp("abcabcabc", "abc"))      # [0, 3, 6]

# Pattern at the end
print(kmp("xyzabc", "abc"))         # [3]

# Pattern not in text
print(kmp("abcdef", "gh"))          # []

# Multiple overlapping matches
print(kmp("aaaaa", "aaa"))          # [0, 1, 2] (due to overlapping)

# Empty pattern
print(kmp("abcde", ""))             # []

# Pattern longer than text
print(kmp("abc", "abcdef"))         # []

# Entire text is the pattern
print(kmp("pattern", "pattern"))    # [0]

# Repeating substring
print(kmp("abababab", "abab"))      # [0, 2, 4]

# No matches but same characters
print(kmp("aaaaaa", "aaaab"))       # []

# extract_total_from_pdf("docs/dummy_delivery.pdf")

