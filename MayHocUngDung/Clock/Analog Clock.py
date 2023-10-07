import tkinter as tk, time, math

width = height = 400

root = tk.Tk()
root.title("Analog Clock")
canvas = tk.Canvas(root, width=width, height=height, bg="white")
canvas.pack()

def update_clock():
    canvas.delete("all")
    now = time.localtime()
    hour = now.tm_hour % 12
    minute = now.tm_min
    second = now.tm_sec
#Draw clock face
    canvas.create_oval(2, 2, width, height, outline="black", width=2)
#Draw hour numbers
    for i in range(12):
        angle = i * math.pi / 6 - math.pi / 2
        x = width / 2 + 0.7 * width / 2 * math.cos(angle)
        y = height / 2 + 0.7 * height / 2 * math.sin(angle)
        if i == 0:
            canvas.create_text(x, y - 10, text=str(i + 12), font=("Helvetica", 12))
        else:
            canvas.create_text(x, y, text=str(i), font=("Helvetica", 12))
#Draw minute lines
    for i in range(60):
        angle = i * math.pi / 30 - math.pi / 2
        x1 = (width / 2) + 0.8 * (width / 2) * math.cos(angle)
        y1 = (height / 2) + 0.8 * (height / 2) * math.sin(angle)
        x2 = (width / 2) + 0.9 * (width / 2) * math.cos(angle)
        y2 = (height / 2) + 0.9 * (height / 2) * math.sin(angle)
        if i % 5 == 0:
            canvas.create_line(x1, y1, x2, y2, fill="black", width=3)
        else:
            canvas.create_line(x1, y1, x2, y2, fill="black", width=1)
#Draw hour hand
    hour_angle = (hour + minute / 60) * math.pi / 6 - math.pi / 2
    hour_x = width / 2 + 0.5 * width / 2 * math.cos(hour_angle)
    hour_y = height / 2 + 0.5 * height / 2 * math.sin(hour_angle)
    canvas.create_line(width / 2, height / 2, hour_x, hour_y, fill="black", width=6)
#Draw minute hand
    minute_angle = (minute + second / 60) * math.pi / 30 - math.pi / 2
    minute_x = width / 2 + 0.7 * width / 2 * math.cos(minute_angle)
    minute_y = height / 2 + 0.7 * height / 2 * math.sin(minute_angle)
    canvas.create_line(width / 2, height / 2, minute_x, minute_y, fill="black", width=4)
#Draw second hand
    second_angle = second * math.pi / 30 - math.pi / 2
    second_x = width / 2 + 0.6 * width / 2 * math.cos(second_angle)
    second_y = height / 2 + 0.6 * width / 2 * math.sin(second_angle)
    canvas.create_line(width / 2, height / 2, second_x, second_y, fill="red", width=2)

canvas.after(1000, update_clock())

update_clock()
root.mainloop()