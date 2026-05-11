import hashlib

def tugas_integritas_data():
    print("=== PROGRAM PENGECEK PERUBAHAN DATA PROFIL (MD5) ===")
    
    # 1. Menerima input data user awal
    nama = input("Masukkan Nama     : ")
    email = input("Masukkan Email    : ")
    hp = input("Masukkan Nomor HP : ")
    
    # Gabungkan data jadi satu string untuk di-hash
    data_awal = f"{nama}{email}{hp}"
    
    # 2. Membuat hash MD5 dari data awal
    hash_awal = hashlib.md5(data_awal.encode()).hexdigest()
    
    print(f"\nHash MD5 Awal Berhasil Disimpan: {hash_awal}")
    print("-" * 40)
    
    # 3. Menerima input data baru untuk dibandingkan
    print("\n[ Simulasi Perubahan Data ]")
    nama_baru = input("Masukkan Nama Baru     : ")
    email_baru = input("Masukkan Email Baru    : ")
    hp_baru = input("Masukkan Nomor HP Baru : ")
    
    data_baru = f"{nama_baru}{email_baru}{hp_baru}"
    
    # 4. Membuat hash MD5 dari data baru
    hash_baru = hashlib.md5(data_baru.encode()).hexdigest()
    
    # 5. Membandingkan dan menampilkan hasil
    print(f"\nHash Lama: {hash_awal}")
    print(f"Hash Baru: {hash_baru}")
    
    print("\n--- STATUS PERUBAHAN DATA ---")
    if hash_awal == hash_baru:
        print("Status: DATA TIDAK BERUBAH (Aman)")
    else:
        print("Status: DATA TELAH BERUBAH / DIMODIFIKASI!")

if __name__ == "__main__":
    tugas_integritas_data()