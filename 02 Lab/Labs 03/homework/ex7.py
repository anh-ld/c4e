def remove_dollar_sign(s):
    s = s.replace("$","")
    return s

print(remove_dollar_sign("This is $$$100,000$$$"))
