#==============================tavabe==================================
def moh_dayereh(ghotr):
    return (ghotr*3.14)
def ma_sahat_dayereh(ghotr):
    shoa=ghotr/2
    return (shoa*shoa*3.14)

def ma_sahat_moraba(zel):
    return zel*zel
def moh_moraba(zel):
    return zel*4

def moh_mostatil(tool,arz):
    return (tool+arz)*2
def ma_sahat_mostatil(tool,arz):
    return (tool*arz)

def moh_mosalas(ghaedeh,ertefa):
    return (ghaedeh+ghaedeh+ghaedeh)
def ma_sahat_mosalas(ghaedeh,ertefa):
    return (ghaedeh*ertefa/2)


#=======================================================================
shape="true"
while shape:
    shekl=input("Lotfan shomareh shekl ra entekhab konid \n 1>dayereh 2>moraba 3>mostatil 4>mosalas ya q baray khorouj")
    if shekl=="q":
        break
    else:
        if shekl=="dayereh":
            ghotr=float(input("Lotfan ghotr ra vared konid\n"))
            kar=input("mohit ya masahat? \n 1>mohit     2>masahat")
            if kar=="mohit":
                out=moh_dayereh(ghotr)
                print(f"mohit dayerh={out}")
            elif kar=="masahat":
                out=ma_sahat_dayereh(ghotr)
                print(f"masahat dayerh={out}")

        if shekl=="moraba":
            zel=float(input("Lotfan zel ra vared koni\n"))
            kar=input("mohit ya masahat? \n 1>mohit     2>masahat\n")
            if kar=="mohit":
                out=moh_moraba(zel)
                print(f"mohit moraba={out}")
            elif kar=="masahat":
                out=ma_sahat_moraba(zel)
                print(f"masahat moraba={out}")



        if shekl=="mostatil":
            tool=float (input("Lotfan tool  ra vared konid\n"))
            arz=float (input("Lotfan arz  ra vared konid\n"))
            kar=input("mohit ya masahat? \n 1>mohit     2>masahat\n")
            if kar=="mohit":
                out=moh_mostatil(tool,arz)
                print(f"mohit moraba={out}")
            elif kar=="masahat":
                out=ma_sahat_mostatil(tool,arz)
                print(f"masahat mostatil={out}")

        if shekl=="mosalas":
            ghaedeh=float(input("Lotfan ghaedeh  ra vared konid\n"))
            ertefa=float(input("Lotfan ertefa  ra vared konid\n"))
            kar=input("mohit ya masahat? \n 1>mohit     2>masahat\n")
            if kar=="mohit":
                out=moh_mosalas(ghaedeh,ertefa)
                print(f"mohit mosalas={out}")
            elif kar=="masahat":
                out=ma_sahat_mosalas(ghaedeh,ertefa)
                print(f"masahat mostatil={out}")
