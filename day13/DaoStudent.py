import psycopg2
class DaoStudent:
    def __init__(self):
        self.connection = psycopg2.connect(database="python", user="postgres", password="python")
        self.cursor = self.connection.cursor()
 
    def selects(self):
        mydict =[]
        sql = f"""
            SELECT 
                s_id,s_name, mobile,address
            from 
                student
            order by s_id
        """
        self.cursor.execute(sql)
        data=self.cursor.fetchall() 
        for i in data:
            mydict.append({'s_id':i[0],'s_name':i[1],'mobile':i[2],'address':i[3]})
            
        return mydict

    def select(self,s_id):
        sql = f"""
            SELECT 
                s_id,s_name, mobile,address
            from 
                student
            where
                s_id = '{s_id}' 
        """
        
        self.cursor.execute(sql)
        rows=self.cursor.fetchall() 
        r = rows[0]
        ret = {'s_id':r[0],'s_name':r[1],'mobile':r[2],'address':r[3]}
        
        return ret

    def insert(self,s_id,s_name,mobile,address):
        sql = f"""
            INSERT INTO student
                (s_id,s_name, mobile,address)
            VALUES
                ({s_id},{s_name},{mobile},{address})
        """
        self.cursor.execute(sql)
        self.connection.commit()
        cnt = self.cursor.rowcount
        
        return cnt
        
    def update(self,s_id,s_name,mobile,address):
        sql =f"""
            UPDATE student 
            set 
                s_name = '{s_name}', 
                mobile = '{mobile}',
                address = '{address}' 
            where 
                s_id = '{s_id}'
        """
        self.cursor.execute(sql)
        self.connection.commit()
        cnt = self.cursor.rowcount
        
        return cnt
    
    def delete(self,s_id):
        sql =f"""
            DELETE FROM student 
            where 
                s_id ='{s_id}';
        """
        self.cursor.execute(sql)
        self.connection.commit()
        cnt = self.cursor.rowcount
        
        return cnt

    def __del__(self):
        self.cursor.close()
        self.connection.close()
        
if __name__ == '__main__':
    ds = DaoStudent()
    # list = ds.selects()
    # sample = ds.select('1')
    cnt = ds.insert(2,'4','4','4')
    # cnt = ds.update('1','6','6','6')
    # cnt = ds.delete('1')
    
    # print(sample)
    print(cnt)
    # print(list)