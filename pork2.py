import sys
import os
class pork2(object):
    def __init__(self, num):
        self.Total_Card_cnt = 54 * 2.0
        self.res = self.pro2(num)
    def init_Pairs(self,num):
        res = {}
        singles = num
        pairs = 0
        while(singles >= 0):
            res[(pairs, singles)] = None
            singles = singles - 2
            pairs = pairs + 1
        return res
    
    def pro2(self,num):
        res = {}
        res[0] = self.init_Pairs(0)
        res[0][(0,0)] = 1.0
        for i in range(1, num+1):
            res[i] = self.init_Pairs(i)
            p_now = res[i]
            p_org = res[i-1]
            max_pair = i / 2
            Card_remain = self.Total_Card_cnt - (i - 1) # picking the i(th) cards, i-1 cards in hands
            for key in p_now.keys():
                p, s = key
                p_now[key] = 0.0
                if s > 0:
                    p_now[key] = p_now[key] + p_org[(p,s-1)]*(Card_remain-(s-1))/Card_remain
                if p > 0:
                    p_now[key] = p_now[key] + p_org[(p-1,s+1)]*(s+1)/Card_remain
        return p_now
class pork3(object):
    def __init__(self, num):
        self.Total_Card_cnt = 54 * 3.0
        self.res = self.pro3(num)
    def init_Treble(self, num):
        res = {}
        treble = 0
        pair = 0
        single = num
        while(single >= 0):
            tmp_t = 0
            tmp_s = single
            while(tmp_s >= 0):
                res[(tmp_t,pair,tmp_s)] = None
                tmp_t = tmp_t+1
                tmp_s = tmp_s - 3
            pair = pair + 1
            single = single - 2
        #print res
        return res
    def pro3(self, num):
        res={}
        res[0] = self.init_Treble(0)
        res[0][(0,0,0)] = 1.0
        for i in range(1, num+1):
            res[i] = self.init_Treble(i)
            p_now = res[i]
            p_org = res[i-1]
            Card_remain = self.Total_Card_cnt - (i - 1)
            for key in p_now.keys():
                t, p, s = key
                #print key
                #print p_org.keys()
                p_now[key] = 0.0
                if t>0 :
                    p_now[key] = p_now[key] + p_org[(t-1,p+1,s)]*(p+1)/Card_remain
                if p>0:
                    p_now[key] = p_now[key] + p_org[(t, p-1, s+1)]*2*(s+1)/Card_remain
                if s>0:
                    p_now[key] = p_now[key] + p_org[(t,p,s-1)]*(Card_remain-2*(s-1)-p)/Card_remain
        return p_now
def print_res2(p):
    for k,v in p.iteritems():
        p,s = k
        print p,s,v
def print_res3(p):
    for k,v in p.iteritems():
        t,p,s = k
        print t,p,s,v
def main():
    print "p3 26"
    p = pork3(26)
    print_res3(p.res)
    print "p2 25"
    p = pork2(25)
    print_res2(p.res)
  
if __name__=="__main__":
    main()
