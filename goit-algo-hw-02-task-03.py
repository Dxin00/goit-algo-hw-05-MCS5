import os
import timeit
import pandas as pd
import matplotlib.pyplot as plt

# Реализации алгоритмов поиска
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m > n:
        return -1

    skip = {}
    for k in range(m - 1):
        skip[pattern[k]] = m - k - 1

    k = m - 1
    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            return i + 1
        k += skip.get(text[k], m)
    return -1

def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    m = len(pattern)
    n = len(text)
    lps = compute_lps(pattern)
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def rabin_karp(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return -1

# Функция для чтения файла с различными кодировками
def read_file_with_multiple_encodings(file_path, encodings=['utf-8', 'latin1', 'windows-1251']):
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return f.read()
        except UnicodeDecodeError:
            pass
    raise UnicodeDecodeError(f"Unable to decode file {file_path} with tried encodings.")

# Шлях до теки txt у директорії проекту
txt_dir = os.path.join(os.getcwd(), "txt")

# Список файлів у теки txt
file_names = os.listdir(txt_dir)

# Зчитуємо вміст кожного файлу
texts = {}
for file_name in file_names:
    file_path = os.path.join(txt_dir, file_name)
    texts[file_name] = read_file_with_multiple_encodings(file_path)

# Підрядки для пошуку
patterns = [
    ("алгоритм пошуку", "вигаданий підрядок"),
    ("рекомендаційна система", "незнайомий підрядок")
]

results = []

for file_name, text in texts.items():
    for pattern_pair in patterns:
        for pattern in pattern_pair:
            bm_time = timeit.timeit(lambda: boyer_moore(text, pattern), number=100)
            kmp_time = timeit.timeit(lambda: kmp_search(text, pattern), number=100)
            rk_time = timeit.timeit(lambda: rabin_karp(text, pattern), number=100)
            results.append({
                "file": file_name,
                "pattern": pattern,
                "bm_time": bm_time,
                "kmp_time": kmp_time,
                "rk_time": rk_time
            })

df = pd.DataFrame(results)

# Вывод красивой таблицы
print(df.to_markdown(index=False, tablefmt="grid"))

# Построение графиков
algorithms = ['bm_time', 'kmp_time', 'rk_time']

for algorithm in algorithms:
    plt.figure(figsize=(10, 5))
    for file_name in df['file'].unique():
        subset = df[df['file'] == file_name]
        plt.plot(subset['pattern'], subset[algorithm], marker='o', label=file_name)
    plt.title(f'Comparison of {algorithm.replace("_time", "")} algorithm execution time')
    plt.xlabel('Pattern')
    plt.ylabel('Time (s)')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
