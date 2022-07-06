import json

# a = {
#     "name": "Dinesh",
#     "Age": "24",
#     "Salary": "25000"
# }
#
# b = json.dumps(a) #Write the file
# print(b)

# file = "F:/apicall/bridgelab/CFP/pythonProject/sample.json"
# new_file = "F:/apicall/bridgelab/CFP/pythonProject/sample1.json"

# f = open(file)
# data = json.load(f)
#
# for i in data['employee']:
#     print(i)

# with open(file, 'r') as fi_file:
#     json_reader = json.load(fi_file)
#     # print(type(json_reader['employee']))   # Find the type of the object
#     # print(json_reader['employee'])  # print the employee object data as a list format
#     # print(json_reader)  # print all the data
#
#     for data in json_reader['employee']:        # python object to json str
#         print(data['id'])
#
# new_str = json.dumps(json_reader, indent=2, sort_keys=True)
# print(new_str)


file = "F:/apicall/bridgelab/CFP/pythonProject/i_o Files/states.json"
new_file = "F:/apicall/bridgelab/CFP/pythonProject/i_o Files/new_states.json"

with open(file, 'r') as f:
    reader = json.load(f)

    for data in reader:
        print(data['name'])

with open(new_file, 'w') as write:
    json.dump(reader, write,indent=4)
