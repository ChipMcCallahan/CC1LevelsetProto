# CC1LevelsetProto
Proto definition and generated Python code for working with CC1 levelsets.

### Demo
See the [Colab notebook](https://github.com/ChipMcCallahan/CC1LevelsetProto/blob/main/cc1_levelset_proto.ipynb) for a fully interactive demo, or use these snippets to get started.

```
!pip install git+https://github.com/ChipMcCallahan/CC1LevelsetProto.git
```

```python
from cc1_levelset_proto.cc1_levelset_pb2 import Levelset, CC1TileCode

levelset = Levelset()
levelset.name = "Demo"
level = levelset.levels.add()
level.title = "Demo Level"
level.author = "Chip McCallahan"
level.time = 100
level.chips = 200
level.password = "AAAA"
level.hint = "This is a hint."
level.clone_controls[33] = 45
level.trap_controls[13] = 37
level.movement.append(14 * 32 + 28)
x, y = 16, 16
tilespec = level.map.tiles[y * 32 + x]
tilespec.top = CC1TileCode.PLAYER_S
tilespec.bottom = CC1TileCode.GRAVEL

print(levelset)
```

```
name: "Demo"
levels {
  title: "Demo Level"
  author: "Chip McCallahan"
  time: 100
  chips: 200
  hint: "This is a hint."
  password: "AAAA"
  map {
    tiles {
      key: 528
      value {
        top: PLAYER_S
        bottom: GRAVEL
      }
    }
  }
  trap_controls {
    key: 13
    value: 37
  }
  clone_controls {
    key: 33
    value: 45
  }
  movement: 1337
}
```
