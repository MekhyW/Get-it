import json

def extract_route(request):
    route = request.split()[1][1:]
    print('*'*100 + '\n' + request + '\n' + route)
    return route

def read_file(filepath):
    file = open(filepath, 'rb')
    content = file.read()
    file.close()
    return content

def load_data(jsonpath):
    with open(jsonpath, encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data

def load_template(templatepath):
    with open(templatepath, encoding="utf-8") as template_file:
        template = template_file.read()
    template_file.close()
    return template

def build_response(body='', code=200, reason='OK', headers=''):
    response = f'HTTP/1.1 {code} {reason}\n'
    response += headers
    response += '\n'
    response += body
    return response.encode()