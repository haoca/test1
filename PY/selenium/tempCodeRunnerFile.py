def readfile():

    try:
        f = open("foo.ini", "r+")
        for line in f:
            accout_id = line.find('用户名为:')
            pass_id = line.find('密码为:')
            # final_id = line.find('吧')
            # print(final_id)
            # print(line)

            if accout_id != -1:
                name_1 = line[5:-1]
            if pass_id != -1:
                password2 = line[4:-1]

        e1.insert('insert', name_1)
        e2.insert('insert', password2)

    # print(name_1, password2)
    # print(s)

    # print(sin)
        f.close()
    except:
        pass