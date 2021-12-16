import dash.dependencies as dd
from dash import html, dcc
from io import BytesIO
import dash
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from wordcloud import WordCloud
import wordcloud


class Chart_WordCloud():
    
    def __init__(self):
        self.df = pd.read_excel("./datasets/Passwords.xlsx") # Excel einlesen
        self.word_cloud = None
        self.create_wordcloud()

    # Wordlcloud erstellen
    def create_wordcloud(self):
        self.df.isna().sum()
        text = {}

        for index, row in self.df.iterrows():
            text[str(row["Password"])] = row["size"]



        x, y = np.ogrid[:250, :250]

        mask = (x - 125) ** 2 + (y - 125) ** 2 > 125 ** 2
        mask = 255 * mask.astype(int)





        self.word_cloud = WordCloud(collocations = False, background_color="white",width=1920, height=1080, mask=mask).generate_from_frequencies(text)
        def black_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
            return("hsl(0,100%, 1%)")
        self.word_cloud.recolor(color_func = black_color_func)

        # Creating word_cloud with text as argument in .generate() method
        #word_cloud = WordCloud(collocations = False, background_color = 'white', width=1200, height=1000).generate(text)
        # Display the generated Word Cloud
        plt.imshow(self.word_cloud, interpolation='bilinear')
        plt.axis("off")

        return self.word_cloud.to_image()
        



"""dfm = pd.DataFrame({'word': ['apple', 'pear', 'orange'], 'freq': [1,3,9]})

app.layout = html.Div([
    html.Img(id="image_wc"),
])

def plot_wordcloud(data):
    d = {a: x for a, x in data.values}
    wc = WordCloud(background_color='black', width=480, height=360)
    wc.fit_words(d)
    return wc.to_image()

@app.callback(dd.Output('image_wc', 'src'), [dd.Input('image_wc', 'id')])
def make_image(b):
    img = BytesIO()
    plot_wordcloud(data=dfm).save(img, format='PNG')
    return 'data:image/png;base64,{}'.format(base64.b64encode(img.getvalue()).decode())

if __name__ == '__main__':
    app.run_server(debug=True)"""