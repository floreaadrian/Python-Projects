from PIL import Image

im = Image.open('unu.jpg') # Can be many different formats.
pix = im.load()
width = im.size[0]
height = im.size[1]
contor = 0
myFile = open("test.html","a")
cssFile = open("test.css","a")
myFile.write("<html>\n<head>\n<link rel=\"stylesheet\" type=\"text/css\" href=\"test.css\">\n</head><body>\n")
cssFile.write("#sizet{\nwidth: 1px;\n height: 1px;\n}\n")
for i in range(0,width):
    myFile.write("<div style=\"display: inline-block;\">")
    for j in range(0, height):
        color = pix[i,j]
        contor = contor + 1
        textToWrite = "<div id=\"sizet\" class=i"+ str(contor) +"></div>\n"
        textToWriteCss = ".i" + str(contor)
        textToWriteCss = textToWriteCss + "{\nbackground-color: rgb("
        textToWriteCss = textToWriteCss +str(color[0])+","+str(color[1])+","+str(color[2])+");}\n"
        myFile.write(textToWrite)
        cssFile.write(textToWriteCss)
    myFile.write("</div>")
myFile.write("</body>\n</html>")
myFile.close()
