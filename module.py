import program_data as pdata

while True:
    print('='*25) 
    print("SELAMAT DATANG DI PROGRAM MANAGEMENT")
    print('='*25) 
    pdata.menu()
    pilihan = int(input('Masukan Pilihan : '))

    if pilihan == 1:
        pdata.tambahkan_barang()
    if pilihan == 2:
        pdata.edit_data()
    if pilihan == 3:
        pdata.menghapus()
    if pilihan == 4:
        pdata.cari_data()
    if pilihan == 5:
        pdata.data_barang()
    if pilihan == 6:
        pdata.jumlah_data()
    if pilihan == 7:
        print('='*25)  
        print("TERIMAKASIH")  
        print('='*25)
        exit()  