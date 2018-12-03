define r = Character("Radon")
define t = Character("Tenta")
define a = Character("Azure")
define x = Character("Xon")

transform center:
    xalign 0.5
    yalign -0.1
    size (944/1.75, 1417/1.75)

transform left:
    xalign 0.1
    yalign -0.1
    size (944/1.75, 1417/1.75)

transform right:
    xalign 0.9
    yalign -0.1
    size (944/1.75, 1417/1.75)

transform walk_away:
    linear 0.25 xalign 1.5 alpha 0
    linear 0.25 yalign -0.1
    linear 0.25 size (944/1.75, 1417/1.75)

transform characterInitialState:
    xalign -1.5 alpha 0
    yalign -0.1
    size (944/1.75, 1417/1.75)
transform showCharacterFromLeft:
    linear 0.5 xalign 0.1 alpha 1
    linear 0.25 yalign -0.1
    linear 0.25 size (944/1.75, 1417/1.75)

transform goToCenterAnimate:
    linear 0.25 xalign 0.4
    linear 0.25 yalign -0.1
    linear 0.25 size (944/1.75, 1417/1.75)

transform dead:
    linear 0.25 xalign 0.1 yalign -0.1 size (944/1.75, 1417/1.75)
    linear 0.25 xalign 0.12 yalign -0.1 size (944/1.75, 1417/1.75)
    linear 0.25 xalign 0.098 yalign -0.1 size (944/1.75, 1417/1.75)
    linear 0.15 xalign 0.12 yalign -0.1 size (944/1.75, 1417/1.75)
    linear 0.15 xalign 0.098 yalign -0.1 size (944/1.75, 1417/1.75)
    linear 0.25 xalign 0.12 yalign -0.1 size (944/1.75, 1417/1.75)
    linear 0.15 xalign 0.090 yalign -0.1 size (944/1.75, 1417/1.75)
    linear 0.25 xalign 0.12 yalign -0.1 size (944/1.75, 1417/1.75)
    linear 0.15 xalign 0.098 yalign -0.1 size (944/1.75, 1417/1.75)
    linear 0.35 xalign 0.15 yalign -0.1 size (944/1.75, 1417/1.75)
    linear 0.15 xalign 0.098 yalign -0.1 size (944/1.75, 1417/1.75)
    linear 0.35 xalign 0.1 yalign -0.5 size (944/1.75, 1417/1.75)
    linear 0.35 xalign 0.1 yalign -0.5 size (944/1.75, 1417/1.75)
    linear 0.40 xalign -0.5 yalign -1.5 size (944/1.75, 1417/1.75) rotate -90
    linear 0.40 xalign -0.5 yalign -2.0 size (944/1.75, 1417/1.75) rotate -90
screen selectCard():
    frame: 
        xfill 1.0
        yfill 1.0
        background Image("images/dpnblkg_blur.jpg")
        hbox:
            xalign 0.5
            yalign 0.5
            button:
                background Frame("gui/tarot back.png")
                hover_background Frame("gui/tarot back hover.png")
                xmaximum (337/2)+20
                ymaximum 509/2
                left_margin 10
                right_margin 10
                action Return("1")
            button:
                background Frame("gui/tarot back.png")
                hover_background Frame("gui/tarot back hover.png")
                xmaximum (337/2)+20
                ymaximum 509/2
                left_margin 10
                right_margin 10
                action Return("2")
            button:
                background Frame("gui/tarot back.png")
                hover_background Frame("gui/tarot back hover.png")
                xmaximum (337/2)+20
                ymaximum 509/2
                left_margin 10
                right_margin 10
                action Return("3")

screen cardSelected(data):
    frame: 
        xfill 1.0
        yfill 1.0
        background Image("images/dpnblkg_blur.jpg")
        vbox:
            xalign 0.5
            yalign 0.5
            hbox:
                button:
                    if data == "1":
                        background Frame("gui/e1.png")
                    else:
                        background Frame("gui/tarot back.png")
                    xmaximum (337/2)+20
                    ymaximum 509/2
                    left_margin 10
                    right_margin 10
                button:
                    if data == "2":
                        background Frame("gui/e2.png")
                    else:
                        background Frame("gui/tarot back.png")
                    xmaximum (337/2)+20
                    ymaximum 509/2
                    left_margin 10
                    right_margin 10
                button:
                    if data == "3":
                        background Frame("gui/e3.png")
                    else:
                        background Frame("gui/tarot back.png")
                    xmaximum (337/2)+20
                    ymaximum 509/2
                    left_margin 10
                    right_margin 10
            textbutton "{color=#07b26a}Continue":
                top_margin 20
                xalign 0.5
                action Return("Done")

