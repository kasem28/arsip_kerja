import streamlit as st
import pandas as pd
from datetime import datetime

# Konfigurasi Halaman
st.set_page_config(page_title="Aplikasi Arsip Kerja", page_icon="📁", layout="wide")

# Inisialisasi Database Sederhana menggunakan Session State
if 'data_arsip' not in st.session_state:
    # Menambahkan kolom 'File Dokumentasi' ke dalam struktur data
    st.session_state.data_arsip = pd.DataFrame(columns=['Tanggal', 'Kategori', 'Judul Dokumen', 'Keterangan', 'File Dokumentasi'])

st.sidebar.title("📁 Menu Arsip")
menu = st.sidebar.radio("Navigasi:", [
    "Dashboard", 
    "Perangkat Pembelajaran", 
    "Administrasi BOS & ARKAS",
    "Administrasi Operator Sekolah", 
    "Praktikum & TEFA", 
    "Inventaris & Gudang",
    "Dokumentasi & Skrip"
])

# Fungsi untuk menambah arsip dengan fitur upload foto
def tambah_arsip(kategori):
    st.subheader(f"Tambah Arsip Baru: {kategori}")
    with st.form(key=f"form_{kategori}", clear_on_submit=True):
        judul = st.text_input("Judul Dokumen / Kegiatan")
        keterangan = st.text_area("Keterangan Singkat / Link Google Drive")
        
        # Fitur upload foto dokumentasi
        foto = st.file_uploader("Upload Foto Dokumentasi (Opsional)", type=["jpg", "jpeg", "png"])
        
        submit = st.form_submit_button("Simpan Arsip")
        
        if submit and judul:
            # Mengambil nama file jika ada foto yang diunggah
            nama_file = foto.name if foto is not None else "Tidak ada file"
            
            file_baru = pd.DataFrame({
                'Tanggal': [datetime.now().strftime("%Y-%m-%d %H:%M")],
                'Kategori': [kategori],
                'Judul Dokumen': [judul],
                'Keterangan': [keterangan],
                'File Dokumentasi': [nama_file]
            })
            st.session_state.data_arsip = pd.concat([st.session_state.data_arsip, file_baru], ignore_index=True)
            st.success("Arsip dan dokumentasi berhasil disimpan!")
        elif submit and not judul:
            st.error("Judul Dokumen wajib diisi!")

# Konten berdasarkan Menu
if menu == "Dashboard":
    st.title("🏠 Dashboard Arsip Kerja")
    st.write("Selamat datang di sistem pengarsipan digital.")
    st.write("### Riwayat Arsip Terbaru")
    if not st.session_state.data_arsip.empty:
        # Menampilkan dataframe dengan kolom yang baru
        st.dataframe(st.session_state.data_arsip.sort_values(by="Tanggal", ascending=False), use_container_width=True)
    else:
        st.info("Belum ada data yang diarsipkan.")

elif menu == "Perangkat Pembelajaran":
    st.title("📚 Arsip Perangkat Pembelajaran")
    st.write("Kelola Modul Ajar, CP, ATP, dan KKTP di sini.")
    tambah_arsip("Perangkat Pembelajaran")

elif menu == "Administrasi BOS & ARKAS":
    st.title("💰 Administrasi BOS & RKAS")
    st.write("Unggah link rekap Excel BKU dan catatan kode rekening ARKAS.")
    tambah_arsip("Administrasi BOS & ARKAS")

elif menu == "Administrasi Operator Sekolah":
    st.title("💻 Administrasi Operator Sekolah")
    st.write("Arsip data Dapodik, surat menyurat, pembaruan data siswa, pengajuan perangkat, dan dokumen operasional lainnya.")
    tambah_arsip("Administrasi Operator Sekolah")

elif menu == "Praktikum & TEFA":
    st.title("🧪 Dokumentasi Praktikum")
    st.write("Arsip SOP pembuatan produk, evaluasi biaya, dan proposal PWMP.")
    tambah_arsip("Praktikum & TEFA")

elif menu == "Inventaris & Gudang":
    st.title("📦 Inventaris Gudang")
    st.write("Laporan rotasi FIFO/FEFO dan pencatatan logistik bahan.")
    tambah_arsip("Inventaris & Gudang")

elif menu == "Dokumentasi & Skrip":
    st.title("🎥 Dokumentasi & Publikasi")
    st.write("Simpan draf skrip video, narasi kegiatan, dan aset desain visual.")
    tambah_arsip("Dokumentasi & Skrip")