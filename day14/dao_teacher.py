import psycopg2


class DaoTe:
    def __init__(self):
        self.conn = psycopg2.connect(database="python", user="postgres", password="python")
        self.cur = self.conn.cursor()
    
    #삽입     
    def insert(self,t_name,mobile,addr):
        
        sql = f"""
            insert into teacher
            (t_id,t_name,mobile,addr)
            values(nextval('t_seq'),'{t_name}','{mobile}','{addr}')
        """
        self.cur.execute(sql)
        self.conn.commit()
        return self.cur.rowcount
    
    # #수정 
    def update(self,t_id,t_name,mobile,addr):
        sql = f"""
            update teacher
            set
            t_name = '{t_name}',
            mobile = '{mobile}',
            addr = '{addr}'
            where t_id='{t_id}' 
        """
        self.cur.execute(sql)
        self.conn.commit()
        return self.cur.rowcount
    #
    def select(self,t_id):
        sql = f"""
            select t_id,t_name,mobile,addr from teacher where t_id='{t_id}'  
        """
        self.cur.execute(sql)
        rows=self.cur.fetchall()
        r = rows[0]
        ret = {'t_id':r[0],'t_name':r[1],'mobile':r[2],'addr':r[3]}
        return ret
    
    # #여러개선택 
    def selects(self):
    
        mychoice=[]
        self.cur.execute("select t_id,t_name,mobile,addr from teacher order by t_id desc")
        rows=self.cur.fetchall()
    
        for r in rows:
            mychoice.append({'t_id':r[0],'t_name':r[1],'mobile':r[2],'addr':r[3]})
        return mychoice
    
    # #삭제
    def delete(self,t_id):
        sql=f"""
            delete from teacher 
            where t_id='{t_id}'
        """
        self.cur.execute(sql)
        print("cnt",self.cur.rowcount)
        self.conn.commit()
        return self.cur.rowcount
   
    def __del__(self):
        self.cur.close();    
        self.conn.close();
        
        
if __name__ == '__main__':
    dt= DaoTe()
    #cnt = dt.insert('3','3','3')  
    #cnt = dt.update(3,'이름2','성별2','주소2')
    cnt = dt.delete(11)
    #emp = dt.select(5)
    #list = dt.selects()
    #print(emp)

  
     
     
      
     
               
            