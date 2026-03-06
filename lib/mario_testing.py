from dataclasses import dataclass

@dataclass
class Character:
    name: str
    health: int
    damage: int

# Frozen prevents the attributes from being edited, a new object needs to be created to overwrite values
# Good for static objects
@dataclass(frozen=True)
class Weapon:
    name: str
    damage: int

mario = Character("Mario", 100, 5)
red_shell = Weapon("Red Shell", 20)

print(mario)
print(red_shell)

# Outputs with 'Character(name=...)
# This is only metadata and isn't passed forward to something like a SQL file
