menu = [
        ["Nasi goreng : Rp. 15.000", "Ayam kremes : Rp 17.000", "Mie ayam : Rp 13.000"],
        ["Bakso  :  Rp 13.000", "Soto ayam  :  Rp 12.000", "Es Teh  :  Rp 5.000"],
        ["Teh hangat  :  Rp 5.000", "Es Jeruk  :  Rp 7.000", "Jeruk hangat  :  Rp 7.000"]
        ]

for m in menu:
        print(m)


pilihan = "y"
while pilihan == "y":
        print("""
        a. Menambah menu makanan/ minuman
        b. Menghapus menu makanan/ minuman 
        c. Mengubah nama menu makanan / minuman
        """)

        pertanyaan = input("Ingin memilih opsi apa?: ")
        if pertanyaan=="a":
                ttambah = input("ingin menambahkan menu di?\nx. Menambah dibelakang\ny. Menambang ditengah\n")
                if ttambah =="x":
                        tambahbelakang = input("Makanan/minuman yang ditambahkan: ")
                        menu.append(tambahbelakang)
                        for m in menu:
                            print(m)
                elif ttambah =="y":
                        tambahtengah = input("Makanan/ minuman yang ditambahkan: ")
                        baris = int(input("Baris: "))
                        kolom = int(input("Kolom: "))
                        menu.insert([baris][kolom], tambahtengah)
                        for m in menu:
                            print(m)
        elif pertanyaan =="b":
                gganti = input("Ingin menggunakan metode?\nx. Del\ny. Remove()\n")
                if gganti == "x":
                        barishapus1 = int(input("Menu dari baris ke-: "))
                        kolomhapus1 = int(input("Menu dari kolom ke-: "))
                        del menu[barishapus1][kolomhapus1]
                        for m in menu:
                            print(m)
                        
                elif gganti == "y":
                        barishapus2 = int(input("Menu dari baris ke-: "))
                        kolomhapus2 = int(input("Menu dari kolom ke-: "))
                        menu.remove(barishapus2,kolomhapus2)
                        for m in menu:
                            print(m)
        else:
#menu awal                
                menu = [
                        ["Nasi goreng : Rp. 15.000", "Ayam kremes : Rp 17.000", "Mie ayam : Rp 13.000"],
                        ["Bakso  :  Rp 13.000", "Soto ayam  :  Rp 12.000", "Es Teh  :  Rp 5.000"],
                        ["Teh hangat  :  Rp 5.000", "Es Jeruk  :  Rp 7.000", "Jeruk hangat  :  Rp 7.000"]
                        ]
                print("data pertama: ", menu)
                menu[0]="Ayam bakar : Rp. 15.000"
                print("\ndata perubahan: ",menu)

        pilihan=input("apakah anda ingin melakukan opsi selanjutnya Y/N= ")