from docxtpl import DocxTemplate
import csv
import json
with open('vw_data', 'r') as f:
    list_vw_data = f.read()
a = ','
list_vw_data = list_vw_data.replace(', ',a)
list_vw_data = list_vw_data.split(',')
list_vw_data = list(list_vw_data)
marka = list_vw_data[0]
model = list_vw_data[1]
transmission = list_vw_data[2]
engine_volume = list_vw_data[3]
price = list_vw_data[4]


def get_context(marka, model, transmission, engine_volume, price):
    return {'марка': marka, 'модель': model, 'трансмиссия': transmission, 'Объем двигателя': engine_volume, 'цена': price}

def from_template(marka, model, transmission, engine_volume, price, template):
    template = DocxTemplate(template)
    context = get_context(marka, model, transmission, engine_volume, price)
    template.render(context)
    template.save(marka + '_report.doсх')


def generate_report(marka, model, transmission, engine_volume, price):
    template = 'vw.docx'
    document = from_template(marka, model, transmission, engine_volume, price, template)
generate_report(marka, model, transmission, engine_volume, price)

list_1 = [['car', 'model', 'transmission', 'engine_volume','price'],['Volkswagen','Tuareg', 'Mechanics', 2.5, 2200000]]

with open('vw_car.csv', 'w') as f:
    writer = csv.writer(f, delimiter = '&')
    writer.writerows(list_1)

with open('vw_car.csv') as m:
    reader = csv.reader(m, delimiter = '&')
    for row in reader:
        print(row)

dict = {'car' : 'Volkswagen', 'model' : 'Tuareg', 'transmission': 'Mechanics', 'engine_volume': 2.5, 'price' : 2200000}

with open('dict_to_json.txt', 'w') as f:
    json.dump(dict, f)

with open('dict_to_json.txt') as f:
    data = json.load(f)
    print(data)
