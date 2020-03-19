books = {'book':[
    {'Title': 'Python in easy steps', 'Author': 'Mike McGrath', 'ISBN': '9781840788129', 'Format': 'PB', 'OnHand': 4},
    {'Title': 'I\'m an HTML web page builder', 'Author': 'Max Wainewright', 'ISBN': '9781526301048', 'Format': 'HB', 'OnHand': 2},
    {'Title': 'I\'m an HTML web page builder', 'Author': 'Max Wainewright', 'ISBN': '1526301040', 'Format': 'PB', 'OnHand': 4}
    ]}



print(books['book'][2]['ISBN'])

#books['book'][1]['Format'] = input('Enter format for our book: ')



bookIndex = int(input('Enter the index o the book to be modified: '))
bookAuthor = input('Enter the Author: ')
books['book'][bookIndex]['Author'] = bookAuthor


# Increament a dictionary value
oldValue = books['book'][2]['OnHand']
newValue = oldValue + 1
books['book'][2]['OnHand'] = newValue



print(books)





