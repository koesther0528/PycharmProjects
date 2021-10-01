print('전체 한꺼번에 읽기')
f = open('text.txt', 'r', encoding='utf-8')
data = f.read()
f.close()
print(data)

print('한줄 씩 읽기')
f = open('text.txt', 'r', encoding='utf-8')
while True:
    line = f.readline()
    if line == '':
        break
    print(line.rstrip())

f.close()

print('전체를 한꺼번에 읽고, 줄 별로 리스트')
f = open('text.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()
for line in lines:
    print(line.rstrip())

f = open('text.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()
for line in lines:
    print('이름:'+ line.rstrip()[:3]+"\t좋아하는 색:" + line.rstrip()[4:])
    
f = open('text.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()
for line in lines:
    data = line.split(':')