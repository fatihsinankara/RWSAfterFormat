import wget

output_directory = "dlcache"

welcome = """
    #####################################################
    # Merhaba.                                          #
    # RWS After Format programına hoşgeldiniz.          #
    # Lütfen kurmak istediğiniz programın numarasını    #
    # yazıp 'Enter' tuşuna basın.                       #
    #####################################################
"""
programlist = """
    Tarayıcılar:
    (1) Google Chrome
    (2) Opera
    (3) Vivaldi
    (4) Firefox

    Virüs Programları:
    (5) Avast Free
    (6) AVG Free

    Diğer:
    (7) Winrar
    (8) 7-Zip
    (9) Steam
    (10) Discord

"""
print (welcome)
print (programlist)
secim = input("Lütfen kurmak istediğiniz programı tuşlayınız: ")