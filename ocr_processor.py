import easyocr

def image_reader(path):
    reader = easyocr.Reader(["en"])
    result = reader.readtext(path)
    text =" "
    for box, detected_text, confidence in result:
        if confidence > 0.5:
            text += detected_text + " "
        
    return text

 