
def sasveicinaties(vards):
    print("Sveiks " + vards)
    izvelne(vards)
    return 0


def sports():
    print("Ja, v2v skola ir sporta un veselibas grozs")


def programma():
    print("Ja , v2v skola ir programmetaju virzeins, ja tev loti paitk , var nak!")


def izglitibas_programmas():
    #saruna par izglitibas programmu
    print("programmas coming soon!")
    izvele=input("1-Vai v2v skola ir sprota un veselibu grozs?\n2-Vai ir iespejams macities par programetaju v2v skola?")
    lietotaju_izvele = int(izvele)
    if lietotaju_izvele == 1:
        sports()
    if lietotaju_izvele == 2:
        programma()

def cik_direktoru():
    print("Vjačeslavs Piskunovs")


def pir_direktors():
    print("Vinu sauc Andrejs Gluhovs")



def direktori():
    #saruna par v2v direktoriem
    print("Ko jus gribat uzinat?")
    izvele= input("1-Kā sauc direktora vietnieku?\n2-Kas ir pasreizejais direktors v2v skola?")
    lietotaju_izvele = int(izvele)
    if lietotaju_izvele == 1:
        cik_direktoru()
    if lietotaju_izvele == 2:
        pir_direktors()


def zinibu():
    print("zinibu diena ir pirmie svetki ,kas notike pec vasaras brivlaika")


def trad():
    print("Kopumā v2v ir 21 svetki, kas skaitas ka tradicijas")


def tradicijas():
    print("Ko jus gribat uzinat par tradicijam?")
    izvele = input("1-Kas ir pirmie svetkie skolas saksana?\n2-Cik tradicijas ir saja skola?")
    lietotaju_izvele = int(izvele)
    if lietotaju_izvele == 1:
        trad()
    if lietotaju_izvele == 2:
        zinibu()

def skolas_eka():
    print("Kuru jus gribetu uzinat?")
    izvele= input("1-Skolas klases\n2-Kafejnica\n3-Toletes\n4-Aktu zale")
    lietotaju_izvele = int(izvele)
    if lietotaju_izvele == 1:
        skolas_klases()
    if lietotaju_izvele == 2:
        kafejnica()
    if lietotaju_izvele == 3:
        toletes()
    if lietotaju_izvele == 4:
        aktu_zale()


def kafejnica():
    print("Musu kafejnicai ir notiekti edieni katru dienu ir daudz")
    pass

def toletes ():
    print("Musu toletes nav tas labakas un nav sliktakas, tas ir toletes")


def aktu_zale():
    print("Aktu zale mums parasti ir ceremonijas un mentoru stundas un ,ja ir balles tad mums tur vinas norisinas")


def skolas_klases():
    print("Musu klases ir jaunas un ar daudz vietam , datorikas klase ari ir atjauninata ar jauniem datoriem un monitoriem")

def sasveicinaties(vards):
    print("Sveiks " + vards)
    izvelne(vards)

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

if __name__ == '__main__':
    print("Sveiki es esmu V2V chatbots Jana! Es tev pastastisu vairak par so skolu")
    vards = input("Kā tevi sauc? ")
    sasveicinaties(vards)
    exit(0)
