import itertools
from cc1_levelset_pb2 import CC1TileCode

# Utils for CC1TileCode enum
class CC1TileCodes:
    ICE = {CC1TileCode.Value(s) for s in ("ICE", "ICE_NW", "ICE_NE", "ICE_SW", "ICE_SE")}
    WALLS = {CC1TileCode.Value(s) for s in ("WALL", "INV_WALL_PERM", "INV_WALL_APP", "BLUE_WALL_REAL")}
    PANELS = {CC1TileCode.Value(s) for s in ("PANEL_SE", "PANEL_N", "PANEL_E", "PANEL_S", "PANEL_W")}
    CLONE_BLOCKS = {CC1TileCode.Value(s) for s in tuple(f"CLONE_BLOCK_{d}" for d in "NESW")}
    BLOCKS = CLONE_BLOCKS.union(set((CC1TileCode.BLOCK,)))
    PLAYERS = {CC1TileCode.Value(s) for s in tuple(f"PLAYER_{d}" for d in "NESW")}
    ANTS = {CC1TileCode.Value(s) for s in tuple(f"ANT_{d}" for d in "NESW")}
    PARAMECIA = {CC1TileCode.Value(s) for s in tuple(f"PARAMECIUM_{d}" for d in "NESW")}
    GLIDERS = {CC1TileCode.Value(s) for s in tuple(f"GLIDER_{d}" for d in "NESW")}
    FIREBALLS = {CC1TileCode.Value(s) for s in tuple(f"FIREBALL_{d}" for d in "NESW")}
    TANKS = {CC1TileCode.Value(s) for s in tuple(f"TANK_{d}" for d in "NESW")}
    BALLS = {CC1TileCode.Value(s) for s in tuple(f"BALL_{d}" for d in "NESW")}
    WALKERS = {CC1TileCode.Value(s) for s in tuple(f"WALKER_{d}" for d in "NESW")}
    TEETH = {CC1TileCode.Value(s) for s in tuple(f"TEETH_{d}" for d in "NESW")}
    BLOBS = {CC1TileCode.Value(s) for s in tuple(f"BLOB_{d}" for d in "NESW")}
    MONSTERS = ANTS.union(PARAMECIA, GLIDERS, FIREBALLS, TANKS, BALLS, WALKERS, TEETH, BLOBS)
    ENTITIES = MONSTERS.union(BLOCKS, PLAYERS)
    DOORS = {CC1TileCode.Value(s) for s in tuple(f"{c}_DOOR" for c in ("RED", "BLUE", "YELLOW", "GREEN"))}
    KEYS = {CC1TileCode.Value(s) for s in tuple(f"{c}_KEY" for c in ("RED", "BLUE", "YELLOW", "GREEN"))}
    BOOTS = {CC1TileCode.Value(s) for s in ("FLIPPERS", "FIRE_BOOTS", "SKATES", "SUCTION_BOOTS")}

    @staticmethod
    def rotate(letters, d):
        if len(letters) == 1:
            return "NESW"[("NESW".index(letters) + "_RVL".index(d)) % 4]
        elif len(letters) == 2:
            corners = {"NE": "NW", "NW": "SW", "SW": "SE", "SE": "NE"}
            passes = "_LVR".index(d)
            for _ in range(passes):
                letters = corners[letters]
            return letters
        else:
            raise Exception(f"Cannot rotate {letters}.")

    @staticmethod
    def rotate_tile(tile_code, d):
        name = CC1TileCode.Name(tile_code)
        if name[-2] == "_":
            return CC1TileCode.Value(name[:-1] + CC1TileCodes.rotate(name[-1], d))
        elif name[-3] == "_" and tile_code not in CC1TileCodes.PANELS:
            return CC1TileCode.Value(name[:-2] + CC1TileCodes.rotate(name[-2:], d))
        else:
            return tile_code

    @staticmethod
    def rotate_left(tile_code):
        return CC1TileCodes.rotate_tile(tile_code, "L")
    
    @staticmethod
    def reverse(tile_code):
        return CC1TileCodes.rotate_tile(tile_code, "V")
    
    @staticmethod
    def rotate_right(tile_code):
        return CC1TileCodes.rotate_tile(tile_code, "R")    
