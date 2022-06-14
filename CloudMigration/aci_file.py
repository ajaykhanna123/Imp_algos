triggers_json = {"values": [{"filename": "rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json0-10"},
                            {"filename": "rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json10-20"},
                            {"filename": "rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json100-110"},
                            {"filename": "rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json110-120"},
                            {"filename": "rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json120-130"},
                            {"filename": "rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json130-137"},
                            {"filename": "rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json20-30"},
                            {"filename": "rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json30-40"},
                            {"filename": "rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json40-50"},
                            {"filename": "rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json50-60"},
                            {"filename": "rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json60-70"},
                            {"filename": "rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json70-80"},
                            {"filename": "rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json80-90"},
                            {"filename": "rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json90-100"}]}
list_of_files = [i['filename'] for i in triggers_json["values"]]
print("list of total files", len(list_of_files))
temp = list_of_files
REQUIRED_ACI_ACTIVE_NUMBER = 5
active_aci = REQUIRED_ACI_ACTIVE_NUMBER


def aci_not_killed_list():
    aci_not_killed = [1]
    if len(aci_not_killed) > 0:
        print(len(aci_not_killed), "are not killed")
    return aci_not_killed


def read_files_and_invoke_aci_parallel(files_list):
    print("read and invoked", len(files_list), "number of acis")


def pop_multiple_items_list(temp_list, no_of_pop_items):
    for _ in range(no_of_pop_items):
        temp_list.pop(0)
    return temp_list


while len(temp) > 0:

    aci_not_killed = aci_not_killed_list()

    if len(aci_not_killed) != 0:
        active_aci -= len(aci_not_killed)
    else:
        active_aci = REQUIRED_ACI_ACTIVE_NUMBER
    if active_aci < 0:
        break

    if len(temp) < active_aci:
        read_files_and_invoke_aci_parallel(temp[0:len(temp)])

        no_of_pop_items = len(temp)
        temp = pop_multiple_items_list(temp, no_of_pop_items)

    else:
        read_files_and_invoke_aci_parallel(temp[0:active_aci])
        no_of_pop_items = active_aci
        temp = pop_multiple_items_list(temp, no_of_pop_items)

    active_aci = REQUIRED_ACI_ACTIVE_NUMBER