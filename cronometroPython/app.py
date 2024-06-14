import tkinter as tk

class Stopwatch:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cronômetro")

        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.running = False

        self.time_label = tk.Label(self.root, text="00:00:00", font=("Helvetica", 48))
        self.time_label.pack()

        self.start_button = tk.Button(self.root, text="Iniciar", command=self.start, width=15, height=2)
        self.start_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.stop_button = tk.Button(self.root, text="Parar", command=self.stop, width=15, height=2)
        self.stop_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.reset_button = tk.Button(self.root, text="Resetar", command=self.reset, width=15, height=2)
        self.reset_button.pack(side=tk.LEFT, padx=5, pady=5)

    def update_time(self):
        if self.running:
            self.seconds += 1
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1

            time_str = f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
            self.time_label.config(text=time_str)
            self.root.after(1000, self.update_time)

    def start(self):
        if not self.running:
            self.running = True
            self.update_time()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.time_label.config(text="00:00:00")

def main():
    stopwatch = Stopwatch()
    stopwatch.root.mainloop()

if __name__ == "__main__":
    main()