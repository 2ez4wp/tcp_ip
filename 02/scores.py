# coding: utf-8
def scores():
    scorelist = list()
    i = 0
    while(i <= 9):
        score = float(raw_input("input  scores (1<=score<=100)\n"))
        if score >=1 and score <=100:
            scorelist.append(score)
            i = i + 1
        
    scoremax = max(scorelist)
    scoremin = min(scorelist)
    sum_scores = sum(scorelist)
    print scorelist
    avg = float(sum_scores - scoremax - scoremin) / 8
    type(avg)
    return avg
    
if __name__ == "__main__":
    print ("score: %.1f"% scores())
    
    
