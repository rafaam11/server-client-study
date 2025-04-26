import socket, tkinter as tk

SERVER_PORT = 9000

class ClientApp:
    def __init__(self, root):
        root.title("PC-2  클라이언트")
        root.resizable(False, False)

        tk.Label(root, text="서버 IP").grid(row=0, column=0, sticky='e')
        self.ip_entry = tk.Entry(root, width=18); self.ip_entry.grid(row=0, column=1, padx=4, pady=6)
        self.ip_entry.insert(0, "192.168.219.104")        # PC-1 IP

        tk.Label(root, text="메시지").grid(row=1, column=0, sticky='e')
        self.msg_entry = tk.Entry(root, width=40); self.msg_entry.grid(row=1, column=1, padx=4)

        tk.Button(root, text="전송", width=10, command=self.send).grid(row=2, column=0, columnspan=2, pady=8)
        self.status = tk.Label(root, text=""); self.status.grid(row=3, column=0, columnspan=2)

    def send(self):
        ip, msg = self.ip_entry.get().strip(), self.msg_entry.get().encode()
        try:
            with socket.create_connection((ip, SERVER_PORT), timeout=3) as s:
                s.sendall(msg)
            self.status.config(text="✅ 전송 성공")
        except Exception as e:
            self.status.config(text=f"❌ 오류: {e}")

if __name__ == "__main__":
    tk.Tk().after(0, lambda: ClientApp(tk._default_root)); tk.mainloop()
