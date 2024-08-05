# Import the libraries
from wordcloud import WordCloud, STOPWORDS

# Take text input to be put into the cloud image
text = input("Enter your text: ")
stopwords = set(STOPWORDS)

# Set font for the text in the image
font_path = "fonts/radiant-kingdom-font/RadiantKingdom-mL5eV.ttf"

# Set wordcloud attributes and parameters
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

# Convert, show, and save the image as a png file in your PC 
img = wordcloud.to_image()
img.show()

wordcloud.to_file('wordcloud_output.png')
