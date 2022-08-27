# import pytesseract
# import cv2
# #pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Akash.Chauhan1\AppData\Local\Tesseract-OCR\tesseract.exe'
# # use this command to install open cv2
# # pip install opencv-python

# # use this command to install PIL
# # pip install Pillow

# import cv2
# from PIL import Image
# import cv2
# line_items_coordinates = []
# def mark_region(image_path):
    
#     image = cv2.imread(image_path)

#     # define threshold of regions to ignore
#     THRESHOLD_REGION_IGNORE = 40

#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     blur = cv2.GaussianBlur(gray, (9,9), 0)
#     thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,30)

#     # Dilate to combine adjacent text contours
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9,9))
#     dilate = cv2.dilate(thresh, kernel, iterations=4)

#     # Find contours, highlight text areas, and extract ROIs
#     cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     cnts = cnts[0] if len(cnts) == 2 else cnts[1]

#     line_items_coordinates = []
#     for c in cnts:
#         area = cv2.contourArea(c)
#         x, y, w, h = cv2.boundingRect(c)
        
#         if w < THRESHOLD_REGION_IGNORE or h < THRESHOLD_REGION_IGNORE:
#             continue
        
#         image = cv2.rectangle(image, (x,y), (x+w, y+h), color=(255,0,255), thickness=3)
#         line_items_coordinates.append([(x,y), (x+w, y+h)])

#     return image, line_items_coordinates

# import matplotlib.pyplot as plt

# img,temp=mark_region('Page_1.jpg')


# image = cv2.imread('Page_1.jpg')

# # get co-ordinates to crop the image
# # c = line_items_coordinates[1]
# c = temp[1]

# # cropping image img = image[y0:y1, x0:x1]
# img = image[c[0][1]:c[1][1], c[0][0]:c[1][0]]    

# plt.figure(figsize=(10,10))
# plt.imshow(img)

# # convert the image to black and white for better OCR
# ret,thresh1 = cv2.threshold(img,120,255,cv2.THRESH_BINARY)

# # pytesseract image to string to get results
# text = str(pytesseract.image_to_string(thresh1, config='--psm 6'))
# print(text)



##################################################################

from PIL import Image
import pytesseract

def process_image(iamge_name, lang_code):
	return pytesseract.image_to_string(Image.open(iamge_name), lang=lang_code)

def print_data(data):
	print(data)

def output_file(filename, data):
	file = open(filename, "w+")
	file.write(data)
	file.close()

def main():
	data_eng = process_image("t1.png", "eng")
	#data_ben = process_image("test_ben.png", "ben")
	print_data(data_eng)
	#print_data(data_ben)
	output_file("eng.txt", data_eng)
	#output_file("ben.txt", data_ben)

if  __name__ == '__main__':
	main()



############################################

# =============================================================================
# This function will extract the information from the text generated from the pdf. 
# I'm using a corrosponding regex which is save with the same name of the pdf file. 
# In future we can create template mapping for the same structured pdf files.
# =============================================================================
# import re
# from PIL import Image
# import pytesseract
# import json
# import glob
# #Recognizing text from the images using OCR 
# def pdf2txt(PDF_file):
#     #pytesseract.pytesseract.tesseract_cmd = r"full path to the exe file"
#     #pytesseract.pytesseract.tesseract_cmd = tesseract_loc
#     PDF_file=PDF_file
#     pdfs = glob.glob(PDF_file)
#     text=''
#     for pdf_path in pdfs:
#         pages = pytesseract.convert_from_path(pdf_path, 500)
    
#         for pageNum,imgBlob in enumerate(pages):
#             filename = pdf_path[:-4]+'_page'+str(pageNum)+'.jpg'
#             # Save the image of the page in system 
#             imgBlob.save(filename, 'JPEG')
#             text = text+pytesseract.image_to_string(filename,lang='eng',config='--psm 6')
#     return(text)






# def extract_info(PDF_file,text):
#     try:
#         with open (PDF_file.split('/')[-1:][0][:-4]+".txt", "r") as myfile:
#             data=myfile.readlines()
#     except FileNotFoundError:
#         print("Wrong file or template missing")
#         return
        
#     values_dict={}
    
#     if (re.findall('REFORAWING|REFDRAWING',text)):
#         print('Document Type: Engineering Drawing')
#         try:
#             values_dict['Job Number']=re.findall(data[0][:-1], text)[0]
#         except:
#             values_dict['Job  Number']=re.findall(data[0][:-1], text)
#         try:
#             values_dict['Pipe Class']=re.findall(data[1][:-1], text)[0]
#         except:
#             values_dict['Pipe Class']=re.findall(data[1][:-1], text)
            
#     elif ((re.findall('Invoice',text))):
#         print('Document Type: Invoice')
#         try:
#             values_dict['Invoice Number']=re.findall(data[0][:-1], text)[0]
#         except:
#             values_dict['Invoice Number']=re.findall(data[0][:-1], text)
#         try:
#             values_dict['Invoice Date']=re.findall(data[1][:-1], text)[0]
#         except:
#             values_dict['Invoice Date']=re.findall(data[1][:-1], text)
#         try:    
#             values_dict['Invoice Amount']=re.findall(data[2], text)[0]
#         except:
#             values_dict['Invoice Amount']=re.findall(data[2], text)
#     else:
#         print('Unknown')

# #Writing json file       
#     print(values_dict)
#     with open (PDF_file.split('/')[-1:][0][:-4]+".json", "w") as myfile:
#         myfile.write(json.dumps(values_dict))
        
# def main(args=None):
#     try:
#         pdf2txt('invoice_sample.pdf')
#         # print(args[0])
#         # text=pdf2txt(args[0])
#         # extract_info(args[0],text)
#     except:
#         print('Usage: pdf_extract.py <pdf file name>')


# main()