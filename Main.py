import tkinter as tk
import time
from Data import Data
from Perceptron import Perceptron
from Plot import Plot
from ErrorGraph import ErrorPlot


Points1 = 0
Points2 = 0
Neuron = 0

class GUI:

    def __init__(self):
        self.iterator = None
        self.Speed = 10
        self.epochs = 0
        self.ranSize = 0
        self.Stop = False
        
        self.root = tk.Tk()
        self.root.geometry("900x450")
        self.root.resizable(False, False)
        self.root.title("Long live the king")

        self.epochs = tk.StringVar(value=10)
        self.ranSize = tk.StringVar(value=3)
        self.Speed = tk.StringVar(value=10)

        self.all = tk.Frame()
        self.all.columnconfigure(0, weight=100000)
        self.all.columnconfigure(1, weight=1)


# # LEFT COLUMN
        self.L_column = tk.Frame(self.all)
        self.L_column.columnconfigure(0, weight=1)
        self.L_column.columnconfigure(1, weight=1)

        self.RandomSizeText = tk.Label(self.L_column, text="Random Size:")
        self.RandomSizeInput = tk.Spinbox(self.L_column, from_=1, to=1000, textvariable=self.ranSize)
        self.RandomSizeText.grid(row=0, column=0, ipady=7)
        self.RandomSizeInput.grid(row=0, column=1)

        self.inputData1 = tk.Text(self.L_column)
        self.inputData1.grid(row=1, column=0, sticky='wsn')
        self.inputData2 = tk.Text(self.L_column)
        self.inputData2.grid(row=1, column=1, sticky='wsn')

        # self.L_btn_Frame = tk.Frame(self.L_column)
        # self.L_btn_Frame.columnconfigure(0, weight=1)
        # self.L_btn_Frame.columnconfigure(1, weight=1)

        self.btn_Randomize = tk.Button(self.L_column, text="Randomize", command=self.RandomizeData)
        self.btn_Save = tk.Button(self.L_column, text="Save", command=self.SaveData)
        self.btn_Randomize.grid(row=2, column=0, sticky='wes')
        self.btn_Save.grid(row=2, column=1, sticky='wes')

        # self.L_btn_Frame.grid(row=1, column=0)
        self.L_column.grid(row=0, column=0, sticky="wns", ipadx=10)

# # RIGHT COLUMN
        self.R_column = tk.Frame(self.all)
        self.R_column.columnconfigure(0, weight=10)

        self.R_btn_Frame = tk.Frame(self.R_column)
        self.R_btn_Frame.columnconfigure(0, weight=1)
        self.R_btn_Frame.columnconfigure(1, weight=1)
        self.R_btn_Frame.columnconfigure(2, weight=1)
        self.R_btn_Frame.columnconfigure(3, weight=1)

        self.btn_Run = tk.Button(self.R_btn_Frame, text="Run", command=self.StartPerceptron)
        self.btn_Step = tk.Button(self.R_btn_Frame, text="Step", command=self.Step)
        self.btn_Clear = tk.Button(self.R_btn_Frame, text="Clear", command=self.Clear, state="disabled")
        self.btn_Result = tk.Button(self.R_btn_Frame, text="Result", command=self.Result)
        self.btn_Run.grid(row=0, column=0, sticky=tk.W+tk.E)
        self.btn_Step.grid(row=0, column=1, sticky=tk.W+tk.E)
        self.btn_Clear.grid(row=0, column=2, sticky=tk.W+tk.E)
        self.btn_Result.grid(row=0, column=3, sticky=tk.W+tk.E)

        self.R_btn_Frame.grid(row=0, column=0, sticky='we')

