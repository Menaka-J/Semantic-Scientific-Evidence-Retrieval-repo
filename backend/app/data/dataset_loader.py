import json
from pathlib import Path

class DatasetLoader:

    def __init__(self, corpus_path):
        self.corpus_path = corpus_path

    def load_corpus(self):

        papers=[]

        with open(self.corpus_path,"r",encoding="utf-8") as file:

            for line in file:

                paper=json.loads(line)

                # abstract=" ".join(paper["abstract"])
                abstract = " ".join(

    paper.get(

        "abstract",

        []

    )

)

                papers.append({

                    "doc_id":paper["doc_id"],

                    # "title":paper["title"],
                    "title": paper.get(

    "title",

    "Unknown"

),

                    "abstract":abstract,

                    "combined_text":paper["title"]+" "+abstract

                })

        return papers