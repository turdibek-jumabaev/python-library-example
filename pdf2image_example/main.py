"""
        Turdibek Jumabaev - https://t.me/turdibekjumabaev
                                                            """


# pdf2image - tashqi kutubxona
# pip install pdf2image
from pdf2image import convert_from_path


# example.pdf - fayl nomi
images = convert_from_path('example.pdf')

for i in range(len(images)):

    # sahifalarni alohida rasmlarga saqlash
    images[i].save('page' + str(i) + '.jpg', 'JPEG')
