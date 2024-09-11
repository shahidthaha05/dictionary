inst=[{'pname': 'synefo', 'id': 1, 'course':'python', 'time':10,'fees':40000},{'pname': 'novavi', 'id': 2, 'course':'java', 'time':12,'fees':50000}]
while True:
    print('''
1.institution details
2.view the institution 
3.update the institution 
4.delet the institution
5.search
6.add 
7.exit''')
    choice=int(input("enter the number :"))
    if choice==1:
          pname=str(input("enter name :"))
          id=int(input("enter id :"))
          coures=str(input("enter course :"))
          time=int(input("enter time :"))
          fees=int(input("enter fees :"))
          shop.append({'pname':name,'id':id,'course':course,'time':time,'fees':fees})
    elif choice==2:
         for i in inst:
              print(i)
    elif choice==3:
             id=int(input("enter id :"))
             f=0
             for i in inst:
                   if id == i['id']:
                         print('''
                                1.upadte id
                                2.upadte course
                                3.update time
                                4.update fees''')
                         choice=int(input("enter your choice :"))
                         if choice==1:
                               pname=str(input("enter name :"))
                               i['pname']=pname
                         elif choice==2:
                               course=str(input("enter course :"))
                               i['course']=course
                         elif choice==3:
                               time=int(input("enter time :"))
                               i['time']=time
                         elif choice==4:
                               fees=int(input("enter fees :"))
                               i['fees']=fees
                               f=1
                               if f==0:
                                    print('invalid name') 
    elif choice==4:
           id=int(input("enter id :"))
           f=0
           for i in inst:
                 if id == i['id']:
                       inst.remove(i)
                       f=1
           if f==0:
                 print('invalid name')
    elif choice==5:
           id=int(input("enter id :"))
           f=0
           for i in inst:
                 if id == i['id']:
                       print(i)
                       f=1
           if f==0:
                 print('invalid name')
    elif choice==6:
          break
    else:
          print('invalid choice')