from fastapi import FastAPI  
import json
with open('pokemons.json', mode='r') as f:
    pokemons = json.load(f)
with open('stats.json', mode='r') as f:
    stats = json.load(f)
with open('battleitems.json', mode='r') as f:
    battleitems = json.load(f)
with open('helditems.json', mode='r') as f:
    helditems = json.load(f)    
with open('pokemondb.json', mode='r') as f:
    pokemondb = json.load(f)    
app = FastAPI()

@app.get("/")
def index():
    return {"api using mostly unite-db data by misi. https://docs.google.com/spreadsheets/d/e/2PACX-1vRIQuAeoMeineAU1a9x9iMslVAagBctoxeQBGiBp3I8DvqhftUOpOtVytoVZ1ukcOBp-30w2KD_M5c0/pubhtml"}

@app.get("/pokemons")
def getPkm():
    #return [i["name"] for (j, i) in enumerate(pokemons) if j % 2 == 0]
    return [i["name"] for i in pokemons]

def getPokemonFromPokemons(name: str) -> list:
    for i in pokemons:
        if name.lower() == i.get('name').lower():
            return i 
    return None

def getPokemonFromPokemondb(name: str) -> list:
    for i in pokemondb:
        if name.lower() == i.get('name').lower():
            return i 
    return None

@app.get("/pokemondb")
def getPkmdb():
    return [i["name"] for i in pokemons]

@app.get("/pokemondb/{name}/ratio")
def getRatio(name: str, move, add: int =0):
    result = getPokemonFromPokemondb(name)
    if result is None:
        return f"Error : {name} isn't available"
    if int(add) != 0:
        return result["skills"][int(move)]["rsb"]["add" + str(add) + "_ratio"]
    return result["skills"][int(move)]["rsb"]["ratio"]

@app.get("/pokemondb/{name}/moveupgrades/ratio")
def getUpgradeRatio(name: str, move, upgrade, add: int=0):
    result = getPokemonFromPokemondb(name)
    if result is None:
        return f"Error : {name} isn't available"
    if int(add) != 0:
        return result["skills"][int(move)]["upgrades"][int(upgrade)]["rsb"]["add" + str(add) + "_ratio"]  
    return result["skills"][int(move)]["upgrades"][int(upgrade)]["rsb"]["ratio"]

@app.get("/pokemondb/{name}/moveupgrades/ratio/enhanced")
def getUpgradeRatioEnhanced(name: str, move, upgrade, add: int=0):
    result = getPokemonFromPokemondb(name)
    if result is None:
        return f"Error : {name} isn't available"
    if int(add) != 0:
        return result["skills"][int(move)]["upgrades"][int(upgrade)]["rsb"]["add" + str(add) + "_enhanced_ratio"]  
    return result["skills"][int(move)]["upgrades"][int(upgrade)]["rsb"]["enhanced_ratio"]

@app.get("/pokemondb/{name}/base")
def getBase(name: str, move, add: int=0):
    result = getPokemonFromPokemondb(name)
    if result is None:
        return f"Error : {name} isn't available"
    if int(add) != 0:
        return result["skills"][int(move)]["rsb"]["add" + str(add) + "_base"]  
    return result["skills"][int(move)]["rsb"]["base"]

@app.get("/pokemondb/{name}/moveupgrades/base")
def getUpgradeBase(name: str, move, upgrade, add: int=0):
    result = getPokemonFromPokemondb(name)
    if result is None:
        return f"Error : {name} isn't available"
    if int(add) != 0:
        return result["skills"][int(move)]["upgrades"][int(upgrade)]["rsb"]["add" + str(add) + "_base"]  
    return result["skills"][int(move)]["upgrades"][int(upgrade)]["rsb"]["base"]

@app.get("/pokemondb/{name}/moveupgrades/base/enhanced")
def getUpgradeBaseEnhanced(name: str, move, upgrade, add: int=0):
    result = getPokemonFromPokemondb(name)
    if result is None:
        return f"Error : {name} isn't available"
    if int(add) != 0:
        return result["skills"][int(move)]["upgrades"][int(upgrade)]["rsb"]["add" + str(add) + "_enhanced_base"]  
    return result["skills"][int(move)]["upgrades"][int(upgrade)]["rsb"]["enhanced_base"]

@app.get("/pokemondb/{name}/slider")
def getSlider(name: str, move, add: int=0):
    result = getPokemonFromPokemondb(name)
    if result is None:
        return f"Error : {name} isn't available"
    if int(add) != 0:
        return result["skills"][int(move)]["rsb"]["add" + str(add) + "_slider"]  
    return result["skills"][int(move)]["rsb"]["slider"]

