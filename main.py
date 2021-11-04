from fastapi import FastAPI  
import json
with open('pokemons.json', mode='r') as f:
    pokemons = json.load(f)
with open('stats.json', mode='r') as f:
    stats = json.load(f)
with open('battleitems.json', mode='r') as f:
    battleitems = json.load(f)    
app = FastAPI()

@app.get("/")
def index():
    return {"Paths : /pokemons, /pokemon, /items, /item"}

@app.get("/pokemons")
def getPkm():
    #return [i["name"] for (j, i) in enumerate(pokemons) if j % 2 == 0]
    return [i["name"] for i in pokemons]

def getPokemonFromPokemons(name: str) -> list:
    for i in pokemons:
        if name.lower() == i.get('name').lower():
            return i 
    return None

@app.get("/pokemons/stats")
def getPkm():
    return [i["level"] for i in stats]

def getPokemonFromStats(name: str) -> list:
    for i in stats:
        if name.lower() == i.get('name').lower():
            return i 
    return None

@app.get("/battleitems")
def getPkm():
    return [i["display_name"] for i in battleitems]

def getItemFromBattleitems(name: str) -> list:
    for i in battleitems:
        if name.lower() == i.get('name').lower():
            return i 
    return None

@app.get("/battleitems/{name}")
def getPokemon(name: str):
    result = getItemFromBattleitems(name)
    if result is None:
        return f"Error : {name} isn't available"
    return result

@app.get("/battleitems/{name}/description")
def getPokemon(name: str):
    result = getItemFromBattleitems(name)
    if result is None:
        return f"Error : {name} isn't available"
    return result["description"]

@app.get("/battleitems/{name}/cooldown")
def getPokemon(name: str):
    result = getItemFromBattleitems(name)
    if result is None:
        return f"Error : {name} isn't available"
    return result["cooldown"]

@app.get("/battleitems/{name}/unlocklevel")
def getPokemon(name: str):
    result = getItemFromBattleitems(name)
    if result is None:
        return f"Error : {name} isn't available"
    return result["unlocklevel"]

@app.get("/battleitems/{name}/image")
def getPokemon(name: str):
    result = getItemFromBattleitems(name)
    if result is None:
        return f"Error : {name} isn't available"
    return result["image"]

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
def getPokemonStatHP(name: str, level: int =None):
    result = getPokemonFromStats(name)
    if result is None:
        return f"Error : {name} isn't available"
    if level is None:
        return [result["level"][int(i)]["attack"] for i in range(0,15)]
    if int(level) > 15:
        return f"Error : This isn't an available level"
    return result["level"][int(level)-1]["attack"]

@app.get("/pokemons/{name}/stat/defense")
def getPokemonStatHP(name: str, level: int =None):
    result = getPokemonFromStats(name)
    if result is None:
        return f"Error : {name} isn't available"
    if level is None:
        return [result["level"][int(i)]["defense"] for i in range(0,15)]
    if int(level) > 15:
        return f"Error : This isn't an available level"
    return result["level"][int(level)-1]["defense"]

@app.get("/pokemons/{name}/stat/sp_attack")
def getPokemonStatHP(name: str, level: int =None):
    result = getPokemonFromStats(name)
    if result is None:
        return f"Error : {name} isn't available"
    if level is None:
        return [result["level"][int(i)]["sp_attack"] for i in range(0,15)]
    if int(level) > 15:
        return f"Error : This isn't an available level"
    return result["level"][int(level)-1]["sp_attack"]

@app.get("/pokemons/{name}/stat/sp_defense")
def getPokemonStatHP(name: str, level: int =None):
    result = getPokemonFromStats(name)
    if result is None:
        return f"Error : {name} isn't available"
    if level is None:
        return [result["level"][int(i)]["sp_defense"] for i in range(0,15)]
    if int(level) > 15:
        return f"Error : This isn't an available level"
    return result["level"][int(level)-1]["sp_defense"]

@app.get("/pokemons/{name}/stat/crit")
def getPokemonStatHP(name: str, level: int =None):
    result = getPokemonFromStats(name)
    if result is None:
        return f"Error : {name} isn't available"
    if level is None:
        return [result["level"][int(i)]["crit"] for i in range(0,15)]
    if int(level) > 15:
        return f"Error : This isn't an available level"
    return str(result["level"][int(level)-1]["crit"]) + "%"

@app.get("/pokemons/{name}/stat/cdr")
def getPokemonStatHP(name: str, level: int =None):
    result = getPokemonFromStats(name)
    if result is None:
        return f"Error : {name} isn't available"
    if level is None:
        return [result["level"][int(i)]["cdr"] for i in range(0,15)]
    if int(level) > 15:
        return f"Error : This isn't an available level"
    return str(result["level"][int(level)-1]["cdr"]) + "%"

@app.get("/pokemons/{name}/stat/lifesteal")
def getPokemonStatHP(name: str, level: int =None):
    result = getPokemonFromStats(name)
    if result is None:
        return f"Error : {name} isn't available"
    if level is None:
        return [result["level"][int(i)]["lifesteal"] for i in range(0,15)]
    if int(level) > 15:
        return f"Error : This isn't an available level"
    return str(result["level"][int(level)-1]["lifesteal"]) + "%"
