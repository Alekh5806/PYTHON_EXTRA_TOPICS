import socket
import os 
from tkinter import ttk
from tkinter import *
from tkinter import filedialog , messagebox
import time

def send_file():
  filepath = filedialog.askopenfilename()
  if not filepath :
    return
  
  filename = os.path.basename(filepath)
  filesize = os.path.getsize(filepath)

  try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1',5000))
    
    client.send(f"{filename}|{filesize}\n".encode())

    with open(filepath, "rb") as f:
      sent = 0
      while True:
          data = f.read(1024)
          if not data:
              break

          client.send(data)
          sent += len(data)

          percent = (sent / filesize) * 100
          progress['value'] = percent

          root.update()
          time.sleep(0.01)
    
    client.send("END".encode())
    client.close()

    messagebox.showinfo("Success","File sent successfully!")
  
  except Exception as e:
    messagebox.showerror("Error",f"Failed to send file: {str(e)}")

# GUI setup 

root = Tk()
root.title("File Transfer Chat App")

Button(root,text = "Send File",command = send_file).pack(pady=20)
progress_label = Label(root,text="Progress:0%")
progress_label.pack(pady=10)
progress = ttk.Progressbar(root,orient=HORIZONTAL,length=300,mode='determinate')
progress.pack(pady=10)

root.mainloop()