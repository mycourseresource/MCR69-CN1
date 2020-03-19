import io, json

libUsers = {'users': [{'userName': 'stefan', 'password': '1234'}, {'userName': 'sean', 'password': '5678'}]}

print(libUsers['users'][1]['userName'])

libBooks = {'books': [
    {'title': 'Python Codebook Part 1', 'isbn': '123456789', 'author': 'Jim D.', 'year': '2019'},
    {'title': 'Python Codebook Part 2', 'isbn': '223456789', 'author': 'Jim D.', 'year': '2020'}
    ]}


print(libBooks['books'][0]['author'])

strBooks = json.dumps(libBooks, ensure_ascii=False)
print(libBooks)
print(strBooks)

with io.open('books.txt', 'w', encoding='utf-8') as f:
    f.write(strBooks)

with open('books.txt') as f:
    data = json.load(f)

print(data)


data['books'][0]['author'] = input('Enter the authors name: ')

print(data)

input('Click to continue')