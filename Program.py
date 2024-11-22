#clear screen
import os
def clear_screen():
    if os.name == 'nt': 
        os.system('cls')

#clear ทีละบรรทัด
def clear_area(lines=1):
    for _ in range(lines):
        print("\033[F\033[K", end='')  # "\033[F" เลื่อนขึ้นบรรทัด และ "\033[K" ลบบรรทัด

#เมนูตัวเลือก
def menu_2choices():
    while True:
        choices=[1,2]
        try:    
            number=int(input('ป้อนตัวเลือก 1 หรือ 2 :  ').strip())
            if number in choices:
                return number
            elif number<1 or number>2:
                clear_area(2)
                print('กรุณาป้อนตัวเลข 1 หรือ 2 เท่านั้น')               
        except ValueError:
            clear_area(2)
            print('กรุณาป้อนเฉพาะตัวเลข')
            

def menu_3choices():
    while True:
        choices=[1,2,3]
        try:    
            number=int(input('ป้อนตัวเลือก 1, 2 หรือ 3:  ').strip())
            if number in choices:
                return number
            elif number<1 or number>3:
                clear_area(2)
                print('กรุณาป้อนตัวเลข 1, 2 หรือ 3 เท่านั้น')
        except ValueError:
            clear_area(2)
            print('กรุณาป้อนเฉพาะตัวเลข')

def menu_4choices():
    while True:
        choices=[1,2,3,4]
        try:    
            number=int(input('ป้อนตัวเลข 1, 2, 3 หรือ 4:  ').strip())
            if number in choices:
                return number
            elif number<1 or number>4:
                clear_area(2)
                print('กรุณาป้อนตัวเลข 1, 2, 3 หรือ 4 เท่านั้น')
        except ValueError:
            clear_area(2)
            print('กรุณาป้อนเฉพาะตัวเลข')

def menu_5choices():
    while True:
        choices=[1,2,3,4,5]
        try:    
            number=int(input('ป้อนตัวเลข 1, 2, 3, 4 หรือ 5:  ').strip())
            if number in choices:
                return number
            elif number<1 or number>5:
                clear_area(2)
                print('กรุณาป้อนตัวเลข 1, 2, 3, 4 หรือ 5 เท่านั้น')
        except ValueError:
            clear_area(2)
            print('กรุณาป้อนเฉพาะตัวเลข')

#หน้าแรก
def mainPage():
    clear_screen()
    print('********หน้าหลัก********')
    print('*      1.บัตรคิว       *')
    print('*       2.ดูข้อมูล      *')
    print('*    3.ปิดโปรแกรม     *')
    print('**********************')
    wordVip,wordNormal=useData()
    number=menu_3choices()
    return number

#หน้าข้อมูล
def showData():
    clear_screen()
    try:
        with open('data.txt','r',encoding='utf-8') as fr:
            lines=fr.readlines()
            if lines:
                for line in lines:
                    words=line.split()
                    line=line.replace(words[-1],' คน และ '+words[-1])
                    for word in words:
                        if word.startswith('V'):
                            line=line.replace(word,'คิว VIP ที่ '+word)
                        if word.startswith('N'):
                            line=line.replace(word,'คิว Normal ที่ '+word)
                        if word.startswith('a'):
                            line=line.replace(word,'สำหรับ'+'ผู้ใหญ่ ')
                        if word.startswith('c'):
                            line=line.replace(word,'สำหรับ'+'เด็ก ')  
                    print(line)
            elif not lines:
                raise Exception('ไม่มีข้อมูลในไฟล์ให้แสดง')
    except FileNotFoundError:
        with open('data.txt','x',encoding='utf-8'):
            print('ไม่พบไฟล์')
            print('กำลังสร้างไฟล์ใหม่')
        print('สร้างไฟล์ใหม่สำเร็จ')
        print('')
    except Exception as e:
        print(e)
    import msvcrt
    print('กดปุ่มใดๆเพื่อย้อนกลับ : ')
    msvcrt.getch()

