# dict

ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 12,
    }, {
        "name": "petja",
        "age": 115,
    }],
}

darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 21,
    }, {
        "name": "pavel",
        "age": 15,
    }],
}

employees = [ivan, darja]


def check_age(children):
    for child in children:
        if child['age'] > 18:
            return True
    return False


def test(employees):
    result = []
    for emp in employees:
        if check_age(emp['children']):
            result.append(emp['name'])
            #   return result4
    return result


#      print("Работники с детьми старше 18: ", emp['name'], " ")

print(test(employees))