import itertools
from cc1_levelset_pb2 import CC1TileCode
from cc1_tile_codes import CC1TileCodes

# Utils for CC1TileSpec proto
class CC1TileSpecs:
    @staticmethod
    def is_invalid(tspec):
        return (tspec.top not in CC1TileCodes.ENTITIES and 
                tspec.bottom != CC1TileCode.FLOOR) or 
                tspec.top in CC1TileCodes.INVALID or
                tspec.bottom in set().union(CC1TileCodes.INVALID, CC1TileCodes.ENTITIES)
