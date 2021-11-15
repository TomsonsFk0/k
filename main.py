def izglitibas_programmas():
    #saruna par izglitibas programmu
    print("programmas coming soon!")
    return 0


def direktori():
    #saruna par v2v direktoriem
    print("direktors coming soon!")
    pass


def tradicijas():
    print("tradicijas coming soon!")
    pass


def skolas_eka():
    print("skolas eka coming soon!")
    pass


def izvelne(vards):
    print(vards + " ,Izvēlies par ko gribi uzzināt!")
    x = input("1-Izglitibas programmas\n2-Direktors\n3-Tradicijas\n4-Skolas eka ")

    lietotaju_izvele=int(x)
    if lietotaju_izvele == 1:
        izglitibas_programmas()
    if lietotaju_izvele == 2:
        direktori()
    if lietotaju_izvele == 3:
        tradicijas()
    if lietotaju_izvele == 4:
        skolas_eka()
        print("laba izvele , kuru tu gribi apskatit?")

def sasveicināties(vards):
    print("Sveiks" + vards)
    izvelne(vards)
    return 0

if __name__ == '__main__':
    print("Sveiki es esmu V2V chatbots Jana! Es tev pastastisu vairak par so skolu")
    vards = input("Kā tevi sauc? ")
    sasveicināties(vards)



