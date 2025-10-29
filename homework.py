import requests

def show_menu():
    """Display the main menu"""
    print("\nBored Activity Finder")
    print("=" * 21)
    print("1. Get a random activity")
    print("2. Get activity by type")
    print("3. Get activity by participants")
    print("4. Save my favorite activities")
    print("5. View my saved activities")
    print("6. Exit")

def main():
    """Main function with menu loop"""
    print("Welcome to the Bored Activity Finder!")
    
    while True:
        show_menu()
        
        try:
            choice = input("\nChoose an option (1-7): ")
            
            if choice == '1':
                get_random_activity()
            elif choice == '2':
                get_activity_by_type()
            elif choice == '3':
                get_activity_by_participants()
            elif choice == '4':
                get_quick_activity()
            elif choice == '5':
                save_favorite_activity()
            elif choice == '6':
                view_saved_activities()
            elif choice == '7':
                print("Thanks for using Bored Activity Finder!")
                break
            else:
                print("Invalid choice! Please choose 1-7.")
                
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break

if __name__ == "__main__":
    main()

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
    pass

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
    pass

def get_activity_by_participants():
    """
    Get activity suggestions based on number of participants
    
    API: https://bored-api.appbrewery.com/filter?participants={number}
    """
    # YOUR CODE HERE
    # 1. Ask user how many participants
    # 2. Make API request with participants parameter
    # 3. Display the activity suggestion
    pass

def save_favorite_activity():
    """
    Get an activity and save it to a text file
    """
    # YOUR CODE HERE
    # 1. after getting an activity from one of the other functions
    # 2. Ask user if they want to save it
    # 3. If yes, append to 'favorite_activities' list
         # 4. Print "Activity Saved"
    pass

def view_saved_activities():
    """
    Read and display saved activities from file
    """
    # YOUR CODE HERE
    # Loop through the list of saved activities and display each one
    pass