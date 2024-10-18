import PySimpleGUI as sg
window = sg.Window(title="Profile", 
                    layout=[[sg.Text("NPM    : 2210010398")],
                            [sg.Text("Nama   : RENNY MELANDA FEBRIYANTI")],
                            [sg.Text("Kelas  : 5O REGULER PAGI BANJARMASIN")]
                            ], size=(400,200))
window()
window.close()