from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# --- DATABASE CONNECTION ---
def get_db_connection():
    return psycopg2.connect(
        host="localhost",      # endre hvis ekstern server
        database="eksamen",
        user="joachim1",
        password="DatabaseJoachim",
        port=5432
    )

@app.get("/test")
def test():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        result = cur.fetchone()
        cur.close()
        conn.close()
        return {"status": "OK", "db": result[0]}
    except Exception as e:
        return {"status": "ERROR", "message": str(e)}

# --- START SERVER ---
if __name__ == "__main__":
    app.run(debug=True)
