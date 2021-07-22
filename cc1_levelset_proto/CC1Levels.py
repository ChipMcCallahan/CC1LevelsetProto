from cc1_levelset_proto.cc1_levelset_pb2 import CC1TileCode
from cc1_levelset_proto import CC1TileCodes, CC1TileSpecs

def add(level, pos, tcode):
	tspec = level[pos]
	CC1TileSpecs.add(tspec, tcode)
	if tcode in CC1TileCodes.MONSTERS and pos not in level.movement:
		level.movement.append(pos)

def remove(level, pos, tcode):
	tspec = level[pos]
	if CC1TileSpecs.remove(tspec, tcode):
		if tcode in CC1TileCodes.MONSTERS and pos in level.movement:
			del level.movement[level.movement.index(pos)]
		elif tcode == CC1TileCode.TRAP:
			for k, v in tuple(level.trap_controls.items()):
				if v == pos:
					del level.trap_controls[k]
		elif tcode == CC1TileCode.TRAP_BUTTON:
			for k in tuple(level.trap_controls.keys()):
				if k == pos:
					del level.trap_controls[k]
		elif tcode == CC1TileCode.CLONER:
			for k, v in tuple(level.clone_controls.items()):
				if v == pos:
					del level.clone_controls[k]
		elif tcode == CC1TileCode.CLONE_BUTTON:
			for k in tuple(level.clone_controls.keys()):
				if k == pos:
					del level.clone_controls[k]

def is_valid(level):
	for tspec in level.map.values():
		if not CC1TileSpecs.is_valid(tspec):
			return False