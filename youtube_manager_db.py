import sqlite3

db_name = 'youtube_videos.db'

con = sqlite3.connect(db_name)

cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
    )
 ''')


def list_videos():
    cursor.execute("SELECT * FROM videos")
    print("\n")
    print("*" * 70)
    print("\n")
    for row in cursor.fetchall():
        print(f"{row[0]}. Video name: {row[1]} Duration: {row[2]}")
    print("\n")
    print("*" * 70)
    print("\n")

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()

def update_video(id, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, id))
    con.commit()

def delete_video(id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (id,))
    con.commit()     

def main():
    while True:
        print("Youtube Manager app with DB")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            video_name = input("Enter the video name: ")
            video_time = input("Enter the video time: ")
            add_video(video_name, video_time)
        elif choice == '3':
            video_id = input("Enter video ID to update: ")
            video_name = input("Enter the video name: ")
            video_time = input("Enter the video time: ")
            update_video(video_id, video_name, video_time)
        elif choice == '4':
            video_id = input("Enter the video ID to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice, enter a valid choice")    
        
    con.close()
if __name__ == "__main__":
    main()