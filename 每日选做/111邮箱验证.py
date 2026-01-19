while True:
    try:
        email=input().strip()
        if not email:
            continue
        if email.count('@') != 1:
            print('NO')
            continue
        if email[0] in ['@', '.'] or email[-1] in ['@', '.']: #*in的用法，用于检查某位是否是某些元素
            print('NO')
            continue
        index=email.index('@')
        domain=email[index + 1:]
        if '.' not in domain:
            print('NO')
            continue
        if '@.' in email or '.@' in email:
            print('NO')
            continue
        print('YES')
    except EOFError:
        break