import json
import os
from typing import List, Dict, Any

DATA_FILE = os.path.join(os.path.dirname(__file__), "database.json")

def load_data() -> Dict[str, Any]:
    if not os.path.exists(DATA_FILE):
        default_data = {
            "questions": [],  # List of {"id": int, "text": str, "options": {"A": "", "B": "", "C": "", "D": ""}, "correct": "A"}
            "results": [],    # List of {"user_id": int, "full_name": str, "username": str, "score": int, "total": int, "details": []}
            "next_id": 1
        }
        save_data(default_data)
        return default_data
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"questions": [], "results": [], "next_id": 1}

def save_data(data: Dict[str, Any]) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_questions() -> List[Dict[str, Any]]:
    data = load_data()
    return data.get("questions", [])

def add_question(text: str, options: Dict[str, str], correct: str) -> int:
    data = load_data()
    qid = data.get("next_id", 1)
    data["questions"].append({
        "id": qid,
        "text": text,
        "options": options,
        "correct": correct.upper()
    })
    data["next_id"] = qid + 1
    save_data(data)
    return qid

def delete_question(qid: int) -> bool:
    data = load_data()
    initial_count = len(data.get("questions", []))
    data["questions"] = [q for q in data.get("questions", []) if q["id"] != qid]
    if len(data["questions"]) != initial_count:
        save_data(data)
        return True
    return False

def clear_all_questions() -> None:
    data = load_data()
    data["questions"] = []
    data["next_id"] = 1
    save_data(data)

def save_result(user_id: int, full_name: str, username: str, score: int, total: int, details: List[Dict[str, Any]]) -> None:
    data = load_data()
    data.setdefault("results", [])
    data["results"].append({
        "user_id": user_id,
        "full_name": full_name,
        "username": username or "",
        "score": score,
        "total": total,
        "details": details
    })
    save_data(data)

def get_results() -> List[Dict[str, Any]]:
    data = load_data()
    return data.get("results", [])

def clear_results() -> None:
    data = load_data()
    data["results"] = []
    save_data(data)
