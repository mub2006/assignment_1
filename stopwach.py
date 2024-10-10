import tkinter as tk
import time

class Stopwatch(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Stopwatch")
        self.geometry("300x400")
        self.resizable(False, False)

        self.is_running = False
        self.start_time = 0
        self.elapsed_time = 0

        self.create_widgets()
        self.update_display()

    def create_widgets(self):
        self.display = tk.Label(self, text="00:00:00", font=("Arial", 48))
        self.display.pack(pady=20)

        self.start_button = tk.Button(self, text="Start", command=self.start, width=10)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(self, text="Stop", command=self.stop, width=10)
        self.stop_button.pack(pady=5)

        self.reset_button = tk.Button(self, text="Reset", command=self.reset, width=10)
        self.reset_button.pack(pady=5)

        self.lap_button = tk.Button(self, text="Lap", command=self.record_lap, width=10)
        self.lap_button.pack(pady=5)

        self.lap_list = tk.Listbox(self)
        self.lap_list.pack(pady=10, fill=tk.BOTH, expand=True)

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = time.time() - self.elapsed_time
            self.update_display()

    def stop(self):
        if self.is_running:
            self.is_running = False

    def reset(self):
        self.elapsed_time = 0
        self.update_display()
        self.lap_list.delete(0, tk.END)

    def record_lap(self):
        if self.is_running:
            lap_time = time.strftime("%H:%M:%S", time.gmtime(self.elapsed_time))
            self.lap_list.insert(tk.END, lap_time)

    def update_display(self):
        if self.is_running:
            self.elapsed_time = time.time() - self.start_time
            self.display.config(text=time.strftime("%H:%M:%S", time.gmtime(self.elapsed_time)))
            self.after(1000, self.update_display)

if __name__ == "__main__":
    app = Stopwatch()
    app.mainloop()
