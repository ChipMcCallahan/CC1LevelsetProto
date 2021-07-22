import itertools
from cc1_levelset_proto.cc1_levelset_pb2 import CC1TileCode, TileSpec
from cc1_levelset_proto.cc1_tile_codes import CC1TileCodes

# Utils for CC1TileSpec proto
class CC1TileSpecs:
    @staticmethod
    def of(top, bottom=CC1TileCode.FLOOR):
        tspec = TileSpec
        tspec.top = top
        if bottom != CC1TileCode.FLOOR:
            tspec.bottom = bottom
        return tspec

    @staticmethod
    def is_invalid(tspec):
        return (tspec.top not in CC1TileCodes.ENTITIES and 
                tspec.bottom != CC1TileCode.FLOOR) or \
                tspec.top in CC1TileCodes.INVALID or \
                tspec.bottom in set().union(CC1TileCodes.INVALID, CC1TileCodes.ENTITIES)

    @staticmethod
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

    @staticmethod
    def remove(tspec, tcodes):
        if isinstance(tcodes, int):
            tcodes = [tcodes]
        for tcode in tcodes:
            if tcode == tspec.top:
                tspec.top = tspec.bottom
                tspec.ClearField("bottom")
            elif tcode == tspec.bottom:
                tspec.ClearField("bottom")

def do_assertions():

    # test is_invalid scenarios
    assert CC1TileSpecs.is_invalid(CC1TileSpecs.of(CC1TileCode.FLOOR, CC1TileCode.WALL))
    assert CC1TileSpecs.is_invalid(CC1TileSpecs.of(CC1TileCode.FLOOR, CC1TileCode.TEETH_S))
    assert CC1TileSpecs.is_invalid(CC1TileSpecs.of(CC1TileCode.TEETH_S, CC1TileCode.TEETH_S))
    assert CC1TileSpecs.is_invalid(CC1TileSpecs.of(CC1TileCode.NOT_USED_0))
    assert not CC1TileSpecs.is_invalid(CC1TileSpecs.of(CC1TileCode.TEETH_S, CC1TileCode.GRAVEL))
    assert not CC1TileSpecs.is_invalid(CC1TileSpecs.of(CC1TileCode.WALL))


    # test add scenarios
    tspec = CC1TileSpecs.of(CC1TileCode.WALL)
    CC1TileSpecs.add(tspec, CC1TileCode.FIRE)
    assert tspec == CC1TileSpecs.of(CC1TileCode.FIRE)

    tspec = CC1TileSpecs.of(CC1TileCode.TEETH_S, CC1TileCode.GRAVEL)
    CC1TileSpecs.add(tspec, CC1TileCode.FIRE)
    assert tspec == CC1TileSpecs.of(CC1TileCode.TEETH_S, CC1TileCode.FIRE)

    tspec = CC1TileSpecs.of(CC1TileCode.TEETH_S, CC1TileCode.GRAVEL)
    CC1TileSpecs.add(tspec, CC1TileCode.PLAYER_S)
    assert tspec == CC1TileSpecs.of(CC1TileCode.PLAYER_S, CC1TileCode.GRAVEL)

    tspec = CC1TileSpecs.of(CC1TileCode.WALL)
    CC1TileSpecs.add(tspec, CC1TileCode.BLOCK)
    assert tspec == CC1TileSpecs.of(CC1TileCode.BLOCK, CC1TileCode.WALL)


    # test remove scenarios
    tspec = CC1TileSpecs.of(CC1TileCode.WALL)
    CC1TileSpecs.remove(tspec, CC1TileCode.BLOCK)
    assert tspec == CC1TileSpecs.of(CC1TileCode.WALL)

    tspec = CC1TileSpecs.of(CC1TileCode.WALL)
    CC1TileSpecs.remove(tspec, CC1TileCode.WALL)
    assert tspec == CC1TileSpecs.of(CC1TileCode.FLOOR)    

    tspec = CC1TileSpecs.of(CC1TileCode.TEETH_S, CC1TileCode.WALL)
    CC1TileSpecs.remove(tspec, CC1TileCode.WALL)
    assert tspec == CC1TileSpecs.of(CC1TileCode.TEETH_S)

    tspec = CC1TileSpecs.of(CC1TileCode.TEETH_S, CC1TileCode.WALL)
    CC1TileSpecs.remove(tspec, CC1TileCode.TEETH_S)
    assert tspec == CC1TileSpecs.of(CC1TileCode.WALL)   

    tspec = CC1TileSpecs.of(CC1TileCode.TEETH_S, CC1TileCode.WALL)
    CC1TileSpecs.remove(tspec, CC1TileCodes.ENTITIES)
    assert tspec == CC1TileSpecs.of(CC1TileCode.WALL)

    tspec = CC1TileSpecs.of(CC1TileCode.FIRE, CC1TileCode.WALL)
    CC1TileSpecs.remove(tspec, CC1TileCodes.WALLS)
    assert tspec == CC1TileSpecs.of(CC1TileCode.FIRE)

    print("CC1TileSpecs assertions passed.")


# file will raise AssertionError on import if assertions fail
do_assertions()