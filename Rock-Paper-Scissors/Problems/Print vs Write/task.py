numbers = [1234, 5678, 90]
# save this list in `file_with_list.txt`
fout = open('file_with_list.txt', mode='w', encoding='utf-8')
fout.write(str(numbers))
fout.close()
