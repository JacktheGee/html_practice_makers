from lib.mario_testing import Character

def test_create_char():
    new_char = Character("Mario", 100, 5)
    assert new_char.name == "Mario"
    assert new_char.health == 100
    assert new_char.damage == 5

def test_char_equals_char():
    new_char1 = Character("Mario", 100, 5)
    new_char2 = Character("Mario", 100, 5)
    assert new_char1 == new_char2
    
# Test will fail if any function is added which alters the output
# of the class attributes
def test_char_formats():
    new_char = Character("Mario", 100, 5)
    assert new_char == Character(name="Mario", health=100, damage=5)
