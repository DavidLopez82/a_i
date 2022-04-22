import enum

class etapa_status(enum.Enum):
    running = 1
    pause = 2
    stop = 3
    finish = 4
    waiting = 5
    not_init = 6

