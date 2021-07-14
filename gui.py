import tkinter as tk
import tkinter.ttk as ttk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)

        self.master = master
        self.pack()

        self.mk_widgets()

    def mk_widgets(self):
        fr1 = tk.Frame(self)
        tk.Label(fr1, text='Technical components:').pack()

        # Make sens related widgets
        self.sens_frame = tk.Frame(fr1, bd=5)

        self.sens_label = tk.Label(self.sens_frame, text='Select sensitivity(dpi):')
        self.sens_label.grid(row=0, column=0, rowspan=2)

        var = tk.IntVar()
        var.set(self.master.mouse.dpi[0])
        self.scale = tk.Scale(self.sens_frame, variable=var, from_=200, to=8500, resolution=100, command=self.change_sens, length=400,  orient=tk.HORIZONTAL)

        self.scale.grid(row=0, column=1, rowspan=2, columnspan=3)
        self.sens_frame.pack()

        # Make poll-rate related widgets
        self.poll_rate_frame = tk.Frame(fr1, bd=5)
        self.poll_rate_label = tk.Label(self.poll_rate_frame, text='Choose poll rate:')
        self.poll_rate_label.grid(row=0, column=0)

        poll_rates = (125, 500, 1000)
        self.poll_rate = tk.StringVar()
        self.poll_rate.set(str(self.master.mouse.poll_rate))
        self.poll_rate.trace_add('write', self.set_poll)
        self.poll_rates_menu = tk.OptionMenu(self.poll_rate_frame, self.poll_rate, *poll_rates)
        self.poll_rates_menu.grid(row=0, column=1)

        self.poll_rate_frame.pack(side='left')
        fr1.pack()


        # Make RGB related widgets:
        fr2 = tk.Frame(self)
        tk.Label(fr2, text='RGB settings:').pack()

        self.brightness_frame = tk.Frame(fr2, bd=5)

        self.brightness_label = tk.Label(self.brightness_frame, text='Set brightness:')
        self.brightness_label.grid(row=0, column=0, rowspan=2)

        var = tk.IntVar()
        var.set(self.master.led.brightness)
        self.scale = tk.Scale(self.brightness_frame, variable=var, from_=0, to=100, resolution=1, command=self.change_brightness, length=300,  orient=tk.HORIZONTAL)

        self.scale.grid(row=0, column=1, rowspan=2, columnspan=3)
        self.brightness_frame.pack()

        rgb_mode_frame = tk.Frame(fr2, bd=5)
        # TODO: make rgb modes

        fr2.pack(side='left')

    def change_brightness(self, arg):
        self.master.led.brightness = int(arg)

    def change_sens(self, args):
        args = int(args)
        self.master.mouse.dpi = (args, args)

    def set_poll(self, *arg):
        rate = int(self.poll_rate.get())
        self.master.mouse.poll_rate = rate

class Window(tk.Tk):
    def __init__(self, mouse, led):
        super().__init__()

        self.title('Razer Viper Mini')

        self.mouse = mouse
        self.led = led

        app = App(self)

    def run(self):
        self.mainloop()

if __name__=='__main__':
    Window(None, None).run()
