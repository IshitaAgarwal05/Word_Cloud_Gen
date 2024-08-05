from wordcloud import WordCloud, STOPWORDS

text = input("Enter your text: ")
stopwords = set(STOPWORDS)
font_path = "fonts/radiant-kingdom-font/RadiantKingdom-mL5eV.ttf"

wordcloud = WordCloud(width = 800, height = 800,
                      background_color="black",
                      contour_color="skyblue",
                      contour_width=3,
                      min_font_size=3,
                      max_words=100,
                      stopwords=stopwords,
                      random_state=21,
                      max_font_size = 100,
                      font_path=font_path).generate(text)

img = wordcloud.to_image()
img.show()

wordcloud.to_file('wordcloud_output.png')
