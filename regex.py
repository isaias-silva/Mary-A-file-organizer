import re
def converter(preregex:str):
     padroes = preregex.split('|')
    
    
     regex_padroes = []
     
     for p in padroes:
        regex = re.escape(p)  
        regex = regex.replace(r'\*', '.*')  
        regex_padroes.append(f'^{regex}$')  

     
     return re.compile('|'.join(regex_padroes))
    
def isMatch(regex:re.Pattern,text:str):
    return re.match(regex,text)