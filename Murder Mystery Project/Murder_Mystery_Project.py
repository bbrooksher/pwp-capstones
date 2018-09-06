import re

murder_note = "You may call me heartless, a killer, a monster, a murderer, but I'm still NOTHING compared to the villian that Jay was. This whole contest was a sham, an elaborate plot to shame the contestants and feed Jay's massive, massive ego. SURE you think you know him! You've seen him smiling for the cameras, laughing, joking, telling stories, waving his money around like a prop but off camera he was a sinister beast, a cruel cruel taskmaster, he treated all of us like slaves, like cattle, like animals! Do you remember Lindsay, she was the first to go, he called her such horrible things that she cried all night, keeping up all up, crying, crying, and more crying, he broke her with his words. I miss my former cast members, all of them very much. And we had to live with him, live in his home, live in his power, deal with his crazy demands. AND FOR WHAT! DID YOU KNOW THAT THE PRIZE ISN'T REAL? He never intended to marry one of us! The carrot on the stick was gone, all that was left was stick, he told us last night that we were all a terrible terrible disappointment and none of us would ever amount to anything, and that regardless of who won the contest he would never speak to any of us again! It's definitely the things like this you can feel in your gut how wrong he is! Well I showed him, he got what he deserved all right, I showed him, I showed him the person I am! I wasn't going to be pushed around any longer, and I wasn't going to let him go on pretending that he was some saint when all he was was a sick sick twisted man who deserved every bit of what he got. The fans need to know, Jay Stacksby is a vile amalgamation of all things evil and bad and the world is a better place without him."
myrtle_beech_intro = "Salutations. My name? Myrtle. Myrtle Beech. I am a woman of simple tastes. I enjoy reading, thinking, and doing my taxes. I entered this competition because I want a serious relationship. I want a commitment. The last man I dated was too whimsical. He wanted to go on dates that had no plan. No end goal. Sometimes we would just end up wandering the streets after dinner. He called it a \"walk\". A \"walk\" with no destination. Can you imagine? I like every action I take to have a measurable effect. When I see a movie, I like to walk away with insights that I did not have before. When I take a bike ride, there better be a worthy destination at the end of the bike path. Jay seems frivolous at times. This worries me. However, it is my staunch belief that one does not make and keep money without having a modicum of discipline. As such, I am hopeful. I will now list three things I cannot live without. Water. Emery boards. Dogs. Thank you for the opportunity to introduce myself. I look forward to the competition."
lily_trebuchet_intro = "Hi, I'm Lily Trebuchet from East Egg, Long Island. I love cats, hiking, and curling up under a warm blanket with a book. So they gave this little questionnaire to use for our bios so lets get started. What are some of my least favorite household chores? Dishes, oh yes it's definitely the dishes, I just hate doing them, don't you? Who is your favorite actor and why? Hmm, that's a hard one, but I think recently I'll have to go with Michael B. Jordan, every bit of that man is handsome, HANDSOME! Do you remember seeing him shirtless? I can't believe what he does for the cameras! Okay okay next question, what is your perfect date? Well it starts with a nice dinner at a delicious but small restaurant, you know like one of those places where the owner is in the back and comes out to talk to you and ask you how your meal was. My favorite form of art? Another hard one, but I think I'll have to go with music, music you can feel in your whole body and it is electrifying and best of all, you can dance to it! Okay final question, let's see, What are three things you cannot live without? Well first off, my beautiful, beautiful cat Jerry, he is my heart and spirit animal. Second is pasta, definitely pasta, and the third I think is my family, I love all of them very much and they support me in everything I do. I know Jay Stacksby is a handsome man and all of us want to be the first to walk down the aisle with him, but I think he might truly be the one for me. Okay that's it for the bio, I hope you have fun watching the show!"
gregg_t_fishy_intro = "A most good day to you all, I am Gregg T Fishy, of the Fishy Enterprise fortune. I am 37 years young, an adventurous spirit and I've never lost my sense of childlike wonder. I do love to be in the backyard gardening and I have the most extraordinary time when I'm fishing. Fishing for what, you might find yourself asking? Why, I happen to always be fishing for compliments of course! I have a stunning pair of radiant blue eyes that will pierce the soul of anyone who dare gaze upon my countenance. I quite enjoy going on long jaunts through garden paths and short walks through greenhouses. I hope that Jay will be as absolutely interesting as he appears on the television, I find that he has some of the most curious tastes in style and humor. When I'm out and about I quite enjoy hearing tales that instill in my heart of hearts the fascination that beguiles my every day life, every fiber of my being scintillates and vascillates with extreme pleasure during one of these charming anecdotes and significantly pleases my beautiful personage. I cannot wait to enjoy being on the television program A Jay To Remember, it certainly seems like a grand time to explore life and love."

#Write a function get_average_sentence_length that takes some text as an argument.
#This function should return the average length of a sentence in the text.
def get_average_sentence_length(text):
    sentences = re.split(r'[.?!]', text)
    word_count = 0
    for sentence in sentences:
        word_count += len(sentence.strip().split())
    return word_count/len(sentences)

#Create a function called prepare_text that takes a single parameter text
def prepare_text(text):
    #makes the text entirely lowercase, removes all the punctuation and returns a list of the words in the text in order.
    return text.lower().replace(".", " ").replace(",", " ").replace("\"", " ").replace("?", " ").replace("!", " ").split()
    
#Create a function called build_frequency_table. It takes in a list
# called corpus and creates a dictionary called frequency_table.
def build_frequency_table(corpus):
    frequency_table = {}
    #For every element in corpus the value frequency_table[element] should
    # be equal to the number of times that element appears in corpus.
    for element in corpus:
        if element in frequency_table:
            frequency_table[element] += 1
        else:
            frequency_table[element] = 1
    return frequency_table

