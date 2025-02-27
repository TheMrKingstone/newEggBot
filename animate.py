import copy
import cv2
import numpy as np
from draw_state import draw_state

def make_video(scramble, solution, tps):
    # opencv video writer
    size = (400, 400)
    writer = cv2.VideoWriter("movie.webm", cv2.VideoWriter_fourcc(*'VP90'), tps, size)

    # create a copy so we don't modify the original
    pos = copy.deepcopy(scramble)

    def write_frame():
        # draw the state and send it to the video writer
        image = draw_state(pos)
        cv2_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        writer.write(cv2_image)

    # draw the first frame before any moves were applied
    write_frame()

    # draw the rest of the frames
    for i in range(solution.length()):
        pos.move(solution.at(i))
        write_frame()

    # finish the video
    writer.release()