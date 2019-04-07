from gmail import GMail, Message
from random import choice

reasons = ['mệt','ngủ quên','đau răng','đau bụng','ngã xe']

gmail = GMail("duyanhle41@gmail.com","iuginvenice")
html_content = """
<p style="text-align: center;"><strong>Đơn xin nghỉ học</strong></p>
<p>Em ch&agrave;o thầy</p>
<p>T&ecirc;n em l&agrave; L&ecirc; Duy Anh</p>
<p>H&ocirc;m nay em {{sickness}} n&ecirc;n em xin thầy cho em xin nghỉ 1 buổi&nbsp;<img src="http://htmleditor.tools/tinymce465/plugins/emoticons/img/smiley-cool.gif" alt="cool" /></p>
<p>Duy Anh</p>
"""
html_content = html_content.replace("{{sickness}}",choice(reasons))
msg = Message('Don xin nghi hoc',to='techkidsc4e16@gmail.com',html=html_content)
gmail.send(msg)
