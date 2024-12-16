import random
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

font_path = "Pretendard-Medium.ttf"
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 40
LINE_HEIGHT = 15

title = input("제목을 입력해 주세요: ")
text = input("본문을 입력해 주세요: ")
answer = input("해설을 입력해 주세요: ")
textList = []
answerList = []
underscore = "_________________________________________________________________________________"

for i in text.rstrip('.').split('.') : 
    i = i.strip()+'.'
    textList.append(i)

for a in answer.rstrip('.').split('.') : 
    a = a.strip()+'.'
    answerList.append(a)

def create_pdf():
    pdf_file = "output.pdf"
    c = canvas.Canvas(pdf_file, pagesize=A4)
    pdfmetrics.registerFont(TTFont("Pretendard", font_path))
    c.setFont("Pretendard", 10.5)
    text_x, text_y = MARGIN, PAGE_HEIGHT - MARGIN
    c.drawString(text_x, text_y, title)
    text_y -= 25
    for item1, item2 in zip(textList, answerList) : 
        if text_y <= 45 : 
            c.showPage()
            c.setFont("Pretendard", 10.5)  # 새 페이지에서도 폰트 설정
            text_y = PAGE_HEIGHT - MARGIN  # 새 페이지의 y 좌표 초기화
        item1 = item1.lower().rstrip('.').split()
        random.shuffle(item1)
        shuffled_item1 = ' / '.join(item1)
        c.drawString(text_x, text_y, shuffled_item1)
        text_y -= 15
        c.drawString(text_x, text_y, item2)
        text_y -= 30
        c.drawString(text_x, text_y, underscore)
        text_y -= 25
    c.save()
create_pdf()