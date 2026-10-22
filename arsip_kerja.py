import streamlit as st
import pandas as pd
from datetime import datetime

# Konfigurasi Halaman
st.set_page_config(page_title="Aplikasi Arsip Kerja", page_icon="📁", layout="wide")

# Inisialisasi Database Sederhana menggunakan Session State
if 'data_arsip' not in st.session_state:
    st.session_state.data_arsip = pd.DataFrame(columns=['Tanggal', 'Kategori', 'Judul Dokumen', 'Keterangan'])

st.sidebar.title("📁 Menu Arsip")
menu = st.sidebar.radio("Navigasi:", [
    "Dashboard", 
    "Perangkat Pembelajaran", 
    "Administrasi BOS & ARKAS", 
    "Praktikum & TEFA", 
    "Inventaris & Gudang",
    "Dokumentasi & Skrip"
])

# Fungsi untuk menambah arsip
def tambah_arsip(kategori):
    st.subheader(f"Tambah Arsip Baru: {kategori}")
    with st.form(key=f"form_{kategori}"):
        judul = st.text_input("Judul Dokumen / Kegiatan")
        keterangan = st.text_area("Keterangan Singkat / Link Google Drive")
        submit = st.form_submit_button("Simpan Arsip")
        
        if submit and judul:
            file_baru = pd.DataFrame({
                'Tanggal': [datetime.now().strftime("%Y-%m-%d %H:%M")],
                'Kategori': [kategori],
                'Judul Dokumen': [judul],
                'Keterangan': [keterangan]
            })
            st.session_state.data_arsip = pd.concat([st.session_state.data_arsip, file_baru], ignore_index=True)
            st.success("Arsip berhasil disimpan!")

# Konten berdasarkan Menu
if menu == "Dashboard":
    st.title("🏠 Dashboard Arsip Kerja")
    st.write("Selamat datang di sistem pengarsipan digital.")
    st.write("### Riwayat Arsip Terbaru")
    if not st.session_state.data_arsip.empty:
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
    st.write("Simpan draf skrip video kunjungan, narasi revitalisasi, dan aset desain label.")
    tambah_arsip("Dokumentasi & Skrip")