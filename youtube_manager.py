import json

file_name = 'youtube.txt'

def load_data():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Helper methods  
def save_data_helper(videos):
    with open(file_name, 'w') as file:
        json.dump(videos, file)



# Controllers
def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    print("\n")
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']}, Duration: {video['time']}")
    print("\n")
    print("*" * 70)
    print("\n")
    
def add_video(videos):
    video_name = input("Enter video name: ")
    video_time = input("Enter video time: ")

    videos.append({'name': video_name, 'time': video_time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        new_video_name = input("Enter the new video name: ")
        new_video_time = input("Enter the new video time: ")
        videos[index-1] = {'name': new_video_name, 'time': new_video_time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))
    if 1 <= index <= len(videos):
        del videos[index-1] 
        save_data_helper(videos)
    else: 
        print("Invalid video index selected") 

# Program start from here
def main():
    videos = load_data()

    while True:
        print('\n Youtube Manager | choose an option')
        print('1. List all youtube videos')
        print('2. Add a youtube video')
        print('3. Update a youtube video details')
        print('4. Delete a youtube video')
        print('5. Exit the app')
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()