import simple_draw as sd


def smile(x, y, size, eye):
    face_point = sd.get_point(x, y)
    left_eye_point = sd.get_point(x - (eye * 2), y + eye)
    right_eye_point = sd.get_point(x + (eye * 2), y + eye)
    color = sd.COLOR_BLACK
    start_point = sd.get_point(x - (eye * 2), y - (eye * 2))
    end_point = sd.get_point(x + (eye * 2), y - (eye * 2))
    sd.circle(face_point, size, color, 2)
    sd.circle(left_eye_point, eye, color, 1)
    sd.circle(right_eye_point, eye, color, 1)
    sd.line(start_point, end_point, color, 2)



if __name__ == "__main__":
    sd.resolution = (1200, 600)
    smile(200, 200, 50, 10)
    sd.pause()