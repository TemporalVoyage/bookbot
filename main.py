def Words(content):
    print(len(content.split()))

def Characters(content):
    result = {}

    for char in content.lower():
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

def Report(dict):
    temp = list(dict.keys())
    temp.sort()
    print('--- Begin report of books/frankenstein.txt ---')
    for char in temp:
        if char.isalpha():
            print(f"The '{char}' character was found {dict[char]} times")

    print('--- End report ---')

with open('./books/frankenstein.txt') as f:
    file_content = f.read()
    Words(file_content)
    data = Characters(file_content)
    Report(data)