#หน้าบัตรคิว
def orderPage_1():
    clear_screen()
    #หน้า2.1
    print('********บัตรคิว***********')
    print('*    1.บัตรแบบ VIP      *')
    print('*   2.บัตรแบบธรรมดา     *')
    print('************************')
    print('*   3.ยกเลิกการสั่งซื้อ     *')
    print('************************')
    print('')
    number=menu_3choices()
    group={'class':'','age':'','amount':''}
    if number==1:
        group['class']='vip'
    else:
        group['class']='normal'
    return number,group

#หน้า2.2
def orderPage_2(group):
    clear_screen()
    print('********บัตรคิว*********')
    print('*       1.ผู้ใหญ่      *')
    print('*       2.เด็ก        *')
    print('**********************')
    print('*   3.ยกเลิกการสั่งซื้อ   *')
    print('**********************')
    print('')
    number=menu_3choices()
    if number==1:
        group['age']='adults'
    elif number==2:
        group['age']='children'
    return number,group

#หน้า2.3
def orderPage_3(group):
    clear_screen()
    print('********บัตรคิว*********')
    print('*      จำนวนคน       *')
    print('**********************')
    print('')
    while True:
        try:            
            amount=int(input('ป้อนจำนวนคน :  ').strip())
            if amount>0:
                break
            elif amount<=0:
                clear_area(2)
                print('กรุณาป้อนจำนวนขั้นต่ำ 1 คน')
        except ValueError:
            clear_area(2)
            print('กรุณาป้อนจำนวนเฉพาะตัวเลข')
    group['amount']=amount
    #clear_area(1)
    #number=menu_3choices()
    return group

#หน้าสรุปยอด
def summaryPage(group):
    clear_screen()
    w=group['class']
    x=group['age']
    y=group['amount']
    print('********สรุปยอด**********')
    print('*',w,x,'จำนวน',y,'คน','*')
    print('************************')
    print('*       1.ชำระเงิน      *')
    print('*        2.แก้ไข       *')
    print('*     3.ยกเลิกการซื้อ    *')
    print('************************')
    print('')
    number=menu_3choices()
    return w,x,y,number

#ราคาตั๋ว
ratePrice={
    'vip':{
        'adults':1000,
        'children':700
    },
    'normal':{
        'adults':800,
        'children':500
    }
}

#หน้าชำระเงิน
def paymentPage(w,x,y):
    clear_screen()
    rate=ratePrice[w][x]
    totalPrice=rate*y
    print('********ชำระเงิน**********')
    print('*',w,x,'จำนวน',y,'คน','*')
    print('*     รวม ',totalPrice,'บาท     *')
    print('************************')
    print('*    1.ชำระเงินเสร็จสิ้น    *')
    print('*        2.แก้ไข        *')
    print('*     3.ยกเลิกการซื้อ     *')
    print('************************')
    print('')
    number=menu_3choices()
    return number      

#ดึงข้อมูลจากไฟล์
def useData():
    try:
        with open('data.txt','r',encoding='utf-8') as fr:
            lines=fr.readlines()
            if lines: #checkว่ามีบรรทัดมั้ย
                line=lines[-1]
                words=line.split()
                for word in words:
                    if word.startswith('V'):
                        wordVip=word[1:]
                    if word.startswith('N'):
                        wordNormal=word[1:]
                print('ดึงข้อมูลสำเร็จ')
            if not lines:
                raise Exception('ไม่มีข้อมูลในไฟล์')
    except FileNotFoundError:
        with open('data.txt','x',encoding='utf-8'):
            wordVip='000'
            wordNormal='000'
            print('ไม่พบไฟล์')
            print('กำลังสร้างไฟล์ใหม่')
        print('สร้างไฟล์ใหม่สำเร็จ')
        print('')
    except Exception as e :
        wordVip='000'
        wordNormal='000'
        print(e)    
    return wordVip, wordNormal

#check date
def checkDate():
    with open('data.txt','r',encoding='utf-8') as fr:
        lines=fr.readlines()
        if lines: #checkว่ามีบรรทัดมั้ย
            line=lines[-1]
            date=line[8:10].strip()
            from datetime import datetime
            today = datetime.now()
            today = today.strftime('%d').strip()
            if today==date:
                return True
            else:
                return False 
        elif not lines:
            return False

