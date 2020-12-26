import pymysql

#创建数据库连接，注意这里我加入了charset和cursorclass参数
conn = pymysql.connect(
    host = "127.0.0.1",
    user = "root",
    password = "******",
    database = "cbioportal",
    charset = 'utf8',
    cursorclass = pymysql.cursors.DictCursor)
#获取游标
cursor = conn.cursor()
insert_mutation_sql = 'INSERT INTO mutations(cancer_type,hugo_symbol, protein_change, mutation_type, refseq_mrna_id, tumor_alt_count, tumor_ref_count, study_id, sample_id, create_time, update_time, status) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

def do_sql_insert(par):
    try:
        cursor.execute(insert_mutation_sql,par)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)
        return 1

    return 0

def do_sql_count(table_name):
    sql = 'SELECT count(*) from ' + table_name
    cursor.execute(sql)
    count = cursor.fetchone()['count(*)']
    return count

def close_sql_connection():
    cursor.close()
    conn.close()


