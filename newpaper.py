from tkinter import *
from PIL import ImageTk,Image
import PIL.Image

root = Tk()
root.title("NewsForEve-Yash NewsFeed")
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root.resizable(width = False,height = False)

head = Label(root,text="Yash NewsFeed",font= "arial 50 bold",padx =600)
head.pack()

f0 = Frame(root,width=500)
f0.pack(side ="left",fill=Y,padx = 20)
f0.propagate(0)

col1head = Label(f0,text = "Amazon hikes Prime membership fees in US as wages, costs rise",font = "comicsansms 20 bold",wraplength=500,justify = "left")
col1head.grid(row = 0,column = 0)

col1content = Label(f0,text = """\nFebruary 04, 2022 12:48 pm.\nThe change is effective Feb 18 for new members and reflects greater benefits such as savings on prescription drugs and faster delivery, Amazon said.Amazon.com Inc on Thursday said it was raising the price of its annual US Prime subscriptions by 17%, as it looks to offset higher costs for shipping and wages that it expects to persist this year.

Shares rose as much as 17% in extended trade, as Amazon also beat profit expectations for the holiday season.

If shares increase on Friday by that much, it would be the stock’s biggest percentage gain since October 2009 and grow founder Jeff Bezos’ wealth by about $20 billion.

For the holiday quarter, Amazon earned $14.3 billion, double its net income from a year earlier.

That included a pre-tax gain of $11.8 billion from its stake in electric car maker Rivian Automotive.

On the heels of a windfall from greater at-home shopping in the pandemic, Amazon has poured money into its operations to manage disruptions, most recently the Omicron variant of Covid-19.

It has marketed signing bonuses to attract hundreds of thousands of workers in a tight labor market, and it has paid more for shipping because it could not get products into the right warehouses.""",wraplength=500,justify="left",font = 'arial 10 ')
# col1content.pack(side = 'left',anchor= "nw",pady = 40)
col1content.grid(row = 1,column= 0)
col1head2 = Label(f0,text = "Google One VPN comes to iOS: Here's all you need to know",font = "arial 20 bold",wraplength= 500,justify = LEFT,)
col1head2.grid(row = 3,column = 0)
col1content2 = Label(f0,text ="""Google One has begun rolling out its own VPN (Virtual Private Network) for iOS users. The service has been available for Android users for over a year, but now, iPhone users can make use of it too. Similar to how the service works on Android, users on iOS too will need a Google One Premium membership plan to be able to use Google One VPN.

For the uninitiated, Google One VPN is Google’s own VPN service that the tech giant bundles with Premium Google One subscriptions. Google’s VPN is also certified by the Internet of Secure Things Alliance (IoXt). The service, however, is only available in select regions. This for now includes 18 countries, including the US, Canada and UK.
India is not in the list and Google VPN is not supported here at the moment, even if you have a premium plan. However, Google does plan on brining the service to more """,wraplength=500,justify = LEFT,font = "arial 10 ")
col1content2.grid(row = 4,column = 0)

f1 = Frame(root,width = 500)
f1.pack(side = "left",fill = Y,padx=20)
f1.propagate(0)

col2content = Label(f1,text = """regions so we may see it eventually launch in India.

Note that to be able to use Google One VPN, you need to have a Google One Premium membership of 2TB or higher cloud storage. Your VPN as well as storage can then be used by up to five members.""",wraplength=500,font = "arial 10",justify = LEFT)
col2content.grid(row = 0,column = 0)
photo = Image.open("GoogleImage.jpg")
pic = ImageTk.PhotoImage(photo)
picLab = Label(f1,image= pic,width = 500,height=500)
picLab.grid(row = 1,column =0,padx = 0)

col2head1 = Label(f1,text = """In heated meeting, India seeks tougher action from US tech giants on fake news""",font = "arial 20 bold",wraplength = 500,justify = LEFT)
col2head1.grid(row =2,column = 0)

col2content2 = Label(f1,text = """The sources, who were familiar with the proceedings at the virtual meeting on Monday, described the conversation as tense and heated, signalling a new low in ties between American tech giants and Prime Minister Narendra Modi's administration.""",font = "arial 10 ",wraplength= 500,justify = LEFT)
col2content2.grid(row =3, column = 0)

col2content3 = Label(f1,text ="""Indian officials have held heated discussions with Google, Twitter and Facebook for not proactively removing what they described as fake news on their platforms, sources told""",wraplength = 500,justify=LEFT)
col2content3.grid(row = 4,column = 0)

f2 = Frame(root,width = 500)
f2.pack(side = "left",fill = Y,padx = 20)
f2.propagate(0)

col3content1 = Label(f2,text =""" Reuters, the government’s latest altercation with Big Tech.

The officials, from the Ministry of Information and Broadcasting (I&B), strongly criticised the companies and said their inaction on fake news was forcing the Indian government to order content takedowns, which in turn drew international criticism that authorities were suppressing free expression, two sources said.

The sources, who were familiar with the proceedings at the virtual meeting on Monday, described the conversation as tense and heated, signalling a new low in ties between American tech giants and Prime Minister Narendra Modi’s administration.

The officials did not issue any ultimatum to the companies at the meeting, they informed.

The government has been tightening tech sector regulations, but wants companies to do more on content moderation.

The meeting was a follow-up to the I&B ministry’s use of “emergency powers” in December and January to order the blocking of 55 channels on Google’s YouTube platform, and some Twitter and Facebook accounts.

In its transparency reports, Twitter has said the Indian government makes among the highest number of requests to remove content from its platform.

Technology website Comparitech in October said that India made 97,631 content removal requests in 2020, the second-highest in the world after Russia, mostly to Facebook and Google.""",font = "arial 10",wraplength=500,justify = LEFT)
col3content1.grid(row = 1,column = 0)

photo1 = Image.open("google-reuters-2.jpg")
pic1 = ImageTk.PhotoImage(photo1)
picLab1 = Label(f2,image=pic1,wraplength = 500,width = 500,height = 350)
picLab1.grid(row = 2,column =0)

root.mainloop()
 