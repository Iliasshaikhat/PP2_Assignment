import psycopg2

DB_CONFIG = {
    "dbname": "snake_db",
    "user": "postgres",
    "password": "1234",  
    "host": "localhost",
    "port": "5432",
    "client_encoding": "utf8"  # Forces correct encoding to prevent Unicode errors
}

def get_connection():
    # try to connect to postgres, and print some help if it fails
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except psycopg2.Error as e:
        print("\n--- DATABASE CONNECTION ERROR ---")
        print(f"Details: {e}")
        print("1. Check if PostgreSQL service is running.")
        print("2. Verify 'password' in DB_CONFIG.")
        print("3. Ensure database 'postgres' exists.")
        print("---------------------------------\n")
        raise e 

def setup_database():
    # create the tables for players and scores if this is the first time running
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS players (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL
            );
            CREATE TABLE IF NOT EXISTS game_sessions (
                id SERIAL PRIMARY KEY,
                player_id INTEGER REFERENCES players(id),
                score INTEGER NOT NULL,
                level_reached INTEGER NOT NULL,
                played_at TIMESTAMP DEFAULT NOW()
            );
        """)
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Database Setup Error: {e}")

def get_or_create_player(username):
    # add the player to the db if they don't exist, and return their id
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO players (username) VALUES (%s)
        ON CONFLICT (username) DO NOTHING;
    """, (username,))
    cur.execute("SELECT id FROM players WHERE username = %s;", (username,))
    player_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return player_id

def save_score(player_id, score, level):
    # save the player's score and what level they made it to
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO game_sessions (player_id, score, level_reached)
        VALUES (%s, %s, %s);
    """, (player_id, score, level))
    conn.commit()
    cur.close()
    conn.close()

def get_top_10():
    # grab the best 10 scores from all players to show on the leaderboard
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT p.username, s.score, s.level_reached, s.played_at::date 
            FROM game_sessions s
            JOIN players p ON s.player_id = p.id
            ORDER BY s.score DESC
            LIMIT 10;
        """)
        top_10 = cur.fetchall()
        cur.close()
        conn.close()
        return top_10
    except:
        return []

def get_personal_best(player_id):
    # find the highest score this specific player has ever gotten
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT MAX(score) FROM game_sessions WHERE player_id = %s;", (player_id,))
    best = cur.fetchone()[0]
    cur.close()
    conn.close()
    return best if best else 0