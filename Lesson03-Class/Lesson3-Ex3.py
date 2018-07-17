class Life:
    
    def __init__(self,the_map,num):

        self.my_map=the_map
        self.my_num=num

    def display(self):
        
        rowcol = self.my_map
        listout = []
        listin = []
        row = 1
        column = 1
        
        while column <= rowcol:
            listin.append("*")
            column += 1
        while row <= rowcol:
            listout.append(list(listin))
            row += 1

        if self.my_num == 1:
    
            nl=list(listout)

    #First
            nl[(len(nl)-2)//2][(len(nl)-2)//2]="0" 
            nl[(len(nl)-2)//2][(len(nl))//2]="0" 
            nl[(len(nl)-2)//2][(len(nl)+2)//2]="0" 

    #Second
            nl[(len(nl))//2][(len(nl)-2)//2]="0"  

    #Third
            nl[(len(nl)+2)//2][(len(nl))//2]="0"  

            for i in nl:
                print(' '.join(i))
        
        if self.my_num == 0:
            nl2=list(listout)
            for i in nl2:
                print(' '.join(i))
        
        return ""

x=Life(5,1)
print(x.display())