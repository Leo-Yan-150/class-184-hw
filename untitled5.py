from tkinter import *
import requests
import json

root = Tk()
root.title("Stuff")
root.geometry("800x700")
root.config(bg="lavender")

newsupdate = Label(root, text="BBC News Update", font=("times new roman", 25, "bold"), bg="lavender")
newsupdate.place(relx=0.5,rely=0.03, anchor=CENTER)
news1 = Label(root,font=("times new roman",18),bg="lavender",wraplength=700,justify=LEFT, fg="indigo")
news1.place(relx=0.5,rely=0.1,anchor=CENTER)
desc1 = Label(root,font=("times new roman", 17),bg="lavender",wraplength=500,justify=LEFT)
desc1.place(relx=0.5,rely=0.15,anchor=CENTER)

news2 = Label(root,font=("times new roman",18),bg="lavender",wraplength=700,justify=LEFT, fg="indigo")
news2.place(relx=0.5,rely=0.25,anchor=CENTER)
desc2 = Label(root,font=("times new roman", 17),bg="lavender",wraplength=500,justify=LEFT)
desc2.place(relx=0.5,rely=0.3,anchor=CENTER)

news3 = Label(root,font=("times new roman",18),bg="lavender",wraplength=700,justify=LEFT, fg="indigo")
news3.place(relx=0.5,rely=0.4,anchor=CENTER)
desc3 = Label(root,font=("times new roman", 17),bg="lavender",wraplength=500,justify=LEFT)
desc3.place(relx=0.5,rely=0.45,anchor=CENTER)

news4 = Label(root,font=("times new roman",18),bg="lavender",wraplength=700,justify=LEFT, fg="indigo")
news4.place(relx=0.5,rely=0.55,anchor=CENTER)
desc4 = Label(root,font=("times new roman", 17),bg="lavender",wraplength=500,justify=LEFT)
desc4.place(relx=0.5,rely=0.6,anchor=CENTER)

news5 = Label(root,font=("times new roman",18),bg="lavender",wraplength=700,justify=LEFT, fg="indigo")
news5.place(relx=0.5,rely=0.7,anchor=CENTER)
desc5 = Label(root,font=("times new roman", 17),bg="lavender",wraplength=500,justify=LEFT)
desc5.place(relx=0.5,rely=0.75,anchor=CENTER)

api_request = requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4afe15aa457d40178798204036605738")
api_outupt_json = json.loads(api_request.content)

title1 = api_outupt_json["articles"][0]["title"]
news1['text'] = title1
thiny1 = api_outupt_json["articles"][0]["description"]
desc1['text'] = thiny1

title2 = api_outupt_json["articles"][1]["title"]
news2['text'] = title2
thiny2 = api_outupt_json["articles"][1]["description"]
desc2['text'] = thiny2

title3 = api_outupt_json["articles"][2]["title"]
news3['text'] = title3
thiny3 = api_outupt_json["articles"][2]["description"]
desc3['text'] = thiny3

title4 = api_outupt_json["articles"][3]["title"]
news4['text'] = title4
thiny4 = api_outupt_json["articles"][3]["description"]
desc4['text'] = thiny4

title5 = api_outupt_json["articles"][4]["title"]
news5['text'] = title5
thiny5 = api_outupt_json["articles"][4]["description"]
desc5['text'] = thiny5

#open_bbc_page didn't work so I did it like this :(

root.mainloop()