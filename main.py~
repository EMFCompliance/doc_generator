import json
import os 
import inquirer
from colorama import init, Fore 
import re

init(autoreset=True)


'''User input'''

question1 = [
    inquirer.List('keyval',
        message = "Select document category",
        choices = ['HS-100 Environmental Programs',
            'HS-200 OSHA/NIOSH Programs',
            'HS-300 Permit Programs/Guidances',
            'HS-400 Compliance Procedures',
            'HS-500 Operating Procedures',
            'HS-600 Operation and Inspection Records',
            'HS-700 Statistical Systems and Reports',
            'HS-800 Training/Historical Records',
            'HS-900 Audit Checklist'],
            ),
                ]


question2 = [
        inquirer.Text('keyval' , message = "Document name")]



question3 = [
    inquirer.List('keyval',
        message = "Select filetype",
        choices = [' Word (docx)',
            'Excel (xlsx)',
            'Excel w/ VBA (xlsm)',
            'Latex source (tex)'], carousel = True )
        ]




category = inquirer.prompt(question1) #this is a redudancy category['category']
doc_name= inquirer.prompt(question2)
ft = inquirer.prompt(question3)

'''Open json file for reference lookup. Assign new document number'''

with open('registry.json', 'r+') as f:
    data = json.load(f)

'''Unpacking values'''

cat_look_up = category['keyval'][:6].replace('-', '_')

look_up_dict ={ 
        'HS-100 Environmental Programs':0,
        'HS-200 OSHA/NIOSH Programs':1,
        'HS-300 Permit Programs/Guidances':2,
        'HS-400 Compliance Procedures':3,
        'HS-500 Operating Procedures':4,
        'HS-600 Operation and Inspection Records':5,
        'HS-700 Statistical Systems and Reports':6,
        'HS-800 Training/Historical Records':7,
        'HS-900 Audit Checklist':8
            }

'''Traverse JSON and load latest value and increment the value '''

val = data['documents'][look_up_dict[category['keyval'] ]][cat_look_up][-1]['doc_cat']
new_val = int(val[3:]) + 1
new_cat = val[:3] + str(new_val)


'''Append json registery'''

append_val ={"doc_cat": new_cat, "doc_name" :
    doc_name['keyval'], "ft" : ft['keyval']}

with open('registry.json', 'r+') as f:
    data = json.load(f)
    data['documents'][look_up_dict[category['keyval']]][cat_look_up].append(append_val)
    f.seek(0)
    json.dump(data, f, indent =4)
    f.close()

'''Create return value and build the document'''
doc_p1 = new_cat
doc_p2 = doc_name['keyval'].replace(" ", "_")
ft_match = re.search(r'\(((\w+))\)', ft['keyval'])
doc_p3 = ft_match.group(1)
file_name = doc_p1 +"_" +  doc_p2 + "." + doc_p3


'''
data = {}
data['documents'] = []
data['documents'].append({
    "doc_cat": , 
    "doc_name":  ,
    "doc_ft":  
    })

with open('registry.json', 'w') as outfile:
    json.dump(data, outfile)
    '''

target = 'issued_docs/' + file_name
#construct a filename
with open(target, 'w') as f:
    f.write("")
    f.close
print(Fore.CYAN+ file_name + " has been created in \n" +Fore.YELLOW+ target)
#push to with open in the target folder
