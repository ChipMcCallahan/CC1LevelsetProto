import itertools
from cc1_levelset_proto.cc1_levelset_pb2 import CC1TileCode, TileSpec
from cc1_levelset_proto import CC1TileCodes

# Utils for CC1TileSpec proto
def of(top, bottom=CC1TileCode.FLOOR):
    tspec = TileSpec()
    tspec.top = top
    if bottom != CC1TileCode.FLOOR:
        tspec.bottom = bottom
    return tspec

def is_invalid(tspec):
    return (tspec.top not in CC1TileCodes.ENTITIES and 
            tspec.bottom != CC1TileCode.FLOOR) or \
            tspec.top in CC1TileCodes.INVALID or \
            tspec.bottom in set().union(CC1TileCodes.INVALID, CC1TileCodes.ENTITIES)

def add(tspec, tcode):
    is_entity = tcode in CC1TileCodes.ENTITIES
    entity_here = tspec.top in CC1TileCodes.ENTITIES
    if is_entity:
        if not entity_here:
            tspec.bottom = tspec.top
        tspec.top = tcode
    else:
        if entity_here:
            tspec.bottom = tcode
        else:
            tspec.top = tcode

def remove(tspec, tcode):
    if tcode == CC1TileCode.FLOOR:
        return False
    elif tcode == tspec.top:
        tspec.top = tspec.bottom
        tspec.ClearField("bottom")
        return True
    elif tcode == tspec.bottom:
        tspec.ClearField("bottom")
        return True
    return False

def do_assertions():

    # test is_invalid scenarios
    assert is_invalid(of(CC1TileCode.FLOOR, CC1TileCode.WALL))
    assert is_invalid(of(CC1TileCode.FLOOR, CC1TileCode.TEETH_S))
    assert is_invalid(of(CC1TileCode.TEETH_S, CC1TileCode.TEETH_S))
    assert is_invalid(of(CC1TileCode.NOT_USED_0))
    assert not is_invalid(of(CC1TileCode.TEETH_S, CC1TileCode.GRAVEL))
    assert not is_invalid(of(CC1TileCode.WALL))


    # test add scenarios
    tspec = of(CC1TileCode.WALL)
    add(tspec, CC1TileCode.FIRE)
    assert tspec == of(CC1TileCode.FIRE)

    tspec = of(CC1TileCode.TEETH_S, CC1TileCode.GRAVEL)
    add(tspec, CC1TileCode.FIRE)
    assert tspec == of(CC1TileCode.TEETH_S, CC1TileCode.FIRE)

    tspec = of(CC1TileCode.TEETH_S, CC1TileCode.GRAVEL)
    add(tspec, CC1TileCode.PLAYER_S)
    assert tspec == of(CC1TileCode.PLAYER_S, CC1TileCode.GRAVEL)

    tspec = of(CC1TileCode.WALL)
    add(tspec, CC1TileCode.BLOCK)
    assert tspec == of(CC1TileCode.BLOCK, CC1TileCode.WALL)


    # test remove scenarios
    tspec = of(CC1TileCode.WALL)
    assert not remove(tspec, CC1TileCode.BLOCK)
    assert tspec == of(CC1TileCode.WALL)

    tspec = of(CC1TileCode.WALL)
    assert remove(tspec, CC1TileCode.WALL)
    assert tspec == of(CC1TileCode.FLOOR)    

    tspec = of(CC1TileCode.TEETH_S, CC1TileCode.WALL)
    assert remove(tspec, CC1TileCode.WALL)
    assert tspec == of(CC1TileCode.TEETH_S)

    tspec = of(CC1TileCode.TEETH_S, CC1TileCode.WALL)
    assert remove(tspec, CC1TileCode.TEETH_S)
    assert tspec == of(CC1TileCode.WALL)   

    tspec = of(CC1TileCode.TEETH_S, CC1TileCode.WALL)
    assert remove(tspec, CC1TileCodes.ENTITIES)
    assert tspec == of(CC1TileCode.WALL)

    tspec = of(CC1TileCode.FIRE, CC1TileCode.WALL)
    assert remove(tspec, CC1TileCodes.WALLS)
    assert tspec == of(CC1TileCode.FIRE)


# file will raise AssertionError on import if assertions fail
do_assertions()