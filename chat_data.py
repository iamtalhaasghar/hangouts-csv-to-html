import csv

fileString = str()
me = 0
other = 0

with open("chat_data.csv", encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        person = row[0]
        time = row[1]
        message = row[2].strip()
        if(len(message)!=0):
            if(person.startswith('A')):
                fileString += '<p id="other_side"><strong>Unknown</strong><i>'+ time + '</i><br>' + message + "</p>"
                other += 1                
            elif(person.startswith('T')):
                fileString += '<p id="my_side"><strong>Me</strong><i>'+ time + '</i><br>' + message + "</p>"
                me += 1
f = open("data.html",'w', encoding='utf-8')
f.write(fileString)
f.close()
print("Me: ", me)
print("Other: ", other)
