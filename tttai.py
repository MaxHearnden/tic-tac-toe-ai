def ttt():
    states={}
    state=[[0,0,0],[0,0,0],[0,0,0]]
    stat=[]
    def repopulate():
        states[bytes(state)]+=[1,2,3,4,5,6,7,8,9]*3
    def open_box():
        if not states[bytes(state)]:
            repopulate()
        go=random.choice(states[bytes(state)])
        while not islegal(go):
            go=random.choise(states[bytes(state)])
        stat.append([state,go])
        return go
    def update():
        for i in stat:
            states[bytes(i[0])].remove(i[1])
    while not win(state):
        inp=yield
        if inp ==0:
            inp=yield open_box()
