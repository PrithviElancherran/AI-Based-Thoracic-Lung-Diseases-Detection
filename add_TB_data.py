from csv import reader

with open('D:\\Downloads\\train.csv', 'r') as read_obj:
    f = []
    d = {}
    csv_reader = reader(read_obj)
    i = 0
    for row in csv_reader:
        if(i == 0):
            i = 1
            continue
        image_id = row[0]
        image_class_id = int(row[2])
        if(image_id not in f):
            f.append(image_id)
            arr = [0] * 16
            arr[image_class_id] = 1
            d[image_id] = arr
        else:
            arr = d[image_id]
            arr[image_class_id] = 1
            d[image_id] = arr
    with open('D:\\Downloads\\t.txt', 'w') as f:
        for key in d:
            value = key + ".jpeg,"
            string = ""
            for i in range(0,15):
                v = str(d[key][i]) + ","
                string += v
            string += str(d[key][15])
            value += string
            f.write(value + "\n")
f.close()