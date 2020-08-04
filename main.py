import pandas as pd
from PIL import Image,ImageFont,ImageDraw
import textwrap 

data=pd.read_excel("dataset.xls")
photo = Image.open('input/'+str(data['Photograph'][0])+'.jpg')

font = ImageFont.truetype("arial.ttf", 40)
wrapper = textwrap.TextWrapper(width=40)
template=Image.open('id.jpg')

for i in data.index:
    img = template.copy() 
    photo = Image.open('input/'+str(data['Photograph'][i])+'.jpg')
    photo = photo.resize((200,248))
    draw = ImageDraw.Draw(img)
    draw.text((185,258),data['Name'][i],fill="#000",font=font)
    draw.text((360,308),data['Guardian Name'][i],fill="#000",font=font)
    draw.text((300,358),str(data['Roll'][i]),fill="#000",font=font)
    draw.text((210,408),data['Course'][i],fill="#000",font=font)
    draw.text((310,458),data['Blood Group'][i],fill="#000",font=font)
    draw.text((370,508),str(data['Contact Number'][i]),fill="#000",font=font)
    draw.text((230,558),str(wrapper.fill(text=data['Address'][i])),fill="#000",font=font)
    img.paste(photo, (759, 41))
    img.convert('RGB').save('output/'+str(data['Roll'][i])+'.jpg') 
    #img.show()
    photo.close()
img.close()