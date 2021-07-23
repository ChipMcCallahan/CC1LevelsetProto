from cc1_levelset_proto.cc1_levelset_pb2 import CC1TileCode
from cc1_levelset_proto import CC1TileCodes, CC1TileSpecs

def add(level, pos, tcode):
	tspec = level.map[pos]
	was_monster = tspec.top in CC1TileCodes.MONSTERS
	CC1TileSpecs.add(tspec, tcode)
	is_monster = tspec.top in CC1TileCodes.MONSTERS

	if was_monster and not is_monster:
		level.movement.remove(pos)
	if is_monster and not was_monster and len(level.movement) < 127:
		level.movement.append(pos)

def remove(level, pos, tcodes, *, keep_cloned_mobs=False):
	if isinstance(tcodes, int):
		tcodes = [tcodes]
	tspec = level.map[pos]
	removed = False
	for tcode in tcodes:
		if CC1TileSpecs.remove(tspec, tcode):
			removed = True
			if tcode in CC1TileCodes.MONSTERS and pos in level.movement:
				level.movement.remove(pos)
			elif tcode == CC1TileCode.TRAP:
				for k, v in tuple(level.trap_controls.items()):
					if v == pos:
						level.trap_controls.pop(k, None)
			elif tcode == CC1TileCode.TRAP_BUTTON:
				level.trap_controls.pop(pos, None)
			elif tcode == CC1TileCode.CLONER:
				for k, v in tuple(level.clone_controls.items()):
					if v == pos:
						level.clone_controls.pop(k, None)
				if not keep_cloned_mobs and tspec.top in CC1TileCodes.ENTITIES:
					CC1TileSpecs.remove(tspec, tspec.top)
			elif tcode == CC1TileCode.CLONE_BUTTON:
				level.clone_controls.pop(pos, None)
	return removed

def is_valid(level):
	for tspec in level.map.values():
		if not CC1TileSpecs.is_valid(tspec):
			return False
