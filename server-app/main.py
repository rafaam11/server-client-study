import socket, threading, tkinter as tk
from datetime import datetime

HOST = ''          # 0.0.0.0, 모든 NIC 수신
PORT = 9000        # 방화벽 허용할 포트

class ServerApp:
    def __init__(self, root):
        root.title("PC-1  서버")
        root.resizable(False, False)

        tk.Button(root, text="서버 시작", command=self.start).pack(pady=6)
        self.log = tk.Text(root, width=52, height=18, state='disabled')
        self.log.pack()

    def start(self):
        threading.Thread(target=self.run_server, daemon=True).start()

    def run_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            self._w(f"[{datetime.now():%H:%M:%S}] 서버 대기중 … :{PORT}")
            while True:
                conn, addr = s.accept()
                self._w(f"[연결] {addr}")
                threading.Thread(target=self.handle, args=(conn, addr), daemon=True).start()

    def handle(self, conn, addr):
        with conn:
            while data := conn.recv(4096):
                msg = data.decode('utf-8', errors='replace')
                self._w(f"{addr} ▶ {msg}")

    def _w(self, text):
        self.log['state']='normal'
        self.log.insert('end', text+'\n')
        self.log.see('end')
        self.log['state']='disabled'

if __name__ == "__main__":
    tk.Tk().after(0, lambda: ServerApp(tk._default_root)); tk.mainloop()
