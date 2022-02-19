with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    list_out = []
    for el in fr:
        remote_addr = el.split(" - - ")[0]
        request_type = el.split('"')[1].split()[0]
        requested_resource = el.split('"')[1].split()[1]
        parse = remote_addr, request_type, requested_resource
        list_out.append(parse)


print(*list_out, sep='\n')
