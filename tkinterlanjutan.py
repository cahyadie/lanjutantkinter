import tkinter as tk
import sqlite3

def simpan_data_ke_sqlite(nama_siswa, biologi, fisika, inggris, prediksi_fakultas):
    # Membuka atau membuat database SQLite
    conn = sqlite3.connect("C:\D\Python\HI\AS.db")
    cursor = conn.cursor()
    
    # Membuat tabel jika belum ada
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nama_siswa str, 
                    biologi int,
                    fisika int,
                    inggris int,
                    prediksi_fakultas text)''')
    
    # Memasukkan data nilai ke dalam tabel
    cursor.execute("INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas) VALUES (?, ?, ?, ?, ?)",
                   (nama_siswa, biologi, fisika, inggris, prediksi_fakultas))
    
    # Melakukan commit dan menutup koneksi
    conn.commit()
    conn.close()


window = tk.Tk()
window.geometry("600x600")
window.title("Aplikasi Prediksi Prodi Pilihan")
    
def hasil():
    hasil_prediksi = tk.Label(frame, text= "Teknologi informasi")
    hasil_prediksi.grid(row = 10, column= 0, padx = 10, pady= 10)
    nama_siswa = str(entry1.get())
    biologi= int(entry2.get())
    fisika = int(entry3.get())
    inggris = int(entry4.get())
    
    if biologi > fisika and biologi > inggris:
        prediksi_fakultas = " kedokteran"
    
    elif fisika > biologi and fisika > inggris:
        prediksi_fakultas = " Teknik"
    
    elif inggris > fisika and inggris > biologi:
        prediksi_fakultas = " Bahasa "

    else:
        prediksi_fakultas = "Tidak terprediksi"
    

    simpan_data_ke_sqlite(nama_siswa, biologi, fisika, inggris, prediksi_fakultas)


#create frame
frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

#create entry (textbox)
entry1 = tk.Entry(frame)
entry2 = tk.Entry(frame)
entry3 = tk.Entry(frame)
entry4 = tk.Entry(frame)


#create label
welcomeText = tk.Label(frame, text="Aplikasi Prediksi Prodi Pilihan")
Label1 = tk.Label(frame, text="Nama_siswa")
Label2 = tk.Label(frame, text="Nilai biologi")
Label3 = tk.Label(frame, text="Nilai fisika")
Label4 = tk.Label(frame, text="Nilai inggris")

button = tk.Button(frame, text="Hasil prediksi",command=hasil)


welcomeText.grid(row = 0, column = 0, padx= 10, pady= 10)
Label1.grid(row = 1, column= 0, padx = 10, pady=10)
entry1.grid(row = 2, column= 0, padx = 10, pady= 10)
Label2.grid(row = 3, column= 0, padx = 10, pady=10)
entry2.grid(row = 4, column= 0, padx = 10, pady= 10)
Label3.grid(row = 5, column= 0, padx = 10, pady=10)
entry3.grid(row = 6, column= 0, padx = 10, pady= 10)
Label4.grid(row = 7, column= 0, padx = 10, pady=10)
entry4.grid(row = 8, column= 0, padx = 10, pady= 10)


button.grid(row = 9, column= 0, padx = 10, pady= 10,) 


window.mainloop()