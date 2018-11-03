define r = Character("Radon")
define t = Character("Tenta")
define a = Character("Azure")
define x = Character("Xon")

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
            jump cont_a
        "Oh begitu ya...":
            jump end_a
    return

label end_a:
        r "Oh begitu ya..."
        r "M-maaf tuan, Saya harus mencari adik Saya. Saya mohon permisi"
        a "Baiklah, Terimakasih!"
        ".:. END"

return

label cont_a:
    r "Siapa pemilik kedai ini?"
    a "Saya tidak tahu siapa pemiliknya, tetapi setahu Saya pemilik cafe ini sangat baik dan ramah"
    r "Baiklah, apa saja yang ada di dalam menu?"
    a "Anda harus memilih menu dari 3 kartu yang Saya sediakan"
    r "M-Maksud Anda?"
    a "Pilihlah salah satu dari 3 kartu yang Saya sediakan. Kartu yang Anda pilih sesuai dengan suasana hati Anda saat ini"
    menu optional_name:
        "Pilih Kartu"
        "Kartu A":
            jump card_a
        "Kartu B":
            jump card_b
        "Kartu C":
            jump card_c
    return

label card_a:
    a "Silakan pilih salah satu dari 3 kartu ini, Nona"
    r "Baiklah, Aku pilih yang pertama"
    "*Kartu yang keluar adalah kartu yang bergambar tengkorak dan malaikat pencabut nyawa*"
    a "Pilihan yang bagus, silakan diminum Nona"
    r "Rasanya seperti anggur ya"
    a "Ya, itu adalah jus anggur"
    r "Kok perutku tiba-tiba berasa sangat sakit ya?"
    "Lalu Radon meminum jus tersebut hingga habis"
    # r "I don't feel so good, Mr. Stark"
    "Setelah menghabiskan jusnya, Radon terjatuh dan tewas" #menjadi abu
    ".:. END"
    return

label card_b:
    a "Silakan pilih salah satu dari 3 kartu ini, Nona"
    r "Baiklah, Aku pilih yang kedua"
    a "Pilihan yang menarik, silakan diminum!"
    "*Kartu yang terpilih bergambar sarang laba-laba*"
    r "Hmmmmm"
    a "Bagaimana rasanya?"
    r "Rasanya seperti buah apel. Tapi kepalaku tiba-tiba pusing dan perutku mual"
    a "Fufufu~"
    r "?!"
    "Radon kehilangan kesadaran dan menjadi seperi orang yang kerasukan"
    a "Xon! Bawakan Aku kandang!" #Execute Order 66!
    x "Baik!"
    a "Kurung dia! Bawakan Ia ke lab agar bisa kujadikan eksperimen! *Tertawa jahat*"
    ".:. END"
    return
label card_c:
    a "Silakan pilih salah satu dari 3 kartu, Nona"
    r "Baiklah, Aku pilih yang ketiga"
    "Azure kaget karena Ia belum pernah melihat kartu ini sebelumnya"
    r "Wah, Rasanya unik! Rasanya seperti 5 buah yang dicampur, tapi ini enak!"
    a "?!"
    "Radon tiba-tiba bercahaya dan tiba-tiba terdapat 5 cincin yang berbentuk buah"
    t "KAKAK! TERNYATA KAMU DISINI!.... HAH?!.... DEWI?!"
    a "Baiklah, ayo kita selesaikan masalah ini!"
    return