from __future__ import print_function

def print_articles(articles):
    print("This data has been written to the file:")
    for name, price in articles.items():
        print(name, ': $', format(price, '.2f'), sep='')

def write_filedata(articles):
    file = open('samplefile.txt', 'a')

    total = 0
    for item, price in articles.items():
        file.write(item + ' ' + format(price, '.2f') + '\n')
        total += price

    file.write('Total sum of all articles = ' + format(total, '.2f') + '\n\n')
    file.close()

def main():
    articles = {'Article1': 4.00, 'Article2': 3.00, 'Article3': 2.00,'Article4': 1.00}
    print_articles(articles)
    write_filedata(articles)

main()
