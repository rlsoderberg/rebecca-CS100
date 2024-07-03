f = open("img_data.txt", "r", encoding='utf-8')
lines = f.read().splitlines()
f.close

for x in range(0, 200, 5):
  print(lines[x])
  print(lines[x+1])
  print(lines[x+2])
  print(lines[x+3])
  print(lines[x+4])
  print('____________')