import paralleldots
class API:

    def __init__(self):

         paralleldots.set_api_key("uUj1TRaaFwAThXbthkvnZq1e49TMeFhyTsgbOYsK3Pk")

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response

    def ner_analysis(self,text):
        response=paralleldots.ner(text)
        return response

    def emotion_preditction_analysis(self,text):
        response=paralleldots.emotion(text)
        return response