#Create a function called ngram_creator that takes a parameter
# text_list, a treated in-order list of the words in a text sample. 
def ngram_creator(text_list):
    #ngram_creator should return a list of all adjacent pairs
    #of words, styled as strings with a space in the center.
    n_gram = []
    for i in range(0, len(text_list) - 1):
        s = str.format("{} {}", text_list[i], text_list[i + 1])
        n_gram.append(s)
    return n_gram

#Let's define a class called TextSample
class TextSample:
    #with a constructor. The constructor should take two arguments: text and author.
    def __init__(self, text, author):
        #text should be saved as self.raw_text
        self.raw_text = text
        #You should save the author of the text as self.author.
        self.author = author
        #Call get_average_sentence_length with the raw text and save it to self.average_sentence_length.
        self.average_sentence_length = get_average_sentence_length(self.raw_text)
        #Update the constructor for TextSample to save the prepared text as self.prepared_text.
        self.prepared_text = prepare_text(self.raw_text)
        #Use build_frequency_table with the prepared text to create a frequency table
        # that counts how frequently all the words in each text sample appears. Call
        # these functions in the constructor for TextSample and assign the
        # word frequency table to a value called self.word_count_frequency.
        self.word_count_frequency = build_frequency_table(self.prepared_text)
        #Use ngram_creator along with the prepared text to create a list of all
        # the two-word ngrams in each TextSample. Use build_frequency_table to
        # tabulate the frequency of each ngram. In the constructor for TextSample
        #save this frequency table as self.ngram_frequency.
        self.ngram_frequency = ngram_creator(self.prepared_text)

    #Additionally, define a string representation for the model.
    #If you print a TextSample it should render:
    #The author's name
    #The average sentence length
    def __repr__(self):
        return "{a}, {l}".format(a=self.author, l=self.average_sentence_length)

#Now create a TextSample object for each of the samples of text that we have.
murderer_sample = TextSample(murder_note, "Anon")
lily_sample = TextSample(lily_trebuchet_intro, "Lily Trebuchet")
myrtle_sample = TextSample(myrtle_beech_intro, "Myrtle Beech")
gregg_sample = TextSample(gregg_t_fishy_intro, "Gregg T Fishy")

#Print out each one after instantiating them.
print(murderer_sample)
print(lily_sample)
print(myrtle_sample)
print(gregg_sample)

#Write a function called frequency_comparison that takes
# two parameters, table1 and table2.     
def frequency_comparison(table1, table2):
    #It should define two local variables,
    #appearances and mutual_appearances.
    appearances = 0
    mutual_appearances = 0
    #Iterate through table1's keys
    for key in table1.keys():
        #and check if table2 has the same key defined.
        if key in table2.keys():
            #If it is, compare the two values for the key
            if table1[key] < table2[key]:
                #the smaller value should get added to mutual_appearances
                mutual_appearances += table1[key]
                # and the larger should get added to appearances
                appearances += table2[key]
        #If the key doesn't exist in table2
        else:
            #the value for the key in table1 should be added to appearances.
            appearances += table1[key]
    #Remember afterwards to iterate through all of table2's keys
    for key in table2.keys():
        #keys that aren't in table1 and add those to appearances as well.
        if key not in table1.keys():
            appearances += table2[key]
    #Return a frequency comparison score equal to the
    # mutual appearances divided by the total appearances.
    return mutual_appearances / appearances

#Write a function called percent_difference that returns the
# percent difference as calculated from the following formula:
#| value1−value2 |/ value1+value2/2
def percent_difference(value1, value2):
    return abs(value1 - value2) / ((value1 + value2) / 2)

#Define a function find_text_similarity that takes two TextSample arguments and
# returns a float between 0 and 1 where 0 means completely different
# and 1 means the same exact sample.
def find_text_similarity(text_sample_1, text_sample_2):
    #Calculate the percent difference of their average sentence length using
    # percent_difference. Save that into a variable called sentence_length_difference.
    sentence_length_difference = percent_difference(text_sample_1.average_sentence_length, text_sample_2.average_sentence_length)
    #Since we want to find how similar the two passages are calculate the inverse
    # of sentence_length_difference by using the formula abs(1 - sentence_length_difference).
    # Save that into a variable called sentence_length_similarity.
    sentence_length_similarity = abs(1 - sentence_length_difference)
    #Calculate the difference between their word usage using frequency_comparison
    # on both TextSample's word_count_frequency attributes. Save that into a
    # variable called word_count_similarity.
    word_count_similarity = frequency_comparison(text_sample_1.word_count_frequency, text_sample_2.word_count_frequency)
    #Calculate the difference between their two-word ngram using frequency_table
    # on both TextSample's ngram_frequency attributes. Save that into a
    # variable called ngram_similarity.
    # *** TO ME THIS INSTRUCTION MAKES NO SENSE AT ALL ***
    table1_frequency = build_frequency_table(text_sample_1.ngram_frequency)
    table2_frequency = build_frequency_table(text_sample_2.ngram_frequency)
    ngram_similarity = frequency_comparison(table1_frequency, table2_frequency)
    #Add all three similarities together and divide by 3.
    return (sentence_length_similarity + word_count_similarity + ngram_similarity) / 3

print(str.format("{}\'s similarity score is: {}", lily_sample.author, find_text_similarity(lily_sample, murderer_sample)))
print(str.format("{}\'s similarity score is: {}", myrtle_sample.author, find_text_similarity(myrtle_sample, murderer_sample)))
print(str.format("{}\'s similarity score is: {}", gregg_sample.author, find_text_similarity(gregg_sample, murderer_sample)))





























    
