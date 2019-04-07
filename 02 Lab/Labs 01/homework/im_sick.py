from gmail import GMail, Message
from random import choice
from datetime import datetime

reasons = ['mệt','ngủ quên','đau răng','đau bụng','ngã xe']
gmail = GMail("duyanhle41@gmail.com","minimalism")

html_content = """
<p style="text-align: center;"><strong>Đơn xin nghỉ học</strong></p>
<p>Em ch&agrave;o thầy,</p>
<p>Em t&ecirc;n l&agrave; L&ecirc; Duy Anh, học vi&ecirc;n lớp C4E16.</p>
<p>H&ocirc;m nay em {{sickness}}, em xin thầy cho em nghỉ 1 buổi.</p>
<p>Em cảm ơn thầy.</p>
"""

html_content = html_content.replace("{{sickness}}",choice(reasons))
msg = Message('Don xin nghi hoc',to='techkidsc4e16@gmail.com',html=html_content)

while True:
    now = datetime.now()
    if now.hour == 7:
        gmail.send(msg)
        break
