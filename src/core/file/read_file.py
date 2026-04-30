
with open("./face.txt","rt") as f:
    for line in f.readlines():
        print(line.strip())

# rt是默认
with open("./face.txt") as f:
    for line in f:
        print(line.strip())

# read(size) size（可选）不指定时，读取所有内容
with open("./face.txt") as f:
    print(f.read())