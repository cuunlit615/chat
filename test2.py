def readfile(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f :
        for line in f:
            lines.append(line.strip())
    return lines
def convert(lines):
    new = []
    person = None
    a_word_count = 0
    a_sticker_count = 0
    a_pic_count = 0
    v_word_count = 0
    v_sticker_count = 0
    v_pic_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                a_sticker_count += 1
            elif s[2] == '圖片':
                a_pic_count += 1
            else:
                for info in s[2:]:
                        a_word_count += len(info)
        elif name == 'Viki':
            if s[2] == '貼圖':
                v_sticker_count += 1
            elif s[2] == '圖片':
                v_pic_count += 1
            else:
                for info in s[2:]:
                        v_word_count += len(info)
    print('Allen', a_word_count)
    print('Viki', v_word_count)

    print('Allen', a_sticker_count)
    print('Viki', v_sticker_count)

    print('Allen', a_pic_count)
    print('Viki', v_pic_count)
def write(filename, lines):
    with open(filename, 'w',  encoding='utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')
def main():
    lines = readfile('LINE-Viki.txt')
    lines = convert(lines)
    # write('output.txt', lines)

main()