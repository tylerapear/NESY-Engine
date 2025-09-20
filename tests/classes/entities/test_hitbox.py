from classes.entities.Hitbox import Hitbox

def create_hitbox(x, y, width, height):
    return Hitbox({"x": x, "y": y, "width": width, "height": height})

def test_collides():
    a = create_hitbox(0, 0, 10, 10)
    b = create_hitbox(5, 5, 10, 10)
    c = create_hitbox(20, 20, 10, 10)

    assert a.collides(b) is True  # Overlapping
    assert a.collides(c) is None  # Not overlapping

def test_get_collision_direction():
    a = create_hitbox(10, 10, 10, 10)
    b = create_hitbox(5, 10, 10, 10)  # Left
    c = create_hitbox(25, 10, 10, 10)  # Right
    d = create_hitbox(10, 5, 10, 10)  # Up
    e = create_hitbox(10, 25, 10, 10)  # Down

    assert a.getCollisionDirection(b) == "Left"
    assert a.getCollisionDirection(c) == "Right"
    assert a.getCollisionDirection(d) == "Up"
    assert a.getCollisionDirection(e) == "Down"