# PERCEPTRON VIEW
        # self.Graph = tk.Canvas(self.R_column, height=200, bg="red")
        # self.Graph.grid(row=1, column=0)
        self.bgimage = tk.PhotoImage(file = "bg.png")

        self.Graph = tk.Frame(self.R_column, height=2000)
        self.Graph.columnconfigure(0, weight=1)
        self.Graph.columnconfigure(1, weight=1)
        self.Graph.columnconfigure(2, weight=3)
        self.Graph.columnconfigure(3, weight=10)
    
        lbl = tk.Label(self.Graph, image=self.bgimage)
        lbl.img = self.bgimage  # Keep a reference in case this code put is in a function.
        lbl.place(relx=0.02, rely=0.19, anchor='nw')  # Place label in center of parent.

        self.x1 = tk.Label(self.Graph, text='0.00', font=("Arial, 20"))
        self.x2 = tk.Label(self.Graph, text='0.00', font=("Arial, 20"))
        self.w1 = tk.Label(self.Graph, text='0.00', font=("Arial, 20"))
        self.w2 = tk.Label(self.Graph, text='0.00', font=("Arial, 20"))
        self.wsum = tk.Label(self.Graph, text='0.00', font=("Arial, 20"))
        self.y = tk.Label(self.Graph, text='0.00', font=("Arial, 20"))
        tk.Label(self.Graph, text="input", font=("Arial, 15")).grid(row=0, column=0, padx=30)
        tk.Label(self.Graph, text="weights", font=("Arial, 15")).grid(row=0, column=1, padx=30)
        tk.Label(self.Graph, text="sum", font=("Arial, 15")).grid(row=0, column=3, padx=30)
        tk.Label(self.Graph, text="result", font=("Arial, 15")).grid(row=0, column=4, padx=30)
        self.x1.grid(row=1, column=0, pady=35)
        self.x2.grid(row=3, column=0, pady=25)
        self.w1.grid(row=1, column=1, pady=25)
        self.w2.grid(row=3, column=1, pady=25)
        tk.Label(self.Graph, text="                    ").grid(row=2, column=2, pady=25)
        self.wsum.grid(row=2, column=3, pady=25)
        self.y.grid(row=2, column=4, pady=25)

        self.Graph.grid(row=1, column=0, sticky='ns', pady=30)


        # self.Console = tk.Text(self.R_column, bg="grey")
        # self.Console.grid(row=20, column=0, sticky='wes', rowspan=10)

        self.Console = tk.Frame(self.R_column)
        self.epochsText = tk.Label(self.Console, text="Epochs:")
        self.epochsInput = tk.Spinbox(self.Console, from_=0, to=1000, textvariable=self.epochs)
        self.speedText = tk.Label(self.Console, text="Speed:")
        self.speedInput = tk.Spinbox(self.Console, from_=1, to=1000, textvariable=self.Speed)


        self.epochsText.grid(row=0, column=0)
        self.epochsInput.grid(row=0, column=1)
        tk.Label(self.Console, text="       ").grid(row=0, column=2)
        self.speedText.grid(row=0, column=3)
        self.speedInput.grid(row=0, column=4)


        self.Console.grid(row=20, column=0, sticky='wes', rowspan=10)

        self.R_column.grid(row=0, column=1, sticky='news')

        self.all.pack(fill="both", anchor="nw", expand=True)

