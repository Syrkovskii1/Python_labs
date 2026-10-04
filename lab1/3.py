import os
import time


if os.name == 'nt':
    CLEAR = 'cls'
else:
    CLEAR = 'clear'

frames = [
    """
      .  .
      .  .
    """,
    """
      #  .
      .  .
    """,
    """
      #  #
      .  .
    """,
    """
      #  #
      #  #
    """
]

def animation():
   
    for _ in range(3):
        for frame in frames:
            os.system(CLEAR)  
            print(frame)       
            time.sleep(0.3)   

if __name__ == '__main__':
    animation()