@app.get("/pokemondb/{name}/moveupgrades/slider")
def getUpgradeSlider(name: str, move, upgrade, add: int=0):
    result = getPokemonFromPokemondb(name)
    if result is None:
        return f"Error : {name} isn't available"
    if int(add) != 0:
        return result["skills"][int(move)]["upgrades"][int(upgrade)]["rsb"]["add" + str(add) + "_slider"] 
    return result["skills"][int(move)]["upgrades"][int(upgrade)]["rsb"]["slider"]

@app.get("/pokemondb/{name}/moveupgrades/slider/enhanced")
def getUpgradeSliderEnhanced(name: str, move, upgrade, add: int=0):
    result = getPokemonFromPokemondb(name)
    if result is None:
        return f"Error : {name} isn't available"
    if int(add) != 0:
        return result["skills"][int(move)]["upgrades"][int(upgrade)]["rsb"]["add" + str(add) + "_enhanced_slider"] 
    return result["skills"][int(move)]["upgrades"][int(upgrade)]["rsb"]["enhanced_slider"]

@app.get("/pokemons/stats")
def getStats():
    return [i["level"] for i in stats]

def getPokemonFromStats(name: str) -> list:
    for i in stats:
        if name.lower() == i.get('name').lower():
            return i 
    return None

@app.get("/battleitems")
def getBattleitems():
    return [i["display_name"] for i in battleitems]

def getItemFromBattleitems(name: str) -> list:
    for i in battleitems:
        if name.lower() == i.get('name').lower():
            return i 
    return None

@app.get("/battleitems/{name}")
def getBattleitemName(name: str):
    result = getItemFromBattleitems(name)
    if result is None:
        return f"Error : {name} isn't available"
    return result

@app.get("/battleitems/{name}/description")
def getBattleitemDesc(name: str):
    result = getItemFromBattleitems(name)
    if result is None:
        return f"Error : {name} isn't available"
    return result["description"]

@app.get("/battleitems/{name}/cooldown")
def getBattleitemCd(name: str):
    result = getItemFromBattleitems(name)
    if result is None:
        return f"Error : {name} isn't available"
    return result["cooldown"]

@app.get("/battleitems/{name}/unlocklevel")
def getBattleitemUnlock(name: str):
    result = getItemFromBattleitems(name)
    if result is None:
        return f"Error : {name} isn't available"
    return result["unlocklevel"]

@app.get("/battleitems/{name}/image")
def getBattleitemImage(name: str):
    result = getItemFromBattleitems(name)
    if result is None:
        return f"Error : {name} isn't available"
    return result["image"]

@app.get("/helditems")
def getHelditems():
    return [i["display_name"] for i in helditems]

def getItemFromHelditems(name: str) -> list:
    for i in helditems:
        if name.lower() == i.get('name').lower():
            return i 
    return None

@app.get("/helditems/{name}")
def getHelditemName(name: str):
    result = getItemFromHelditems(name)
    if result is None:
        return f"Error : {name} isn't available"
    return result

@app.get("/helditems/{name}/bonus")
def getHelditemName(name: str):
    result = getItemFromHelditems(name)
    if result is None:
        return f"Error : {name} isn't available"
    return str(result["bonus1"]) + " " + str(result["bonus2"]) + " " + str(result["bonus3"])

@app.get("/helditems/{name}/desc")
def getHelditemName(name: str):
    result = getItemFromHelditems(name)
    if result is None:
        return f"Error : {name} isn't available"
    return str(result["description1"])
    
@app.get("/helditems/{name}/image")
def getHelditemName(name: str):
    result = getItemFromHelditems(name)
    if result is None:
        return f"Error : {name} isn't available"
    return str(result["image"])

def getPokemonFromPokemons(name: str) -> list:
    for i in pokemons:
        if name.lower() == i.get('name').lower():
            return i 
    return None

@app.get("/pokemons/{name}")
def getPokemon(name: str):
    result = getPokemonFromPokemons(name)
    if result is None:
        return f"Error : {name} isn't available"
    return result

@app.get("/pokemons/{name}/moves")
def getPokemonMove(name: str, move: int =None):
    result = getPokemonFromPokemons(name)
    if result is None:
        return f"Error : {name} isn't available"
    if move is None:
        return result["move"]
    if move > 8:
        return f"Error : This isn't an available move"
    return result["move"][move]

@app.get("/pokemons/{name}/moves/cd")
def getPokemonMove(name: str, movecd: int =None):
    result = getPokemonFromPokemons(name)
    if result is None:
        return f"Error : {name} isn't available"
    if movecd is None:
        return result["movecd"]
    if movecd > 8:
        return f"Error : This isn't an available move"
    return result["movecd"][movecd]

@app.get("/pokemons/{name}/moves/desc")
def getPokemonMoveDesc(name: str, movedesc: int =None):
    result = getPokemonFromPokemons(name)
    if result is None:
        return f"Error : {name} isn't available"
    if movedesc is None:
        return result["movedesc"]
    if int(movedesc) > 11:
        return f"Error : This isn't an available description"
    return result["movedesc"][movedesc]

