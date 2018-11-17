import scholarly
from typing import List, Dict, Tuple

class Study():
    def __init__(self, title: str, url: str, author: str):
        self.title = title
        self.url = url
        self.author = author

    def get_title(self):
        return self.title

    def get_url(self):
        return self.url

    def get_author(self):
        return self.author


def get_all_studies(keywords: List[str]) -> List[Study]:
    retval = []
    query = scholarly.search_pubs_query(' '.join(keywords))

    try:
        res = next(query)
        retval.append([Study(res.bib.title, res.bib.url, res.bib.author)])

    except StopIteration:
        pass

    return retval


def passes_filters(study: Study, filters: List[List[str]]) -> bool:
    study_kw = set(Study.get_title().split())
    for f in filters:
        filter_set = set(f)
        if len(study_kw & filter_set) > 0:
            continue
        else:
            return false
    return true

def filter_studies(studies: List[Study], filters: List[List[str]]) -> List[Study]:
    """
    Filters studies by title. Condition for inclusion is that the title contains
    one word from each filter list in filter
    Example: to get all studies with titles that contain
    (prevention, education, training) AND (violence, sexual, consent)
    use:
    [['prevention', 'education', 'training'], ['violence', 'sexual', 'consent']]
    as the filters argument
    """
    return [s for s in studies if passes_filters(s, filters)]

def main():

    filter1 = ['orientation', 'train', 'training', 'program', 'prevent', 'prevention', 'educate', 'education']
    filter2 = ['assault', 'violence', 'sexual', 'consent', 'rape']
    others = ['college', 'campus', 'effectiveness']
    keywords = filter1 + filter2 + others

    studies = get_all_studies(keywords)

    print("Found {} search results on Google Scholar".format(len(studies)))
    filters = [filter1, filter2]

    filtered_studies = filter_studies(studies, filters)

    print("After filtering, {} articles were deemed relevant".format(len(filtered_studies)))
