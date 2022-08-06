import nltk
from nltk import FreqDist

from main import pre_process_text_file, compute_score, tokenize_no_puntctuation


def test_freq_dist():
    freq_dist = FreqDist(nltk.RegexpTokenizer(r"\w+").tokenize("This is a test text. "
                                                               "Nothing else matters! \n 332 new line\n"
                                                               "What is the purpose of this test? To test the text"))
    assert len(freq_dist) == 17 and {'the', 'test', 'text', 'is'} \
        .intersection(set([entry[0] for entry in freq_dist.most_common(4)])) == {'the', 'test', 'text', 'is'}


def test_compute_score():
    input_words = ["this", "is", "a", "random", "test", "just", "nothing", "special"]
    input_words_none = ["srgs", "gsf", "gsfg", "sfgfg", "hnhn", "qdqd", "czvv", "hhy"]
    input_text = "Received overcame oh sensible so at an. Formed do change merely to county it. " \
                 "Am separate contempt domestic to to oh. On relation my so addition branched." \
                 " Put hearing cottage she norland letters equally prepare too. " \
                 "Replied exposed savings he no viewing as up. Soon body add him hill. " \
                 "No father living really people estate if. Mistake do produce beloved demesne if am pursuit. " \
                 "With my them if up many. Lain week nay she them her she. " \
                 "Extremity so attending objection as engrossed gentleman something. " \
                 "Instantly gentleman contained belonging exquisite now direction she ham. West room at sent if year. " \
                 "Numerous indulged distance old law you. Total state as merit court green decay he. " \
                 "Steepest sex bachelor the may delicate its yourself. As he instantly on discovery concluded to. " \
                 "Open draw far pure miss felt say yet few sigh.Picture removal detract earnest is by. " \
                 "Esteems met joy attempt way clothes yet demesne tedious. " \
                 "Replying an marianne do it an entrance advanced. Two dare say play when hold. " \
                 "Required bringing me material stanhill jointure is as he. " \
                 "Mutual indeed yet her living result matter him bed whence. " \
                 "Admiration stimulated cultivated reasonable be projection possession of. " \
                 "Real no near room ye bred sake if some. Is arranging furnished knowledge agreeable so. " \
                 "Fanny as smile up small. It vulgar chatty simple months turned oh at change of. " \
                 "Astonished set expression solicitude way admiration. Death there mirth way the noisy merit. " \
                 "Piqued shy spring nor six though mutual living ask extent. " \
                 "Replying of dashwood advanced ladyship smallest disposal or. Attempt offices own improve now see. " \
                 "Called person are around county talked her esteem. Those fully these way nay thing seems. " \
                 "Two before narrow not relied how except moment myself. Dejection assurance mrs led certainly. " \
                 "So gate at no only none open. Betrayed at properly it of graceful on. " \
                 "Dinner abroad am depart ye turned hearts as me wished. " \
                 "Therefore allowance too perfectly gentleman supposing man his now. " \
                 "Families goodness all eat out bed steepest servants. " \
                 "Explained the incommode sir improving northward immediate eat. " \
                 "Man denoting received you sex possible you. Shew park own loud son door less yet. " \
                 "He my polite be object oh change. Consider no mr am overcame yourself throwing sociable children." \
                 " Hastily her totally conduct may. My solid by stuff first smile fanny." \
                 " Humoured how advanced mrs elegance sir who. Home sons when them dine do want to." \
                 " Estimating themselves unsatiable imprudence an he at an." \
                 " Be of on situation perpetual allowance offending as principle satisfied." \
                 " Improved carriage securing are desirous too. Post no so what deal evil rent by real in. " \
                 "But her ready least set lived spite solid. September how men saw tolerably two behaviour arranging. " \
                 "She offices for highest and replied one venture pasture. " \
                 "Applauded no discovery in newspaper allowance am northward. " \
                 "Frequently partiality possession resolution at or appearance unaffected he me. " \
                 "Engaged its was evident pleased husband. Ye goodness felicity do disposal dwelling no. " \
                 "First am plate jokes to began of cause an scale. " \
                 "Subjects he prospect elegance followed no overcame possible it on. " \
                 "But why smiling man her imagine married. " \
                 "Chiefly can man her out believe manners cottage colonel unknown. " \
                 "Solicitude it introduced companions inquietude me he remarkably friendship at. " \
                 "My almost or horses period. " \
                 "Motionless are six terminated man possession him attachment unpleasing melancholy. " \
                 "Sir smile arose one share. No abroad in easily relied an whence lovers temper by. " \
                 "Looked wisdom common he an be giving length mr.Knowledge nay estimable questions " \
                 "repulsive daughters boy. Solicitude gay way unaffected expression for. " \
                 "His mistress ladyship required off horrible disposed rejoiced. " \
                 "Unpleasing pianoforte unreserved as oh he unpleasant no inquietude insipidity. " \
                 "Advantages can discretion possession add favourable cultivated admiration far. " \
                 "Why rather assure how esteem end hunted nearer and before. " \
                 "By an truth after heard going early given he. Charmed to it excited females whether at examine. " \
                 "Him abilities suffering may are yet dependent."
    input_text_simple = "I have always loved this random test, just for fun, it is nothing special"
    input_text_proc = pre_process_text_file(input_text, lower=True, stemming=False, remove_stopwords=False)
    input_text_simple_proc = pre_process_text_file(input_text_simple, lower=True, stemming=False,
                                                   remove_stopwords=False)
    score = compute_score(input_text_proc, input_words)
    score_simple = compute_score(input_text_simple_proc, input_words)
    score_zero = compute_score(input_text_proc, input_words_none)
    score_zero_simple = compute_score(input_text_simple_proc, input_words_none)
    assert score == 12.4
    assert score_simple == 87.5
    assert score_zero == 0 and score_zero_simple == 0
