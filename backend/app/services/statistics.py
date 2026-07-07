class DatasetStatistics:

    def __init__(self,papers):

        self.papers=papers

    def summary(self):

        docs=len(self.papers)

        avg=sum(

            len(

                p["combined_text"].split()

            )

            for p in self.papers

        )/docs

        return{

            "documents":docs,

            "average_words":round(avg,2)

        }