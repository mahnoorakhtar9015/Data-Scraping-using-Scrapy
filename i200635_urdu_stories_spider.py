# Mahnoor Akhtar
# 20I-0635

import scrapy
import csv

# this is the main scrapy class that contains the function the function to parse the urdu text
class i200635_urdu_stories_spider(scrapy.Spider):
    # setting the name according to the instruction given in manual
    name='i200635_urdu_stories_spider'   
    # setting the urdu to the given url in assignment instructions
    start_urls=['https://www.urduzone.net/']

    # this parse function will fetch all the links that are under the h3 headings
    # To understand the structure of the assignment I first inspect the website and then I get to know that the all the urdu stories are accessed 
    # through another link and the I first parse all the links 
    def parse(self, response):
        # here I applied the css selector to get access to h3 heading.h3 heading contain the title of the story and under that 
        # heading there is <a> tag the contain the link to the full story
        links = response.css('h3 a::attr(href)').getall()

        # links contain the link to all stories and here I am going through all the the links through callback function and call the pasre_story 
        # function for all the links 
        for i in links:
            yield response.follow(i, callback=self.parse_story)

    # this function parse the text that is inside <p> tag and on all links 
    def parse_story(self, response):
       

        # here I applied the css selector to fetch data that is inside the tag to <p>
        story_text = response.css('p::text').getall()

        # Now I joined all the <p> tag text to make a complete story
        cleaned_story_text = ' '.join(story_text).strip()


        #  yield output the results on the terminal
        yield {
            
            'story_text': cleaned_story_text
        }

        # after wactching the results on the teminal I find out that there are some tags of \n so i removed it
        cleaned_story_text = cleaned_story_text.replace('\n', '')

        #  yield output the results on the terminal
        yield {
            
            'story_text': cleaned_story_text
        }

        # after getting the clear text here I called the function that will write the text in the csv file.
        self.add_to_csv(cleaned_story_text)

    # this function will write the stories in the csv files
    def add_to_csv(self,text):
        # here specifying the file name
        filename = 'i200635_urdu_stories.csv'

        # here opening the file and writing the text inside it.
        with open(filename, 'a', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([text])

     


