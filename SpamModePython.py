import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import keyboard

class SpamModeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SPAM MODE - Made by CiMi131")
        self.root.geometry("440x500")
        self.root.configure(bg="#121212")
        self.root.resizable(False, False)
        
        self.is_running = False
        self.current_hotkey = "f6"
        
        # Stil Ayarları
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure(
            "TCombobox", 
            fieldbackground="#2a2a2a", 
            background="#121212", 
            foreground="white", 
            arrowcolor="white",
            bordercolor="#2a2a2a"
        )
        
        # Başlık (Beyaz yapıldı)
        self.title_label = tk.Label(self.root, text="SPAM MODE", bg="#121212", fg="white", font=("Consolas", 16, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(20, 15))
        
        # Durum Paneli
        self.status_frame = tk.Frame(self.root, bg="#121212")
        self.status_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=30, pady=(0, 15))
        
        self.run_var = tk.BooleanVar(value=False)
        self.start_chk = tk.Checkbutton(
            self.status_frame, 
            text="Spam Modunu Etkinleştir", 
            variable=self.run_var, 
            command=self.on_toggle,
            bg="#121212", 
            fg="white", 
            selectcolor="#2a2a2a", 
            activebackground="#121212", 
            activeforeground="white", 
            font=("Consolas", 10, "bold")
        )
        self.start_chk.pack(side="left")
        
        # Durum Etiketi (İlk açılış rengi Beyaz yapıldı)
        self.status_label = tk.Label(self.status_frame, text="Durduruldu", bg="#121212", fg="white", font=("Consolas", 10, "bold"))
        self.status_label.pack(side="right")
        
        # Giriş Alanları Tasarımı
        label_config = {"bg": "#121212", "fg": "#aaaaaa", "font": ("Consolas", 9, "bold")}
        entry_config = {"bg": "#2a2a2a", "fg": "#ffffff", "relief": "flat", "insertbackground": "white", "font": ("Consolas", 10)}
        
        # 1. Yazılacak Yazı
        tk.Label(self.root, text="YAZILACAK YAZI :", **label_config).grid(row=2, column=0, sticky="nw", padx=(30, 10), pady=10)
        self.text_entry = tk.Text(self.root, height=4, width=30, **entry_config, highlightthickness=1, highlightbackground="#3a3a3a", highlightcolor="#ffffff")
        self.text_entry.grid(row=2, column=1, sticky="w", pady=10)
        
        # 2. MS Başına Spam
        tk.Label(self.root, text="MS BAŞINA SPAM :", **label_config).grid(row=3, column=0, sticky="w", padx=(30, 10), pady=10)
        self.ms_entry = tk.Entry(self.root, width=30, **entry_config, highlightthickness=1, highlightbackground="#3a3a3a", highlightcolor="#ffffff")
        self.ms_entry.grid(row=3, column=1, sticky="w", pady=10)
        
        # 3. Spam Limiti
        tk.Label(self.root, text="SPAM LİMİTİ :", **label_config).grid(row=4, column=0, sticky="w", padx=(30, 10), pady=10)
        self.limit_entry = tk.Entry(self.root, width=30, **entry_config, highlightthickness=1, highlightbackground="#3a3a3a", highlightcolor="#ffffff")
        self.limit_entry.grid(row=4, column=1, sticky="w", pady=10)
        
        # 4. Basılacak Tuşlar
        tk.Label(self.root, text="BASILACAK TUŞLAR :", **label_config).grid(row=5, column=0, sticky="w", padx=(30, 10), pady=10)
        self.enter_var = tk.BooleanVar(value=True)
        self.chk = tk.Checkbutton(self.root, text="ENTER", variable=self.enter_var, bg="#121212", fg="white", selectcolor="#2a2a2a", activebackground="#121212", activeforeground="white", font=("Consolas", 9, "bold"))
        self.chk.grid(row=5, column=1, sticky="w", pady=10)
        
        # 5. Özel Modlar
        tk.Label(self.root, text="ÖZEL MODLAR :", **label_config).grid(row=6, column=0, sticky="w", padx=(30, 10), pady=10)
        self.whatsapp_var = tk.BooleanVar(value=False)
        self.wa_chk = tk.Checkbutton(self.root, text="WhatsApp Modu (275 ms)", variable=self.whatsapp_var, command=self.on_whatsapp_toggle, bg="#121212", fg="white", selectcolor="#2a2a2a", activebackground="#121212", activeforeground="white", font=("Consolas", 9, "bold"))
        self.wa_chk.grid(row=6, column=1, sticky="w", pady=10)
        
        # 6. Hotkey Seçimi
        tk.Label(self.root, text="HOTKEY SEÇİMİ :", **label_config).grid(row=7, column=0, sticky="w", padx=(30, 10), pady=10)
        
        hotkey_options = [
            "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12",
            "ctrl+shift+alt+s", "ctrl+shift+alt+a", "ctrl+shift+alt+w", "ctrl+shift+alt+x",
            "ctrl+shift+s", "ctrl+shift+a", "ctrl+alt+w", "ctrl+alt+s"
        ]
        self.hotkey_combo = ttk.Combobox(self.root, values=hotkey_options, width=28, state="readonly", font=("Consolas", 9))
        self.hotkey_combo.set("f6")
        self.hotkey_combo.grid(row=7, column=1, sticky="w", pady=10)
        self.hotkey_combo.bind("<<ComboboxSelected>>", self.update_hotkey)
        
        # Placeholder Tanımlamaları
        self.placeholders = {
            "text": "örnek : a",
            "ms": "1sn 1000ms dir",
            "limit": "örnek: 500 (opsiyonel)"
        }
        self.setup_placeholders()
        self.hotkey_handler = keyboard.add_hotkey(self.current_hotkey, lambda: self.root.after(0, self.toggle_via_hotkey))

    def setup_placeholders(self):
        # Text Entry Placeholder
        self.text_entry.insert("1.0", self.placeholders["text"])
        self.text_entry.config(fg="#777777")
        self.text_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(self.text_entry, self.placeholders["text"], is_text_widget=True))
        self.text_entry.bind("<FocusOut>", lambda e: self.set_placeholder(self.text_entry, self.placeholders["text"], is_text_widget=True))

        # MS Entry Placeholder
        self.ms_entry.insert(0, self.placeholders["ms"])
        self.ms_entry.config(fg="#777777")
        self.ms_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(self.ms_entry, self.placeholders["ms"]))
        self.ms_entry.bind("<FocusOut>", lambda e: self.set_placeholder(self.ms_entry, self.placeholders["ms"]))

        # Limit Entry Placeholder
        self.limit_entry.insert(0, self.placeholders["limit"])
        self.limit_entry.config(fg="#777777")
        self.limit_entry.bind("<FocusIn>", lambda e: self.clear_placeholder(self.limit_entry, self.placeholders["limit"]))
        self.limit_entry.bind("<FocusOut>", lambda e: self.set_placeholder(self.limit_entry, self.placeholders["limit"]))

    def clear_placeholder(self, widget, placeholder_text, is_text_widget=False):
        content = widget.get("1.0", "end-1c") if is_text_widget else widget.get()
        if content == placeholder_text:
            if is_text_widget:
                widget.delete("1.0", "end")
            else:
                widget.delete(0, "end")
            widget.config(fg="#ffffff")

    def set_placeholder(self, widget, placeholder_text, is_text_widget=False):
        content = widget.get("1.0", "end-1c").strip() if is_text_widget else widget.get().strip()
        if not content:
            if is_text_widget:
                widget.insert("1.0", placeholder_text)
            else:
                widget.insert(0, placeholder_text)
            widget.config(fg="#777777")

    def validate_inputs(self):
        text_val = self.text_entry.get("1.0", "end-1c").strip()
        ms_val = self.ms_entry.get().strip()

        if not text_val or text_val == self.placeholders["text"]:
            messagebox.showwarning("Eksik Bilgi", "Yazılacak yazı alanı boş bırakılamaz!")
            return False

        if not self.whatsapp_var.get():
            if not ms_val or ms_val == self.placeholders["ms"]:
                messagebox.showwarning("Eksik Bilgi", "MS Başına Spam alanı boş bırakılamaz!")
                return False
            if not ms_val.isdigit():
                messagebox.showwarning("Geçersiz Değer", "MS değeri sadece sayılardan oluşmalıdır!")
                return False

        return True

    def on_whatsapp_toggle(self):
        if self.whatsapp_var.get() and not self.run_var.get():
            self.ms_entry.config(state="disabled")
        elif not self.whatsapp_var.get() and not self.run_var.get():
            self.ms_entry.config(state="normal")

    def set_widgets_state(self, state):
        self.text_entry.config(state=state)
        if state == "disabled":
            self.ms_entry.config(state="disabled")
        else:
            if self.whatsapp_var.get():
                self.ms_entry.config(state="disabled")
            else:
                self.ms_entry.config(state="normal")
        self.limit_entry.config(state=state)
        self.chk.config(state=state)
        self.wa_chk.config(state=state)
        self.hotkey_combo.config(state=state)

    def update_hotkey(self, event=None):
        new_key = self.hotkey_combo.get()
        if new_key and new_key != self.current_hotkey:
            try:
                keyboard.remove_hotkey(self.hotkey_handler)
            except:
                pass
            self.current_hotkey = new_key
            try:
                self.hotkey_handler = keyboard.add_hotkey(self.current_hotkey, lambda: self.root.after(0, self.toggle_via_hotkey))
            except:
                pass

    def on_toggle(self):
        if self.run_var.get():
            if not self.validate_inputs():
                self.run_var.set(False)
                return
            self.set_widgets_state("disabled")
            self.start_countdown(3)
        else:
            self.stop_spam()

    def toggle_via_hotkey(self):
        if self.run_var.get():
            self.run_var.set(False)
            self.stop_spam()
        else:
            if not self.validate_inputs():
                return
            self.run_var.set(True)
            self.set_widgets_state("disabled")
            self.start_countdown(3)

    def start_countdown(self, seconds):
        if not self.run_var.get():
            return
        if seconds > 0:
            # Geri sayım metni rengi Beyaz yapıldı
            self.status_label.config(text=f"{seconds}...", fg="white")
            self.root.after(1000, lambda: self.start_countdown(seconds - 1))
        else:
            # Çalışıyor metni rengi Beyaz yapıldı
            self.status_label.config(text="Çalışıyor", fg="white")
            self.is_running = True
            threading.Thread(target=self.spam_loop, daemon=True).start()

    def stop_spam(self):
        self.is_running = False
        # Durduruldu metni rengi Beyaz yapıldı
        self.status_label.config(text="Durduruldu", fg="white")
        self.set_widgets_state("normal")

    def spam_loop(self):
        text_to_send = self.text_entry.get("1.0", "end-1c")
        
        if self.whatsapp_var.get():
            delay = 0.275
        else:
            ms_text = self.ms_entry.get()
            delay = max(0.001, float(ms_text) / 1000.0)
            
        limit_text = self.limit_entry.get()
        if limit_text == self.placeholders["limit"] or not limit_text.isdigit():
            limit = -1
        else:
            limit = int(limit_text)
            
        count = 0
        while self.is_running and self.run_var.get():
            if limit != -1 and count >= limit:
                self.root.after(0, self.safe_stop_ui)
                break
            keyboard.write(text_to_send)
            if self.enter_var.get():
                keyboard.press_and_release("enter")
            count += 1
            time.sleep(delay)

    def safe_stop_ui(self):
        self.run_var.set(False)
        self.stop_spam()

if __name__ == "__main__":
    root = tk.Tk()
    app = SpamModeApp(root)
    root.mainloop()