# -*- coding: UTF-8 -*-

import MySQLdb
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 打开数据库连接
db = MySQLdb.connect("127.0.0.1", "dev", "123456", "music163", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

def create_db1():
    # 创建数据表SQL语句
    sql = """CREATE TABLE if not exists artists(
        SEQ int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
        ARTIST_ID varchar(32),
        ARTIST_NAME varchar(65),
        CATE_ID varchar(65),
        INITIAL int(5),
        primary key (seq),
        unique key ID (ARTIST_ID)
       )"""

    cursor.execute(sql)

def create_db2():
    # 创建数据表SQL语句
    sql = """CREATE TABLE if not exists albums(
        ALBUM_ID varchar(65),
        ARTIST_ID varchar(65),
        ARTIST_NAME varchar(100)
       )"""

    cursor.execute(sql)

def create_db3():
    # 创建数据表SQL语句
    sql = """CREATE TABLE if not exists musics(
        MUSIC_ID varchar(65),
        MUSIC_NAME varchar(65),
        ALBUM_ID varchar(65),
        ARTIST_ID varchar(65),
        ARTIST_NAME varchar(100)
       )"""

    cursor.execute(sql)


# 保存歌手
def insert_artist(artist_id, artist_name, cate_id, initial):
    sql ="""INSERT INTO artists 
    (ARTIST_ID, ARTIST_NAME, CATE_ID, INITIAL) 
    VALUES (%s, %s, %s, %s)
    """
    # sql = "INSERT INTO `artists` (`ARTIST_ID`, `ARTIST_NAME`) VALUES (%s, %s, %s, %d)"
    cursor.execute(sql, (artist_id, artist_name, cate_id, initial))
    db.commit()

# 获取歌手
def get_all_artist():
    sql = """SELECT
        ARTIST_ID 
        FROM artists
        ORDER BY 
        ARTIST_ID"""
    cursor.execute(sql)
    
    return cursor.fetchall()

# 获取歌手
def get_artist(album_id):
    sql = """SELECT
        ARTIST_ID,
        ARTIST_NAME
        FROM albums
        LEFT artists
        ON albums.ARTIST_ID = artists.ARTIST_ID 
        WHERE ALBUM_ID = %s
        """
    cursor.execute(sql, (album_id))
    
    return cursor.fetchall()

# 保存专辑
def insert_album(album_id, artist_id, artist_name):
    sql = "INSERT INTO `albums` (`ALBUM_ID`, `ARTIST_ID`, `ARTIST_NAME`) VALUES (%s, %s, %s)"
    cursor.execute(sql, (album_id, artist_id, artist_name))
    db.commit()

# 获取所有专辑的 ID
def get_all_album():
    sql = "SELECT `ALBUM_ID` FROM `albums` ORDER BY ALBUM_ID"
    cursor.execute(sql, ())
    return cursor.fetchall()
    
# 保存音乐
def insert_music(music_id, music_name, album_id, artist_id, artist_name):
    sql = "INSERT INTO `musics` (`MUSIC_ID`, `MUSIC_NAME`, `ALBUM_ID`, `ARTIST_ID`, `ARTIST_NAME`) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (music_id, music_name, album_id, artist_id, artist_name))
    connection.commit()

def dis_connect():
    db.close()

# create_db3()