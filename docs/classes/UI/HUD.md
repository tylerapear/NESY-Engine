
# HUD Class

## Summary

The `HUD` class represents a draggable heads-up display (HUD) in a Pygame application.  
It displays the player's health bar, movement key hints (WASD), and attack key (J).  
The HUD can be repositioned by clicking and dragging it with the mouse.

---

## Constructor

### Syntax

```python
HUD(player, screen_size, anchor="top-left", offset=(10, 10))
```
--- 

## Parameters

| Parameter   | Type   | Required | Default    | Description                                                            |
| ----------- | ------ | -------- | ---------- | ---------------------------------------------------------------------- |
| player      | object | Yes      | N/A        | The player object that must have `health` and `max_health` attributes. |
| screen_size | tuple  | Yes      | N/A        | Screen dimensions `(width, height)` used for HUD positioning.          |
| anchor      | str    | No       | "top-left" | Determines initial positioning anchor of the HUD.                      |
| offset      | tuple  | No       | (10, 10)   | Pixel offset from the anchor position.                                 |

## Example

```python
hud = HUD(player, (1280, 720), anchor="top-left", offset=(10, 10))
```
---

## Properties

### player
**Type:** object  
**Description:** Reference to the player object containing health information.  
`hud.player = player_instance`

### screen_size
**Type:** tuple  
**Description:** Screen size (width, height) used for positioning HUD elements.  
`hud.screen_size = (800, 600)`

### anchor
**Type:** str  
**Description:** Anchor point for initial placement of the HUD.  
`hud.anchor = "top-left"`

### offset
**Type:** tuple  
**Description:** Offset values (x, y) from the anchor point.  
`hud.offset = (10, 20)`

### dragging
**Type:** bool  
**Description:** Indicates whether the HUD is currently being dragged.  
`hud.dragging = True`

### bar_x, bar_y
**Type:** int  
**Description:** X and Y coordinates of the HUD’s top-left corner.  
`hud.bar_x = 100`  
`hud.bar_y = 50`

---

## Methods

### update(events, dt)

Handles HUD interaction, including dragging with the mouse.

**Parameters:**

- `events`: List of Pygame events to process.
- `dt`: Delta time (not currently used in this method but included for consistency).

**Returns:**

- None

**Example:**

```python
hud.update(pygame.event.get(), dt)
```

### draw(surface)

Renders the HUD onto the provided Pygame surface. Displays:

- A health bar with current player health.
- WASD keys for movement.
- J key for attack.

**Parameters:**

- `surface`: The Pygame surface where the HUD will be drawn.

**Returns:**

- None

**Example:**

```python
hud.draw(screen)
```
---

## Dependencies

- **pygame**: Used for rendering, font management, surface creation, and input events.
- **player object**: Must provide `health` and `max_health` attributes.

---

## Notes

- The HUD is draggable within the game window using mouse events.
- The default HUD includes a health bar, WASD movement hints, and an "Attack" J key.
- The `dt` parameter in `update()` is currently unused but can be extended for time-based animations.
- The HUD bar is drawn at a fixed size of 1225x120 pixels.

---