#เลขคิว
def queuePage(w,y,wordVip,wordNormal): 
    clear_screen()
    is_same_day=checkDate()
    if is_same_day==False:
        wordVip='000'
        wordNormal='000'
    queueVIP=int(wordVip)
    queueNormal=int(wordNormal)
    allQueueVip=[]
    allQueueNormal=[]
    for i in range(y):       
        if w=='vip':
            queueVIP+=1
            queueVIP_str=f"V{queueVIP:03}" #ทำให้เป็น 001 แบบ3หลัก แบบstr
            allQueueVip.append(queueVIP_str)
            queueNormal_str=f"N{queueNormal:03}" #ทำให้เป็น 001 แบบ3หลัก แบบstr
            allQueueNormal.append(queueNormal_str)
        elif w=='normal':
            queueNormal+=1
            queueNormal_str=f"N{queueNormal:03}" #ทำให้เป็น 001 แบบ3หลัก แบบstr
            allQueueNormal.append(queueNormal_str)
            queueVIP_str=f"V{queueVIP:03}" #ทำให้เป็น 001 แบบ3หลัก แบบstr
            allQueueVip.append(queueVIP_str)
    print('********บัตรคิว**********')
    if w=='vip':
        for item in range(len(allQueueVip)):
            print(f'*    {allQueueVip[item]}     *')
    elif w=='normal':
        for item in range(len(allQueueNormal)):
            print(f'*   {allQueueNormal[item]}   *')
    print('************************')
    print('*       เสร็จสิ้น         *')
    print('************************')
    print('')
    import msvcrt
    print('กดปุ่มใดๆเพื่อย้อนกลับ : ')
    msvcrt.getch()         
    return allQueueVip,allQueueNormal

#timestamp
def timeStamp():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d")

#save data in file
def storeData(w,x,y,allQueueVip,allQueueNormal):
    current_timestamp=timeStamp()
    try:
        with open('data.txt','a',encoding='utf-8') as fa:
            if w=='vip':
                fa.write(f'{current_timestamp} : {allQueueVip[-1]} {x} {y} {allQueueNormal[-1]}\n')
            elif w=='normal':
                fa.write(f'{current_timestamp} : {allQueueNormal[-1]} {x} {y} {allQueueVip[-1]}\n')           
    except  FileNotFoundError:
        with open('data.txt','w',encoding='utf-8') as fw:
            if w=='vip':
                fa.write(f'{current_timestamp} : {allQueueVip[-1]} {x} {y} {allQueueNormal[-1]}\n')
            elif w=='normal':
                fa.write(f'{current_timestamp} : {allQueueNormal[-1]} {x} {y} {allQueueVip[-1]}\n')   
    clear_screen()  
    
#การทำงานหลัก
while True:
    click=mainPage()
    found=False
    if click==1:
        while True:
            if found==True:
                break
            click,group=orderPage_1()
            if click==1 or click==2:
                while True:
                    if found==True:
                        break
                    elif found=='op1':
                        found=False
                        break
                    click,group=orderPage_2(group)
                    if click==1 or click==2:
                        while True:
                            if found==True:
                                break
                            elif found=='op1':
                                break
                            group=orderPage_3(group)
                            while True:
                                if found==True:
                                    break
                                elif found=='op1':
                                    break
                                w,x,y,click=summaryPage(group)
                                if click==1:
                                    while True:
                                        click=paymentPage(w,x,y)   
                                        if click==1:
                                                    wordVip,wordNormal=useData()
                                                    allQueueVip,allQueueNormal=queuePage(w,y,wordVip,wordNormal)
                                                    storeData(w,x,y,allQueueVip,allQueueNormal)
                                                    found=True
                                                    break
                                        elif click==2:
                                            found='op1'
                                            break
                                        elif click==3:
                                                found=True
                                                break
                                elif click==2:
                                    found='op1'
                                    break
                                elif click==3:
                                    found=True
                                    break                                                
                    elif click==3:
                        found=True
                        break      
            elif click==3:
                found=True 
                break 
    elif click==2:
        showData()
    elif click==3:
        break

 

        