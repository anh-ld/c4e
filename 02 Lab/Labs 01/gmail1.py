from gmail import GMail, Message

gmail = GMail("duyanhle41@gmail.com","iuginvenice")
msg = Message('A Test Message',to='techkidsc4e16@gmail.com',text='Hello Techkids',html="<b>Hello</b>")
gmail.send(msg)
