import nltk
from nltk import FreqDist


def test_freq_dist():
    freq_dist =FreqDist(nltk.RegexpTokenizer(r"\w+").tokenize("This is a test text. "
                                                              "Nothing else matters! \n 332 new line\n"
                                                              "What is the purpose of this test? To test the text"))
    assert len(freq_dist) == 17 and {'the','test','text', 'is'}\
        .intersection(set([entry[0] for entry in freq_dist.most_common(4)])) == {'the','test','text', 'is'}