label start:

    scene pantai aja
    play music "audio/coconut.mp3"

    "Pada suatu hari di musim panas, di pantai dengan banyak para pedagang kaki lima, Radon dan Tenta sedang berjalan-jalan menyusuri pantai."

    show tenta_happy at center
    t "Kak! Lihat! Ada permen warna-warni! Beli ya kak!"
    show tenta_happy at right
    show radon_smile2 at left
    r "Hah? Ini uangnya, beli secukupnya ya!"
    hide tenta_happy
    hide radon_smile2
    "Beberapa saat kemudian"
    show tenta_happy at center
    t "Kak! Maaf aku beli banyak, Ini untuk kakak satu ya! Hehe..."
    show tenta_happy at right
    show radon_talk down2 at left
    r "Dasar kamu ini ya"
    t "Kak! Lihat! Lihat! Balonnya lucu-lucu, boleh beli satu?"
    hide radon_talk down2
    show radon_hah at left
    r "*Menghela nafas* Baiklah, tapi kamu beli sendiri ya, kakak tunggu disini"
    hide tenta_happy
    show tenta_happy2 at right
    t "Siap kapten!"
    show tenta_happy2 at walk_away 
    pause .5
    hide radon_hah
    hide tenta_happy2

    "Dan Tenta pergi membeli balon sendirian"
    
    "Tenta lama sekali membeli balonnya, hingga Radon panik dan mencari-cari Tenta"

    show radon_confuse at center
    r "Tenta? Tenta!?"
    r "Tenta!? Kamu Dimana!?"
    hide radon_confuse
    "Setelah kesana kemari mencari Tenta, Radon merasa haus dan kelelahan"
    show radon_hah at center
    r "Duh badanku lemas dan Aku menjadi haus"
    r "Sebaiknya Aku mencari kedai jus buah di dekat sini..."
    hide radon_hah
    scene kios 1
    "Setelah berjalan sedikit dengan energi yang tersisa, akhirnya Radon menemukan sebuah kedai jus"
    "Saat mendekati kedai tersebut, terlihat jelas papan bertuliskan \"Mood Cafe\""
    show radon_smile at center
    r "Wah! Akhirnya aku menemukan kedai jus!"
    r "Desain luarnya berwarna sekali dan penuh dengan gambar buah!"
    hide radon_smile
    show radon_smile2 at center
    r "Baiklah, Sebaiknya aku berteduh dari panas terik sebentar dan memesan jus buah, lalu aku akan ke pusat informasi untuk mencari Tenta"
    hide radon_smile2
    play sound "audio/bell.mp3"
    "Akhirnya Radon masuk kedalam kedai jus tersebut"
    show halloween cafe
    "Tampilan dalam kedai tersebut sangatlah berbeda dengan tampilan luarnya. Tampilan dalamnya memiliki suasana {i}halloween{/i}, serba misterius dan para {i}staff{/i}nya juga serba gelap"
    show radon_suspicious at center
    r "Hah?! Tempat apa ini?!"
    show radon_suspicious at left
    show azure_smile at right
    a "Selamat datang di Mood Cafe!"
    hide radon_suspicious
    show radon_confuse at left
    r "*bingung*"
    a "Silahkan duduk dimanapun nona suka!"
    r "Apakah aku boleh bertanya?"
    a "Silahkan, nona"
    r "Apakah ini benar-benar kedai jus buah? Kalau iya, mengapa tampilan dalamnya berbeda dengan tampilan luarnya?"
    a "Saya mohon maaf atas ketidaknyamanannya, nona. Anda tidak salah memilih tempat."
    hide azure_smile
    show azure_talk at right
    a "Menu dan tema kedai ini disesuaikan dengan musim saat ini." 
    a "Soal itu Saya sendiri tidak tahu mengapa pemilik kedai ini tidak merubah temanya menjadi musim panas"
    hide radon_confuse
    hide azure_talk
    menu: 
        "Siapa pemilik kedai ini?": 
            jump cont_a
        "Oh begitu ya...":
            jump end_a
    return

label end_a:
        show radon_smile at center
        r "Oh begitu ya..."
        r "M-maaf tuan, Saya harus mencari adik Saya. Saya mohon permisi"
        show radon_smile at left
        show azure_smile at right
        a "Baiklah, Terimakasih!"
        hide radon_smile
        hide azure_smile
        scene cg out
        ".:. END"

return

