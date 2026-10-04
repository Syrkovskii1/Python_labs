import os
import sys
import time

WHITE = '\u001b[47m'
RESET = '\u001b[0m'
CURSOR_HOME = '\u001b[H'
HIDE_CURSOR = '\u001b[?25l'
SHOW_CURSOR = '\u001b[?25h'


def get_pattern_frame(shift: int, height: int = 5, repeats: int = 2) -> str:
    """Генерирует один кадр узора 'c', сдвинутый по горизонтали на shift."""
    period = 2 * (height - 1)  # 8
    total_x = period * repeats + 1
    frame_lines = []

    for y in range(height):
        line = ""
        for x in range(total_x):
            # Сдвигаем фазу волны на значение shift
            pos = (x + shift) % period

            # Траектория первой волны
            y1 = pos if pos < height else period - pos
            # Вторая волна (зеркальная)
            y2 = (height - 1) - y1

            if y == y1 or y == y2:
                line += f"{WHITE}  {RESET}"
            else:
                line += "  "
        frame_lines.append(line)

    return "\n".join(frame_lines) + "\n"


def animation():
    clear_command = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear_command)

    # Генерируем строго 4 кадра со смещением от 0 до 3
    frames = [get_pattern_frame(shift=s) for s in range(4)]

    sys.stdout.write(HIDE_CURSOR)
    sys.stdout.flush()

    try:
        # Проигрываем анимацию (волна циклически бежит по экрану)
        for _ in range(12):
            for i, frame in enumerate(frames):
                sys.stdout.write(CURSOR_HOME)
                sys.stdout.write(f"Кадр {i + 1} / 4\n")
                sys.stdout.write(frame)
                sys.stdout.flush()
                time.sleep(0.15)
    finally:
        sys.stdout.write(SHOW_CURSOR)
        sys.stdout.flush()
        print("\nГотово!")


if __name__ == "__main__":
    animation()