import psycopg2
class dao_emp:
    def __init__(self):
        self.connection = psycopg2.connect(database="python", user="postgres", password="python")
        self.cursor = self.connection.cursor()
 
    def selects(self):
        mydict =[]
        sql = f"""
            SELECT 
                E_ID,E_NAME,SEX,ADDR
            from 
                EMP
            order by E_ID
        """
        self.cursor.execute(sql)
        data=self.cursor.fetchall() 
        for i in data:
            mydict.append({'E_ID':i[0],'E_NAME':i[1],'SEX':i[2],'ADDR':i[3]})
            
        return mydict
    
    def select(self,e_id):
        sql = f"""
            SELECT 
                E_ID,E_NAME,SEX,ADDR
            from 
                EMP
            where
                E_ID = '{e_id}' 
        """
        
        self.cursor.execute(sql)
        rows=self.cursor.fetchall() 
        r = rows[0]
        ret = {'E_ID':r[0],'E_NAME':r[1],'SEX':r[2],'ADDR':r[3]}
        
        return ret
    
    def insert(self,e_id,e_name,sex,addr):
        sql = f"""
            INSERT INTO EMP
                (E_ID,E_NAME,SEX,ADDR)
            VALUES
                ({e_id},{e_name},{sex},{addr})
        """
        self.cursor.execute(sql)
        self.connection.commit()
        cnt = self.cursor.rowcount
        
        return cnt
        
    def update(self,e_id,e_name,sex,addr):
        sql =f"""
            UPDATE EMP 
            set 
                e_name = '{e_name}', 
                sex = '{sex}',
                addr = '{addr}' 
            where 
                e_id = '{e_id}'
        """
        self.cursor.execute(sql)
        self.connection.commit()
        cnt = self.cursor.rowcount
        
        return cnt

    def delete(self,e_id):
        sql =f"""
            DELETE FROM EMP 
            where 
                e_id ='{e_id}';
        """
        self.cursor.execute(sql)
        self.connection.commit()
        cnt = self.cursor.rowcount
        
        return cnt

    def __del__(self):
        self.cursor.close()
        self.connection.close()
        
if __name__ == '__main__':
    de = dao_emp()
    list = de.selects()
    sample = de.select('1')
    # cnt = de.insert('4','4','4','4')
    # cnt = de.update('4','6','6','6')
    # cnt = de.delete('4')
    
    print(sample)
    # print(cnt)
    print(list)