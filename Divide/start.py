from see import fisier

Setting= "settingsCVS.properties"

def readSettings():
    f = open(Setting,"r")
    lines = f.read().split("\n")
    settings = {}
    for line in lines:
        setting = line.split("=")
        if len(line) >1:
            settings[setting[0]]=setting[1]
    f.close()
    return settings

if "CSV"==setting["repo"]
    clasa = fisier()