# APPBAR

        self.appbar = tk.Menu(self.root)
        self.root.config(menu=self.appbar)

        self.fileMenu = tk.Menu(self.appbar)
        self.fileMenu.add_command(label="Save data to File", command=self.onSaveDataFile)
        self.fileMenu.add_command(label="Load data from File", command=self.onReadDateFile)

        self.appbar.add_cascade(label="File", menu=self.fileMenu)


        self.root.mainloop()

    def SaveData(self):
        global Points1, Points2
        if (Points1 == 0):
            Points1 = Data(self.inputData1.get("1.0", "end-1c"))
            Points2 = Data(self.inputData2.get("1.0", "end-1c"))
        else:
            Points1.setData(self.inputData1.get("1.0", "end-1c"))
            Points2.setData(self.inputData2.get("1.0", "end-1c"))
        self.btn_Step.config(state=tk.NORMAL, command=self.Step)

    def RandomizeData(self):
        global Points1, Points2
        if (Points1 == 0):
            Points1 = Data()
            Points2 = Data()

        data = Points1.generatePoints(int(self.ranSize.get()))
        self.inputData1.delete("1.0", "end")
        self.inputData1.insert("1.0", data)
        data = Points2.generatePoints(int(self.ranSize.get()))
        self.inputData2.delete("1.0", "end")
        self.inputData2.insert("1.0", data)
        self.btn_Step.config(state=tk.NORMAL, command=self.Step)

    def StartPerceptron(self):
        global Points1, Points2, Neuron
        self.btn_Clear.config(state=tk.NORMAL)
        if (Neuron == 0):
            Neuron = Perceptron()
        self.iterator = Neuron.train(Points1.PointsList, Points2.PointsList, int(self.epochs.get()))
        self.AutoUpdateGraph()
        self.Stop = False

    def Step(self):
        global Points1, Points2, Neuron
        self.btn_Clear.config(state=tk.NORMAL)
        if (Neuron == 0):
            Neuron = Perceptron()
        self.iterator = Neuron.train(Points1.PointsList, Points2.PointsList, int(self.epochs.get()))
        self.StepUpdateGraph()

    def Clear(self):
        global Neuron
        self.btn_Clear.config(state=tk.DISABLED)
        Neuron.Clear()
        self.x1.config(text='0.00')
        self.x2.config(text='0.00')
        self.w1.config(text='0.00')
        self.w2.config(text='0.00')
        self.wsum.config(text='0.00')
        self.y.config(text='0.00')
        self.btn_Step.config(state=tk.NORMAL, command=self.Step)
        self.Stop = True

    def Result(self):
        global Points1, Points2, Neuron
        if (Neuron == 0):
            Plot(Points1.PointsList, Points2.PointsList)
        else:
            m = -Neuron.weights[0] / Neuron.weights[1]
            b = -Neuron.bias / Neuron.weights[1]
            Plot(Points1.PointsList, Points2.PointsList, m, b)
            ErrorPlot(Neuron.errors)



    def AutoUpdateGraph(self):
        try:
            if (not self.Stop):
                x1, x2, w1, w2, ws, y = next(self.iterator)
                w1 = round(w1, 4)
                w2 = round(w2, 4)
                ws = round(ws, 4)
                self.x1.config(text=x1)
                self.x2.config(text=x2)
                self.w1.config(text=w1)
                self.w2.config(text=w2)
                self.wsum.config(text=ws)
                self.y.config(text=y)
                self.root.after(int(self.Speed.get()), self.AutoUpdateGraph)
        except StopIteration:
            pass

    def StepUpdateGraph(self):
        try:
            x1, x2, w1, w2, ws, y = next(self.iterator)
            w1 = round(w1, 4)
            w2 = round(w2, 4)
            ws = round(ws, 4)
            self.x1.config(text=x1)
            self.x2.config(text=x2)
            self.w1.config(text=w1)
            self.w2.config(text=w2)
            self.wsum.config(text=ws)
            self.y.config(text=y)
            self.btn_Step.config(state=tk.NORMAL, command=self.StepUpdateGraph)
        except StopIteration:
            self.btn_Step.config(state=tk.DISABLED)

    def onSaveDataFile(self):
        global Points1, Points2
        f = open("PerceptronTrainingData", "w")
        f.write(Points1.getPointsList() + "###\n" + Points2.getPointsList())
        f.close()

    def onReadDateFile(self):
        global Points1, Points2
        if (Points1 == 0):
            Points1 = Data()
            Points2 = Data()
        f = open("PerceptronTrainingData", "r")
        data = f.read()
        p1, p2 = data.split("###\n")
        Points1.setData(p1)
        Points2.setData(p2)
        self.inputData1.delete("1.0", "end")
        self.inputData1.insert("1.0", p1)
        self.inputData2.delete("1.0", "end")
        self.inputData2.insert("1.0", p2)


GUI()