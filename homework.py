import requests



"""
-- JSON format for Bored API --
{
  "activity": "Learn to play a musical instrument",
  "type": "music",
  "participants": 1,
  "price": 0.1,
  "link": "",
  "key": "4526284",
  "accessibility": "Few to no challenges"
}
"""


def get_random_activity():
    """
    Get a completely random activity suggestion
    
    API: https://bored-api.appbrewery.com/random
    """
    # YOUR CODE HERE
    # 1. Make a GET request to the API
    # 2. Parse the JSON response  
    # 3. Print the activity and type nicely
    # 4. Handle any errors
    url = "https://bored-api.appbrewery.com/random"

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print("Random Activity Suggestion:")
        print(f"Activity: {data['activity']}")
        print(F"Type: {data['type']}")
        print(f"Participants: {data['participants']}")
        print("Ready to try it?")
    else:
        print("Failed to fetch posts.")

def get_activity_by_type():
    """
    Let user choose an activity type and get a suggestion
    
    API: https://bored-api.appbrewery.com/filter?type={type}
    
    Types: education, recreational, social, diy, charity, cooking, relaxation, music, busywork
    """
    # YOUR CODE HERE
    # 1. Show the user available types
    # 2. Get their choice
    # 3. Make API request with type parameter
    # 4. Display the result
    
    
    activity_type = input("Select a type! (education, recreational, social, diy, charity, cooking, relaxation, music, busywork): ")
    
    activities = ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"]

    if activity_type in activities:
        url = f"https://bored-api.appbrewery.com/filter?type={activity_type}"
        
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            for i in range(len(data)):
                print("Random Activity Suggestion:")
                print(f"Activity: {data[i]['activity']}")
                print(F"Type: {data[i]['type']}")
                print(f"Participants: {data[i]['participants']}")
                print("Ready to try it?")
        else:
            print("Failed to fetch data")
    else:
        print("Activity type must be in listed options.")

    

def get_activity_by_participants():
    """
    Get activity suggestions based on number of participants
    
    API: https://bored-api.appbrewery.com/filter?participants={number}
    """
    # YOUR CODE HERE
    # 1. Ask user how many participants
    # 2. Make API request with participants parameter
    # 3. Display the activity suggestion
    number = input("Choose the number of participants for your activity: ")

    url = f"https://bored-api.appbrewery.com/filter?participants={number}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Random Activity Suggestion:")
        for i in range(len(data)):
            print(f"Activity: {data[i]['activity']}")
            print(F"Type: {data[i]['type']}")
            print(f"Participants: {data[i]['participants']}")
            print("Ready to try it?")
    else:
        print("Failed to fetch data.")


def show_menu():
    """Display the main menu"""
    print("\nBored Activity Finder")
    print("=" * 21)
    print("1. Get a random activity")
    print("2. Get activity by type")
    print("3. Get activity by participants")
    print("4. Exit")

def main():
    """Main function with menu loop"""
    print("Welcome to the Bored Activity Finder!")
    
    while True:
        show_menu()
        
        try:
            choice = input("\nChoose an option (1-4): ")
            
            if choice == '1':
                get_random_activity()
            elif choice == '2':
                get_activity_by_type()
            elif choice == '3':
                get_activity_by_participants()
            elif choice == '4':
                print("Thanks for using Bored Activity Finder!")
                break
            else:
                print("Invalid choice! Please choose 1-4.")
                
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break

if __name__ == "__main__":
    main()