import csv
a = open("Form.csv",mode="r",encoding='utf-8')
a = csv.reader(a)
next(a)
#6
out = open("out.txt",mode='w',encoding='utf-8')
for row in a :
    q = f'<div class="w3-container"><p class="" style="font-size: 1.5em;"><img src="https://images.unsplash.com/photo-1643446757604-c2b7c45c45dc?" style="width: 1em; height: 1em; vertical-align: baseline; border-radius:100%;">   {row[2]}</p><time class="w3-opacity">{row[0]}</time><h6 class="w3-text-orange"><i class="fa fa-star fa-fw w3-margin-right"></i>{row[3]}/5</h6><p>{row[4]}</p><p><strong>Reviews:</strong><br>{row[5]}</p><hr></div>'
    out.write(q)

out.close()