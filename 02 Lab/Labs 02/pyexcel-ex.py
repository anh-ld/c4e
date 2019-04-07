import pyexcel

a_list_of_dictionary = [
    {
        "title" : "T1",
        "link" : "http://google.com.vn"
    },
    {
        "title" : "T2",
        "link" : "http://google.com.vn"
    },
    {
        "title" : "T3",
        "link" : "http://google.com.vn"
    },
]
pyexcel.save_as(records=a_list_of_dictionary, dest_file_name="1.xls")
