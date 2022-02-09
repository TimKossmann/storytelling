import datetime
from re import I
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE
from data_breaches_bar_chart_bubble_plot_actual_year import Charts_DataBreaches
from data_breaches_attack_vectors_treemap import Chart_AttackVectors
from phishing_graphs import Phishing_Graphs
from passwords_wordcloud import Chart_WordCloud



class Powerpoint():
    def __init__(self):
        self.pp = Presentation("Powerpoint_Template.pptx")
        self.dbr = Charts_DataBreaches()
        self.pg = Phishing_Graphs()
        pass

    def get_picture_img_layout(self):
        return self.pp.slide_layouts[0]
    
    def create_images(self):
        date = datetime.date.today()
        actual_year = date.strftime("%Y")

        self.dbr.update_bubblechart_by_year(int(actual_year) -1).write_image("fig_bubblechart_pp.png")
        self.dbr.create_lineplot(int(actual_year) -1).write_image("fig_lineplot_pp.png", width=600, height=300,scale=1)
        self.dbr.create_table().write_image('fig_table_pp.png')
        
        
        self.pg.get_link_donut(True, False).write_image("phishing_link_pp.png")
        self.pg.get_input_donut(True, False).write_image("phishing_input_pp.png")
        self.pg.get_attach_donut(True, False).write_image("phishing_attach_pp.png")


    def create_pp(self):
        #first_slide = pp.slides.add_slide(layout)
        #pic = first_slide.shapes.add_picture("fail_bar_mark.png", Inches(0), Inches(1.5), height=Inches(5.5))

        bubble_side = self.pp.slides.add_slide(self.get_picture_img_layout())
        title = bubble_side.placeholders[0]
        title.text = "Warum brauch ich das?"

        placeholder = bubble_side.placeholders[1]
        print(placeholder.placeholder_format.type)
        placeholder.insert_picture("fig_lineplot_pp.png")

        sub_text = bubble_side.placeholders[2]
        tf = sub_text.text_frame

        p = tf.add_paragraph()
        p.text = 'Kosten die durch Datenlecks entstehen steigen Jahr für Jahr an'
        p.level = 0

        p = tf.add_paragraph()
        p.text = 'Oft können solche Attacken verhindert werden'
        p.level = 0


        phishing_slide = self.pp.slides.add_slide(self.pp.slide_layouts[1])
        added_img = 0
        added_txt = 0

        img_names = ["phishing_link_pp.png", "phishing_input_pp.png", "phishing_attach_pp.png"]
        img_txt = [self.pg.get_text_for_dounut("link"), self.pg.get_text_for_dounut("input"), self.pg.get_text_for_dounut("attach")]
        for plch in phishing_slide.placeholders:
            print(plch.placeholder_format.type)
            plc_type = str(plch.placeholder_format.type)
            if "PICTURE" in plc_type:
                #placeholder_loop = phishing_slide.placeholders[index+2]
                plch.insert_picture(img_names[added_img])
                added_img += 1
            if "OBJECT" in plc_type:
                tf = plch.text_frame
                p = tf.add_paragraph()
                p.text = img_txt[added_txt].replace("<br>", "")
                added_txt += 1

        
        """
        placeholder = first_slide.placeholders[1]
        print(placeholder.placeholder_format.type)
        placeholder.insert_picture("fail_bar_mark.png")

        placeholder = first_slide.placeholders[0]
        placeholder.text = 'Fail Bar'

        placeholder = first_slide.placeholders[2]
        placeholder.text = 'Fail Bar \nZweiter Text'
        #print(len(first_slide.placeholders))"""

        self.pp.save("Powerpoint.pptx")

if __name__ == "__main__":
    pp = Powerpoint()
    pp.create_images()
    pp.create_pp()
