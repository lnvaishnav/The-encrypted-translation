from translate import Translator                    # For Translating Text
from fpdf import FPDF                               # For Converting Text into PDF File
from PyPDF2 import PdfFileReader, PdfFileWriter     # For PDF encryption
import getpass, sys                                 # User password input in hidden

normalText = []
languageCode = []
translatedText = []
finalText1 = []
finalText2 = []

x = int(input("The data is in two way for translating \nEnter 1 = saved file's translation \n      2 = manual\nEnter Your Choice: "))
if x == 1:
    n = int(input("Enter the language which you wanna translate the data: \n1.Japaneese 2.Korean 3.Portuguese "))
    if n == 1:
        translator= Translator(to_lang="ja")    # This mode provides the language for converting entered data
    elif n == 2:
        translator= Translator(to_lang="ko")
    elif n == 3:
        translator= Translator(to_lang="pt")
    else:
        print("Thanks!!")
        exit(0)

    try:
        with open('TextFile.txt', mode = 'r') as translation_file:     # For translating purpose
            text_data = translation_file.read()
            translated_data = translator.translate(text_data)
            print(translated_data)
        
        with open('output_data.txt', mode = 'w') as translation_file2:
            translation_file2.write(translated_data)

    except:
        print("File doesn't exist!!")

elif x == 2:
    print("NOTICE: The maximum limit is 500 characters only including white spaces also!")
    new_text_file = str(input("Enter file name for saving your input: "))
    new_text_file_save = str(input(f"Enter the name for {new_text_file} to saving its translated text: "))

    def translatingFn():
        user_text = str(input("Enter the text you want to translate: "))
        normalText.append(user_text)
        print("\nPlease check the language code here: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes")
        language_code = str(input("Please input the language code: "))
        languageCode.append(language_code)
        print("NOTE: If language code is appropriate then you'll get the result!")
        translator = Translator(to_lang=language_code)  # This will automatically takes the language according to user input iso_language_code
        translated_user_input = translator.translate(user_text)
        print(translated_user_input)
        translatedText.append(translated_user_input)
    
    translatingFn()

    while True:
        userChoice = int(input("Enter 1 if you want to translate more text: "))
        if userChoice == 1:
            translatingFn()
        else:
            break

    length_normalText = len(normalText)
    with open(f'{new_text_file}.txt', mode = 'w') as user_txt_input:   # This will create a new txt file
        for i in range(length_normalText):
            user_txt_input.writelines(f"{normalText[i]}\n")

    length_translatedText = len(translatedText)
    with open(f'{new_text_file_save}.txt', mode = 'w') as user_txt_output:   # This will create a new txt file
        for i in range(length_translatedText):
            user_txt_output.writelines(f"{translatedText[i]}\n")

    for i in range(length_normalText):
        finalText1.append(f"You entered: {normalText[i]}.")

    for i in range(length_normalText):
        finalText2.append(f"Translated text in language code '{languageCode[i]}' : {translatedText[i]}.")

    pdf_data = int(input("If you want this data in pdf format, enter '1' else '0' \nEnter Your Choice: "))
    if pdf_data == 1:        
        pdf = FPDF()        # This is pre defined perameters of "fpdf" Python library
        pdf.add_page()
        pdf.set_font("Arial", size = 16)
        #pdf.multi_cell(200, 10, txt = f'{translated_data_file}',fill = False, border = 0)   # For adjusting lines
        sizeX, sizeY = 200, 10
        for i in range(length_normalText):
            pdf.multi_cell(sizeX, sizeY, txt = f'{finalText1[i]}\n{finalText2[i]}',fill = False, border = 0)
            sizeX = sizeX + 200
        pdf_file_name = str(input("Enter name for your PDF file: "))
        pdf.output(f"{pdf_file_name}.pdf")        
        input("Enter to continue.....")

        y = int(input(f"If you want encryption on your PDF file {pdf_file_name} then enter '1' else '0' for exiting \nEnter Your Choice: "))
        if y == 1:
            print("Enter any text/number/special_character for encryption. \nNote: Password will not appears because of security issues :) ")
            pdf_passwd = getpass.getpass(stream = sys.stderr)   # This will hide the user input password

            def encrypting_pdf(pdf_in, pdf_out, pdf_passwd):    # This gonna encrypt the pdf using user input password
                pdf_writing = PdfFileWriter()
                pdf_reading = PdfFileReader(pdf_in)

                for pages in range(pdf_reading.getNumPages()):
                    pdf_writing.addPage(pdf_reading.getPage(pages))

                pdf_writing.encrypt(user_pwd=pdf_passwd, owner_pwd=None, use_128bit=True)
                with open(pdf_out, mode = 'wb') as pdf_now_encrypt:
                    pdf_writing.write(pdf_now_encrypt)

            if __name__ == '__main__':
                encrypting_pdf(pdf_in = f'{pdf_file_name}.pdf', pdf_out = f'{pdf_file_name}.pdf', pdf_passwd = pdf_passwd)
            print(f"Your PDF {pdf_file_name} file successfully encrypted!!!")
        else:
            print(f"Thanks for your interest!!! \nYour PDF file {pdf_file_name} successfully saved")
            exit(0)
        
        with open(f'{new_text_file}.txt', mode = 'w') as erasing_txt_file1:
                erasing_txt_file1.write("The data is erased and saved into PDF file. \nYou can see the data in the PDF file only with the help of the password you given!!!")
        with open(f'{new_text_file_save}.txt', mode = 'w') as erasing_txt_file2:
                erasing_txt_file2.write("The data is erased and saved into PDF file. \nYou can see the data in the PDF file only with the help of the password you given!!!")

    else:
        print("Thanks for using this program!!!")
        exit(0)

else:
    exit(0)
