import os
import sqlite3

# DB_NAME = os.getenv("DB_NAME")
from model.result import Result

DB_NAME = "app.db"

conn = sqlite3.connect(DB_NAME)
conn.row_factory = sqlite3.Row
cur = conn.cursor()


def create_result(result: Result, user_id: str) -> None:
    """
    運動結果を1件追加する関数
    :param result: Result
    :param user_id: str
    :return:
    """

    cur.execute("INSERT INTO result(user_id, result_name, result_count, result_time) VALUES(?, ?, ?, ?)",
                (user_id,
                 result.result_name,
                 result.result_count,
                 result.result_time))
    conn.commit()
    return


def update_result(result: Result,
                  user_id: str) -> None:
    """
    運動結果を1件更新する関数
    :param result:
    :param user_id:
    :return:
    """

    cur.execute("UPDATE result SET user_id = ?, result_name = ?, result_count = ?, result_time = ? WHERE id = ?",
                (user_id,
                 result.result_name,
                 result.result_count,
                 result.result_time,
                 result.id_, ))
    conn.commit()
    return


def read_result(result: Result,
                user_id: str) -> list:
    """
    運動結果をリストで返す関数
    :param user_id: str
    :return:
    """

    cur.execute("SELECT result_time as argument, result_count as value "
                "FROM result WHERE result_name = ? and user_id = ?",
                (result.result_name, user_id, ))

    response_list = cur.fetchall()
    return response_list


def delete_result(result: Result,
                  user_id: str) -> None:
    """
    運動結果を1件削除する関数
    :param result: Result
    :param user_id: str
    :return:
    """

    cur.execute("DELETE FROM result WHERE id = ? AND user_id = ?",
                (result.id_, user_id))
    return
