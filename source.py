T = int(input())
score_list = []
if T>=1 and T<= 1000:
    for turn in range(T):
        s = [*input()]
        if len(s)>= 1 and len(s)<= 60:
            over_k = ''
            runs_k = ''
            wicket_k = ''
            
            runs = ['0', '1', '2', '3', '4', '5', '6']
            t_runs = 0
            t_w = 0 
            t_over = 0
            for i in range(len(s)):
                if s[i] in runs :
                    run = int(s[i])
                    t_runs += run
                if s[i] == 'W':
                    t_w += 1
            
            l = len(s)
            if l >= 6:
                o = l // 6
                no = (l - 6 * o)/10
                t_over = o + no
                
            else:
                t_over  = l/10
                
            if t_runs > 1:
                runs_k = 'Runs'
            else:
                runs_k = 'Run'
                
            if t_w > 1:
                wicket_k = 'Wickets.'
            else:
                wicket_k = 'Wicket.'
            
            if t_over > 1:
                over_k = 'Overs'
            else:
                over_k = 'Over'
            # print(f"{t_over} {over_k} {t_runs} {runs_k} {t_w} {wicket_k}") 
            score_list.append(f"{t_over} {over_k} {t_runs} {runs_k} {t_w} {wicket_k}")
        
    for i in score_list:
        print(i)
