def formatter(response): 
    # removing spacing and new lines
    rl = response.split('/n')
    for i in list(rl): 
        if i == ' ': rl.remove(' ')
    print(rl)
    # printing worksheet
    print('Questions ')
    for i in range(0, len(rl), 2): 
        print(rl[i])
    print('Answers: ')
    for i in range(1, len(rl), 2): 
        print(rl[i])