@app.get("/pokemons/{name}/moves/rsb")
def getPokemonMoveRsb(name: str, move: int =None):
    result = getPokemonFromPokemons(name)
    if result is None:
        return f"Error : {name} isn't available"
    if move is None:
        return result["moversb"]
    if int(move) > 11:
        return f"Error : This isn't an available description"
    return result["moversb"][move]

@app.get("/pokemons/{name}/moves/icons")
def getPokemonIcon(name: str, move: int =None):
    result = getPokemonFromPokemons(name)
    if result is None:
        return f"Error : {name} isn't available"
    if move is None:
        return result["moveicon"]
    if int(move) > 11:
        return f"Error : This isn't an available description"
    return result["moveicon"][move]

@app.get("/pokemons/{name}/class")
def getPokemonMoveClass(name: str):
    result = getPokemonFromPokemons(name)
    if result is None:
        return f"Error : {name} isn't available"
    return result["class"]
    
@app.get("/pokemons/{name}/stat")
def getPokemonStat(name: str, level: int =None):
    result = getPokemonFromStats(name)
    if result is None:
        return f"Error : {name} isn't available"
    if level is None:
        return result
    if int(level) > 15:
        return f"Error : This isn't an available level"
    return result["level"][int(level)-1]

@app.get("/pokemons/{name}/stat/hp")
def getPokemonStatHP(name: str, level: int =None):
    result = getPokemonFromStats(name)
    if result is None:
        return f"Error : {name} isn't available"
    if level is None:
        return [result["level"][int(i)]["hp"] for i in range(0,15)]
    if int(level) > 15:
        return f"Error : This isn't an available level"
    return result["level"][int(level)-1]["hp"]
    
@app.get("/pokemons/{name}/stat/attack")
def getPokemonStatAtk(name: str, level: int =None):
    result = getPokemonFromStats(name)
    if result is None:
        return f"Error : {name} isn't available"
    if level is None:
        return [result["level"][int(i)]["attack"] for i in range(0,15)]
    if int(level) > 15:
        return f"Error : This isn't an available level"
    return result["level"][int(level)-1]["attack"]

@app.get("/pokemons/{name}/stat/defense")
def getPokemonStatDef(name: str, level: int =None):
    result = getPokemonFromStats(name)
    if result is None:
        return f"Error : {name} isn't available"
    if level is None:
        return [result["level"][int(i)]["defense"] for i in range(0,15)]
    if int(level) > 15:
        return f"Error : This isn't an available level"
    return result["level"][int(level)-1]["defense"]

@app.get("/pokemons/{name}/stat/sp_attack")
def getPokemonStatSpa(name: str, level: int =None):
    result = getPokemonFromStats(name)
    if result is None:
        return f"Error : {name} isn't available"
    if level is None:
        return [result["level"][int(i)]["sp_attack"] for i in range(0,15)]
    if int(level) > 15:
        return f"Error : This isn't an available level"
    return result["level"][int(level)-1]["sp_attack"]

@app.get("/pokemons/{name}/stat/sp_defense")
def getPokemonStatSpd(name: str, level: int =None):
    result = getPokemonFromStats(name)
    if result is None:
        return f"Error : {name} isn't available"
    if level is None:
        return [result["level"][int(i)]["sp_defense"] for i in range(0,15)]
    if int(level) > 15:
        return f"Error : This isn't an available level"
    return result["level"][int(level)-1]["sp_defense"]

@app.get("/pokemons/{name}/stat/crit")
def getPokemonStatCrit(name: str, level: int =None):
    result = getPokemonFromStats(name)
    if result is None:
        return f"Error : {name} isn't available"
    if level is None:
        return [result["level"][int(i)]["crit"] for i in range(0,15)]
    if int(level) > 15:
        return f"Error : This isn't an available level"
    return str(result["level"][int(level)-1]["crit"]) + "%"

@app.get("/pokemons/{name}/stat/cdr")
def getPokemonStatCDR(name: str, level: int =None):
    result = getPokemonFromStats(name)
    if result is None:
        return f"Error : {name} isn't available"
    if level is None:
        return [result["level"][int(i)]["cdr"] for i in range(0,15)]
    if int(level) > 15:
        return f"Error : This isn't an available level"
    return str(result["level"][int(level)-1]["cdr"]) + "%"

@app.get("/pokemons/{name}/stat/lifesteal")
def getPokemonStatLifesteal(name: str, level: int =None):
    result = getPokemonFromStats(name)
    if result is None:
        return f"Error : {name} isn't available"
    if level is None:
        return [result["level"][int(i)]["lifesteal"] for i in range(0,15)]
    if int(level) > 15:
        return f"Error : This isn't an available level"
    return str(result["level"][int(level)-1]["lifesteal"]) + "%"
