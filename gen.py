# To execute, run py gen.py from the command line

import json
import os

fd = open("index.html","w")
fs = open('TheoryTest.json',)

h = open("header.html")
header = h.read()
h.close()

f = open("footer.html")
footer = f.read()
f.close()

data = json.load(fs)
fs.close()

fd.write(header)

fd.write(f'''
  <div class="title-block">
    <h1>{data["Document"]["Title"]}</h1>
    <h2>{data["Document"]["Subtitle"]}</h2>
    <h3>{data["Document"]["Date"]}</h3>
    <h4>{data["Document"]["Author"]}</h4>
  </div>
''')

fd.write (
  '''
  <div class="card">
      <div class="card-body">
        <h4 class="card-title">Notes</h4>
  '''
)

for n in data['Notes']:
  card = f'<p class="card-text">{n}</p>'
  fd.write(card + "\n")

fd.write('</div></div>')

n=1
for i in data['stuff']:
  question = str(n) + ". " + i["Question"]
  answer = i["Answer"]
  card = f'''
    <div class="card">
      <div class="card-body">
        <h4 class="card-title">{question}</h4>
        <p class="card-text">{answer}</p>
      </div>
    </div>
  '''
  fd.write(card + "\n")
  n += 1

fd.write(footer)
fd.close()

print("All done.")

# aws s3 cp index.html s3://tt.osirl.com/ --acl public-read

result = os.system("aws s3 cp index.html s3://tt.osirl.com/ --acl public-read")
print(result)
