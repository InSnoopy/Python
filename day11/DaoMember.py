import psycopg2


class DaoMember:

    def __init__(self):
        self.connection = psycopg2.connect(database="python", user="postgres", password="python")
        self.cursor = self.connection.cursor()

    def selects(self):
        mydict = []
        self.cursor.execute("SELECT m_id,m_nm,tel,ymd from member")
        data = self.cursor.fetchall() 
        for i in data:
            mydict.append({'m_id':i[0], 'm_nm':i[1], 'tel':i[2], 'ymd':i[3]})
            
        return mydict
    
    def select(self,m_id):
        sql = f"""
            SELECT 
                m_id,m_nm,tel,ymd
            from 
                member
            where
                m_id = '{m_id}' 
        """
        
        self.cursor.execute(sql)
        rows=self.cursor.fetchall() 
        r = rows[0]
        ret = {'m_id':r[0], 'm_nm':r[1], 'tel':r[2], 'ymd':r[3]}
        
        return ret
    
    def insert(self, m_id, m_nm, tel, ymd):
        sql = f"""
            INSERT INTO member
                (m_id,m_nm,tel,ymd)
            VALUES
                ({m_id},{m_nm},{tel},{ymd})
        """
        self.cursor.execute(sql)
        self.connection.commit()
        cnt = self.cursor.rowcount
        
        return cnt


    def update(self, m_id, m_nm, tel, ymd):
        sql =f"""
            UPDATE member 
            set 
                m_nm = '{m_nm}', 
                tel = '{tel}',
                ymd = '{ymd}' 
            where 
                m_id = '{m_id}'
        """
        self.cursor.execute(sql)
        self.connection.commit()
        cnt = self.cursor.rowcount
        
        return cnt
    
    def delete(self,m_id):
        sql =f"""
            DELETE FROM member 
            where 
                m_id ='{m_id}';
        """
        self.cursor.execute(sql)
        self.connection.commit()
        cnt = self.cursor.rowcount
        
        return cnt
    
    def __del__(self):
        self.cursor.close()
        self.connection.close()

        
if __name__ == '__main__':
    dm = DaoMember()
    # list = dm.selects()
    # sample = dm.select('4')
    # cnt = dm.insert('4', '4', '4', '4')
    # cnt = dm.update('4','6','6','6')
    # cnt = dm.delete('4')
    
    # print(sample)
    # print(cnt)
    # print(list)
