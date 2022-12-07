import psycopg2
class DaoSample:
    def __init__(self):
        self.connection = psycopg2.connect(database="python", user="postgres", password="python")
        self.cursor = self.connection.cursor()
 
    def selects(self):
        mydict =[]
        self.cursor.execute("SELECT col01,col02,col03 from sample")
        data=self.cursor.fetchall() 
        for i in data:
            mydict.append({'col01':i[0],'col02':i[1],'col3':i[2]})
            
        return mydict
    
    def select(self,col01):
        sql = f"""
            SELECT 
                col01,col02,col03 
            from 
                sample
            where
                col01 = '{col01}' 
        """
        
        self.cursor.execute(sql)
        rows=self.cursor.fetchall() 
        r = rows[0]
        ret = {'col01':r[0],'col02':r[1],'col3':r[2]}
        
        return ret
    
    def insert(self,col01,col02,col03):
        sql = f"""
            INSERT INTO sample
                (col01,col02,col03) 
            VALUES
                ({col01},{col02},{col03})
        """
        self.cursor.execute(sql)
        self.connection.commit()
        cnt = self.cursor.rowcount
        
        return cnt
        
    def update(self,col01,col02,col03):
        sql =f"""
            UPDATE sample 
            set 
                col02 = '{col02}', 
                col03 = '{col03}' 
            where 
                col01 = '{col01}'
        """
        self.cursor.execute(sql)
        self.connection.commit()
        cnt = self.cursor.rowcount
        
        return cnt

    def delete(self,col01):
        sql =f"""
            DELETE FROM sample 
            where 
                col01 ='{col01}';
        """
        self.cursor.execute(sql)
        self.connection.commit()
        cnt = self.cursor.rowcount
        
        return cnt

    def __del__(self):
        self.cursor.close()
        self.connection.close()
        
if __name__ == '__main__':
    ds = DaoSample()
    # list = ds.selects()
    # sample = ds.select('1')
    # cnt = ds.insert('4','4','4')
    # cnt = ds.update('4','6','6')
    # cnt = ds.delete('4')
    
    # print(sample)
    # print(cnt)
    # print(list)