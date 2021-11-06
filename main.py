#!/usr/bin/env python3
import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

def main() -> None:
    screen_width = 80
    screen_height = 50

    class Player:
        def __init__(self, x, y) -> None:
            self.x = x
            self.y =y

    player = Player(int(screen_width/2), int(screen_height/2))
    event_handler = EventHandler();

    tileset = tcod.tileset.load_tilesheet(
        "assets/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Lemegeton",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            root_console.print(x=player.x, y=player.y, string="@")
            
            context.present(root_console)

            root_console.clear()

            for event in tcod.event.wait():
                action = event_handler.dispatch(event)

                if action is None:
                    continue
                
                if isinstance(action, MovementAction):
                    player.x += action.dx
                    player.y += action.dy
                elif isinstance(action, EscapeAction):
                    raise SystemExit()




if __name__ == "__main__":
    main()