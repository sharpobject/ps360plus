fname = "PS360.tryit.hex"
def real_hex(n):
  s = hex(n)[2:]
  while len(s)<2:
    s = "0"+s
  return s.upper()
with open(fname) as f:
  content = f.readlines()
for line in content:
  stuff = line[1:-4]
  sum = 0
  for i in range(0, len(stuff), 2):
    sum = sum + int(stuff[i:i+2], 16)
  sum = sum & 0xff
  sum = (0x100 - sum) & 0xff
  print ":"+stuff+real_hex(sum)+"\r"
