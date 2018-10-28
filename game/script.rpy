define r = Character("Radon")
define t = Character("Tenta")
define a = Character("Azure")

label start:

    scene bg beach

    "Pada suatu hari di musim panas, di pantai dengan banyak para pedagang kaki lima, Radon dan Tenta sedang berjalan-jalan menyusuri pantai."

    t "Kak! Lihat! Ada permen warna-warni! Beli ya kak!"
    r "Hah? Ini uangnya, beli secukupnya ya!"
    "Beberapa saat kemudian"
    t "Kak! Maaf aku beli banyak, Ini untuk kakak satu ya! Hehe..."
    r "Dasar kamu ini ya"
    t "Kak! Lihat! Lihat! Balonnya lucu-lucu, boleh beli satu?"
    r "*Menghela nafas* Baiklah, tapi kamu beli sendiri ya, kakak tunggu disini"
    t "Siap kapten!"
    "Dan Tenta pergi membeli balon sendirian"
    "Tenta lama sekali membeli balonnya, hingga Radon panik dan mencari-cari Tenta"
    r "Tenta? Tenta!?"
    r "Tenta!? Kamu Dimana!?"
    "Setelah kesana kemari mencari Tenta, Radon merasa haus dan kelelahan"
    r "Duh badanku lemas dan Aku menjadi haus"
    r "Sebaiknya Aku mencari kedai jus buah di dekat sini..."
    "Setelah berjalan sedikit dengan energi yang tersisa, akhirnya Radon menemukan sebuah kedai jus"
    "Saat mendekati kedai tersebut, terlihat jelas papan bertuliskan \"Mood Cafe\""
    r "Wah! Akhirnya aku menemukan kedai jus!"
    r "Desain luarnya berwarna sekali dan penuh dengan gambar buah!"
    r "Baiklah, Sebaiknya aku berteduh dari panas terik sebentar dan memesan jus buah, lalu aku akan ke pusat informasi untuk mencari Tenta"
    "Akhirnya Radon masuk kedalam kedai jus tersebut"
    "Tampilan dalam kedai tersebut sangatlah berbeda dengan tampilan luarnya. Tampilan dalamnya memiliki suasana {i}halloween{/i}, serba misterius dan para {i}staff{/i}nya juga serba gelap"
    r "Hah?! Tempat apa ini?!"
    a "Selamat datang di Mood Cafe!"
    r "*bingung*"
    a "Silahkan duduk dimanapun nona suka!"
    r "Apakah aku boleh bertanya?"
    a "Silahkan, nona"
    r "Apakah ini benar-benar kedai jus buah? Kalau iya, mengapa tampilan dalamnya berbeda dengan tampilan luarnya?"
    a "Saya mohon maaf atas ketidaknyamanannya, nona. Anda tidak salah memilih tempat. Menu dan tema kedai ini disesuaikan dengan musim saat ini. Soal itu Saya sendiri tidak tahu mengapa pemilik kedai ini tidak merubah temanya menjadi musim panas"
    menu: 
        "Siapa pemilik kedai ini?": 
            jump a
        "Oh begitu ya...":
            jump end_a


    label end_a:
        r "Oh begitu ya..."
        r "M-maaf tuan, Saya harus mencari adik Saya. Saya mohon permisi"
        ".:. END"
        
    return
