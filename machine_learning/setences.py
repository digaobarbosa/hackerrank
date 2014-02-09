__author__ = 'digao'
__url__ = "https://www.hackerrank.com/challenges/from-paragraphs-to-sentences"

import sys,StringIO
import re
puncts = ['.','?','!']

def main(input):
    tokens = re.split("([?!\.\s])",input.read())
    begin_set = 0
    inside_quote = False
    setences = []
    for i in xrange(len(tokens)):
        token = tokens[i]
        if len(token)==0:
            continue
        if not inside_quote and token[0]=='"':
            inside_quote=True
        elif inside_quote and (token[-1]=='"' or (len(token)>1 and token[-2]=='"')):
            inside_quote = False
        if not inside_quote and token[-1] in puncts:
            setences.append(''.join(tokens[begin_set:i+1]).strip())
            begin_set = i+1

    for set in setences:
        print set



test_input = """In the third category he included those Brothers (the majority) who saw nothing in Freemasonry but the external forms and ceremonies, and prized the strict performance of these forms without troubling about their purport or significance. Such were Willarski and even the Grand Master of the principal lodge. Finally, to the fourth category also a great many Brothers belonged, particularly those who had lately joined. These according to Pierre's observations were men who had no belief in anything, nor desire for anything, but joined the Freemasons merely to associate with the wealthy young Brothers who were influential through their connections or rank, and of whom there were very many in the lodge.Pierre began to feel dissatisfied with what he was doing. Freemasonry, at any rate as he saw it here, sometimes seemed to him based merely on externals. He did not think of doubting Freemasonry itself, but suspected that Russian Masonry had taken a wrong path and deviated from its original principles. And so toward the end of the year he went abroad to be initiated into the higher secrets of the order.What is to be done in these circumstances? To favor revolutions, overthrow everything, repel force by force?No! We are very far from that. Every violent reform deserves censure, for it quite fails to remedy evil while men remain what they are, and also because wisdom needs no violence. "But what is there in running across it like that?" said Ilagin's groom. "Once she had missed it and turned it away, any mongrel could take it," Ilagin was saying at the same time, breathless from his gallop and his excitement.
"""
test2 = """"But what is there in running across it like that?" said Ilagin's groom. "Once she had missed it and turned it away, any mongrel could take it," Ilagin was saying at the same time, breathless from his gallop and his excitement."""
#main(StringIO.StringIO(test_input))
main(sys.stdin)