label cont_a:
    show radon_confuse at center
    r "Siapa pemilik kedai ini?"
    show radon_confuse at left
    show azure_smile at right
    a "Saya tidak tahu siapa pemiliknya, tetapi setahu Saya pemilik cafe ini sangat baik dan ramah"
    hide radon_confuse
    show radon_hah at left
    r "Baiklah, apa saja yang ada di dalam menu?"
    hide azure_smile
    show azure_talk at right
    a "Anda harus memilih menu dari 3 kartu yang Saya sediakan"
    hide radon_hah
    show radon_confuse at left
    r "M-Maksud Anda?"
    hide azure_talk
    show azure_smile at right
    a "Pilihlah salah satu dari 3 kartu yang Saya sediakan. Kartu yang Anda pilih sesuai dengan suasana hati Anda saat ini"
    scene dpnblkg
    hide azure_smile
    hide radon_confuse
    call screen selectCard
    if _return == "1":
        jump card_a
    elif _return == "2":
        jump card_b
    elif _return == "3":
        jump card_c
    return

label card_a:
    call screen cardSelected("1")
    show azure_smile at center
    a "Silakan pilih salah satu dari 3 kartu ini, Nona"
    show azure_smile at right
    show radon_talk down2 at left
    r "Baiklah, Aku pilih yang pertama"
    hide azure_smile
    hide radon_talk down2
    "*Kartu yang keluar adalah kartu yang bergambar tengkorak dan malaikat pencabut nyawa*"
    show azure_smile at center
    a "Pilihan yang bagus, silakan diminum Nona"
    show azure_smile at right
    show radon_smile2 at left
    r "Rasanya seperti anggur ya"
    a "Ya, itu adalah jus anggur"
    hide radon_smile2
    show radon_confuse at left
    r "Kok perutku tiba-tiba berasa sangat sakit ya?"
    hide azure_smile
    "Lalu Radon meminum jus tersebut hingga habis"
    show radon_confuse at dead
    pause 6
    hide radon_confuse
    # r "I don't feel so good, Mr. Stark"
    scene ending 1
    "Setelah menghabiskan jusnya, Radon terjatuh dan tewas" #menjadi abu
    ".:. END"
    return

label card_b:
    call screen cardSelected("2")
    show azure_smile at center
    a "Silakan pilih salah satu dari 3 kartu ini, Nona"
    show azure_smile at right
    show radon_talk close2 at left
    r "Baiklah, Aku pilih yang kedua"
    a "Pilihan yang menarik, silakan diminum!"
    hide radon_talk close2
    show radon_smile2 at left
    "*Kartu yang terpilih bergambar sarang laba-laba*"
    r "Hmmmmm"
    a "Bagaimana rasanya?"
    hide radon_smile2
    show radon_confuse at left
    r "Rasanya seperti buah apel. Tapi kepalaku tiba-tiba pusing dan perutku mual"
    hide azure_smile
    show azure_smile2 at right
    a "Fufufu~"
    r "?!"
    hide radon_confuse
    "Radon kehilangan kesadaran dan menjadi seperi orang yang kerasukan"
    show shon_biasa at left
    a "Xon! Bawakan Aku kandang!" #Execute Order 66!
    hide azure_smile2
    hide shon_biasa
    show shon_yes at right
    x "Baik!"
    hide shon_yes
    show shon_hmm at right
    show azure_smile2:
        xalign 0.75
        yalign -0.1
        size (944/1.75, 1417/1.75)
    a "Kurung dia! Bawakan Ia ke lab agar bisa kujadikan eksperimen! *Tertawa jahat*"
    scene ending 2
    ".:. END"
    return
label card_c:
    call screen cardSelected("3")
    show azure_smile at center
    a "Silakan pilih salah satu dari 3 kartu, Nona"
    show azure_smile at right
    show radon_talk close2 at left
    r "Baiklah, Aku pilih yang ketiga"
    "Azure kaget karena Ia belum pernah melihat kartu ini sebelumnya"
    hide radon_talk close2
    show radon_talk2 at left
    r "Wah, Rasanya unik! Rasanya seperti 5 buah yang dicampur, tapi ini enak!"
    stop music fadeout 1
    play music "audio/berubah.mp3"
    hide azure_smile
    show azure_battle at right
    a "?!"
    hide radon_talk2
    show pinces_ladon at left
    "Radon tiba-tiba bercahaya dan tiba-tiba terdapat 5 cincin yang berbentuk buah"
    show tenta_surprised at characterInitialState
    show pinces_ladon at goToCenterAnimate
    show tenta_surprised at showCharacterFromLeft
    pause .5
    t "KAKAK! TERNYATA KAMU DISINI!.... HAH?!.... DEWI?!"
    a "Baiklah, ayo kita selesaikan masalah ini!"
    return



label credits:
    show screen about()



