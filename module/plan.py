import os
import sqlite3

from model.plan import CreatePlan, UpdatePlan, ReadPlan, DeletePlan

DB_NAME = os.getenv("DB_NAME")
# model

DB_NAME = "app.db"


conn = sqlite3.connect(DB_NAME)
conn.row_factory = sqlite3.Row
cur = conn.cursor()


def create_plan(plan: CreatePlan, user_id: str) -> None:
    """
    運動予定を1件追加する関数
    :param plan: CreatePlan
    :param user_id: str
    :return:
    """
    cur.execute("INSERT INTO plan(user_id, plan_name, start_time, end_time, plan_notes) VALUES(?, ?, ?, ?, ?)",
                (user_id,
                 plan.plan_name,
                 plan.start_time,
                 plan.end_time,
                 plan.plan_notes))
    conn.commit()

    return


# 保留　ちょっと構造考える
def update_plan(plan: UpdatePlan, user_id: str) -> None:
    cur.execute("UPDATE plan SET user_id = ?, plan_name = ?, start_time")


def read_plan(user_id: str) -> list:
    """
    運動予定をリストで返す関数
    :param user_id: str
    :return: list
    """
    cur.execute("SELECT id, plan_name, start_time, end_time, plan_notes "
                "FROM plan WHERE user_id = ? ",
                (user_id, ))

    response_list = cur.fetchall()
    return response_list


def delete_plan(plan: DeletePlan, user_id: str) -> None:
    """
    運動予定を1件削除する関数
    :param plan: DeletePlan
    :param user_id: str
    :return:
    """
    cur.execute("DELETE FROM plan WHERE id = ? AND user_id = ?",
                (plan.id_, user_id))
    conn.commit()

    return
