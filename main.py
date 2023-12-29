from graphics import Window, Line, Point


def main():
    win = Window(800, 600)
    
    # draw lines to test Line and Point classes
    l = Line(Point(50, 50), Point(400, 400))
    win.draw_line(l, "black")

    win.wait_for_close()


main()