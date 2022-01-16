import json #in order to be able to interpret it
import requests #to be able to pull on web service
class TENOR_CLIENT:
    def __init__(self, token): #class constructor
        self.token = token 
    def get_random_bloons(self):
        #variable for the api request
        apikey = self.token  
        search_term = "bloonstd6"
        media_filter = "gif, tinygif, nanogif"
        lmt = 1
        #tenor has a format for grabing gif using their api
        r = requests.get(
            "https://g.tenor.com/v1/random?q=%s&key=%s&limit=%s&media_filter=%s" % (search_term, apikey, lmt, media_filter))
        #this is required since a code other than 200 means that it has failed to reach the tenor server for any reason
        if r.status_code == 200:
            gif = json.loads(r.content)
            gif_final = (gif['results'][0]['media'][0]['gif']['url']) #the link of the gif are stored in a dictionary and to access it, this code is required
        #to inform the user if there is an issue with the service
        else:
            gif = None
            gif_final = "an error has occured"
        return gif_final
    #with how I design the code this has become quite modular, so later on I can add even more randomizer
    def get_random_gog(self):
        apikey = self.token  
        search_term = "gog"
        media_filter = "gif, tinygif, nanogif"
        lmt = 1

        r = requests.get(
            "https://g.tenor.com/v1/random?q=%s&key=%s&limit=%s&media_filter=%s" % (search_term, apikey, lmt, media_filter))

        if r.status_code == 200:
            gif = json.loads(r.content)
            gif_final = (gif['results'][0]['media'][0]['gif']['url'])
        else:
            gif = None
            gif_final = "an error has occured"
        return gif_final



