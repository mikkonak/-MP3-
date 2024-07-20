import os
import subprocess
from tkinter import Tk, Label, Entry, Button, filedialog
from pydub import AudioSegment
from pydub.utils import which

# Указание пути к ffmpeg
AudioSegment.converter = which("ffmpeg")

def create_empty_mp3(file_path, duration):
    # Создание пустого аудио
    silent_audio = AudioSegment.silent(duration=duration*1000)  # Продолжительность в миллисекундах
    silent_audio.export(file_path, format="mp3")

def generate_files():
    try:
        duration = int(entry_duration.get())
        count = int(entry_count.get())
        folder_path = filedialog.askdirectory(title="Выберите папку для сохранения файлов")

        if not folder_path:
            return
        
        for i in range(count):
            file_name = f"{i + 1}.mp3"
            file_path = os.path.join(folder_path, file_name)
            create_empty_mp3(file_path, duration)

        # Открыть папку
        if os.name == 'nt':  # Windows
            os.startfile(folder_path)
        elif os.name == 'posix':  # macOS или Linux
            subprocess.Popen(['open', folder_path])
        
        print(f"Создано {count} пустых mp3 файлов в папке {folder_path}")
    except ValueError:
        print("Пожалуйста, введите корректные числовые значения для длительности и количества файлов.")

# Создание графического интерфейса
root = Tk()
root.title("Генератор пустых MP3 файлов")

Label(root, text="Длительность (в секундах):").grid(row=0, column=0)
entry_duration = Entry(root)
entry_duration.grid(row=0, column=1)

Label(root, text="Количество файлов:").grid(row=1, column=0)
entry_count = Entry(root)
entry_count.grid(row=1, column=1)

Button(root, text="Создать файлы", command=generate_files).grid(row=2, columnspan=2)

root.mainloop()
