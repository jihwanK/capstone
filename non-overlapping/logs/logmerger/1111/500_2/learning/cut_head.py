def cut(fname):
    w = open('output_headless.txt', 'w') 
    with open(fname, 'r') as read:
        lines = read.readlines()
        for line in lines:
            seg = line.split('\t')
            if seg[1] != '100':
                w.write(line)
    w.close()

cut('output.txt')