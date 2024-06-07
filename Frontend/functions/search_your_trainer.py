from models.search_your_trainer import InputModel, OutputModel
from utils.page import PageModel
import sqlite3

def execute(page: PageModel, key: str, model: InputModel) -> OutputModel:
    conn = sqlite3.connect('trainers.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT name, experience, specialty, photo_url FROM trainers WHERE name=?", (model.trainer_name,))
    result = cursor.fetchone()
    conn.close()

    if result:
        output = f"이름: {result['name']}, 경력: {result['experience']}, 전문 분야: {result['specialty']}"
        return OutputModel(output=output)
    else:
        return OutputModel(output="해당 트레이너의 정보를 찾을 수 없습니다.")
