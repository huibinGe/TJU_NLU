from databaseConn import MySqlHelper
import pymysql
import hosts
import json
#pymysql = MySqlHelper()
host = hosts.Hosts()

conn = pymysql.connect(host=host.host, port=host.port,
                            user=host.user, password=host.password, db=host.db)
cursor = conn.cursor()
query = "SELECT * FROM guesses1"
cursor.execute(query)
guesses = cursor.fetchall()
query = "SELECT * FROM novels1"
cursor.execute(query)
novels = cursor.fetchall()
f = open('shibiao_round2/with_context_step2.json', 'w', encoding='utf-8')
for guess_raw, novel_raw in zip(guesses, novels):
    novel_id1, _, _, guess,t_words1, is_right = guess_raw
    novel_id2, context, target_sentence, t_word2, extra, tag = novel_raw
    assert  novel_id1 == novel_id2
    assert  t_words1 == t_word2
    example = {
        'novel_id': novel_id1,
        'context': context,
        'target_sentence': target_sentence,
        't_words': t_words1,
        'guess': guess,
        'is_right': is_right
    }
    f.write(json.dumps(example, ensure_ascii=False) + '\n')
f.close()
