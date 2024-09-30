def readfile(filename):#讀檔
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f :
        for line in f:
            lines.append(line.strip())#將檔案內容竹行加至lines列表
    return lines
def convert(lines):#句子轉換
    new = []
    person = None
    for line in lines:
        if line == 'Allen':#如果該行為Allen，將 Allen 存入 person
            person = 'Allen'
            continue
        elif line == 'Tom':#如果該行為Tom，將 Tom 存入 person
            person = 'Tom'
            continue
        if person:#如果person == True
            new.append(person + ':' + line)#new列表添加person:line
    return new
def write(filename, lines):#寫入
    with open(filename, 'w',  encoding='utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')
def main():
    lines = readfile('input.txt')#讀檔+定義lines
    lines = convert(lines)#lines轉換
    write('output.txt', lines)#寫入

main()
