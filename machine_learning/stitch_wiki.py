 # coding=UTF-8
__author__ = 'digao'
__url__="https://www.hackerrank.com/challenges/stitch-the-torn-wiki"
import sys,StringIO,re

common_words=set("""I you me they are was years today before after later is was were last first at with in that the a
 of and is had have by""".split())

def read_text(line):
    tokens = set(re.split("\W",line))
    tokens.difference_update(common_words)
    return tokens


def main(input):
    N = int(input.readline())
    INPUTS = []
    for x in xrange(N):
        INPUTS.append(read_text(input.readline()))
    input.readline()

    points = []
    for x in xrange(N):
        cont = read_text(input.readline())
        pp = []
        points.append(pp)
        for OP in INPUTS:
            pp.append(len(OP.intersection(cont)))
    already = {}
    for pp  in points:
        max = 0
        max_index=0
        for i in xrange(len(pp)):
            p = pp[i]
            if p>max and i not in already:
                max_index=i
                max = p
        print max_index+1
        already[max_index]=True






test_input="""3
Delhi (also known as the National Capital Territory of India) is a metropolitan region in India that includes the national capital city, New Delhi. With a population of 22 million in 2011, it is the world's second most populous city and the largest city in India in terms of area. The NCT and its urban region have been given the special status of National Capital Region (NCR) under the Constitution of India's 69th amendment act of 1991. The NCR includes the neighbouring cities of Baghpat, Gurgaon, Sonepat, Faridabad, Ghaziabad, Noida, Greater Noida and other nearby towns, and has nearly 22.2 million residents.
Seattle is a coastal seaport city and the seat of King County, in the U.S. state of Washington. With an estimated 634,535 residents as of 2012, Seattle is the largest city in the Pacific Northwest region of North America and one of the fastest-growing cities in the United States. The Seattle metropolitan area of around 4 million inhabitants is the 15th largest metropolitan area in the nation.[6] The city is situated on a narrow isthmus between Puget Sound (an inlet of the Pacific Ocean) and Lake Washington, about 100 miles (160 km) south of the Canada–United States border. A major gateway for trade with Asia, Seattle is the 8th largest port in the United States and 9th largest in North America in terms of container handling.
Martin Luther OSA (10 November 1483 – 18 February 1546) was a German monk, Catholic priest, professor of theology and seminal figure of a reform movement in 16th century Christianity, subsequently known as the Protestant Reformation.[1] He strongly disputed the claim that freedom from God's punishment for sin could be purchased with money. He confronted indulgence salesman Johann Tetzel, a Dominican friar, with his Ninety-Five Theses in 1517. His refusal to retract all of his writings at the demand of Pope Leo X in 1520 and the Holy Roman Emperor Charles V at the Diet of Worms in 1521 resulted in his excommunication by the Pope and condemnation as an outlaw by the Emperor.
*****
The Seattle area had been inhabited by Native Americans for at least 4,000 years before the first permanent European settlers. Arthur A. Denny and his group of travelers, subsequently known as the Denny Party, arrived at Alki Point on November 13, 1851. The settlement was moved to its current site and named "Seattle" in 1853, after Chief Si'ahl of the local Duwamish and Suquamish tribes.
Although technically a federally administered union territory, the political administration of the NCT of Delhi today more closely resembles that of a state of India, with its own legislature, high court and an executive council of ministers headed by a Chief Minister. New Delhi is jointly administered by the federal government of India and the local government of Delhi, and is the capital of the NCT of Delhi.
Luther taught that salvation and subsequently eternity in heaven is not earned by good deeds but is received only as a free gift of God's grace through faith in Jesus Christ as redeemer from sin and subsequently eternity in hell. His theology challenged the authority of the Pope of the Roman Catholic Church by teaching that the Bible is the only source of divinely revealed knowledge from God and opposed sacerdotalism by considering all baptized Christians to be a holy priesthood. Those who identify with these, and all of Luther's wider teachings, are called Lutherans."""


#main(StringIO.StringIO(test_input))
main(sys.stdin)
