import smtplib
import time
import sys
import json

# Function to send email alert
def send_email_alert(sender_email, sender_password, recipient_email):
    try:
        # Setting up the server and email content
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, sender_password)
        subject = "Emergency Alert"
        body = "This is an emergency alert from the Women's Safety App."
        message = f'Subject: {subject}\n\n{body}'
        
        server.sendmail(sender_email, recipient_email, message)
        server.quit()
        print("Emergency email sent!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Function to display safety tips
def display_safety_tips():
    print("\n--- Safety Tips ---")
    print("1. Trust your instincts.")
    print("2. Stay aware of your surroundings.")
    print("3. Keep your phone fully charged.")
    print("4. Avoid risky areas and paths.")
    print("5. Contact emergency services when necessary.")
    print("-------------------\n")

# Function to get and save user's emergency contact
def get_and_save_emergency_contact():
    name = input("Enter your emergency contact's name: ")
    phone = input("Enter the phone number of your emergency contact: ")
    email = input("Enter the email address of your emergency contact: ")

    # Saving the emergency contact information to a JSON file
    contact_info = {
        'name': name,
        'phone': phone,
        'email': email
    }

    with open("emergency_contact.json", "w") as file:
        json.dump(contact_info, file)
    
    print(f"Emergency contact {name} saved with phone number: {phone} and email: {email}")

# Function to load stored emergency contact information
def load_emergency_contact():
    try:
        with open("emergency_contact.json", "r") as file:
            contact_info = json.load(file)
        return contact_info
    except FileNotFoundError:
        print("No emergency contact saved. Please save the contact first.")
        return None

# Main menu of the app
def main_menu():
    print("\nWelcome to the Women's Safety App!")
    print("1. Send Emergency Alert (Email only)")
    print("2. View Safety Tips")
    print("3. Set Emergency Contact")
    print("4. Exit")
    
    try:
        choice = input("Select an option (1-4): ")
        if choice == "1":
            # Send emergency alert via email
            contact_info = load_emergency_contact()

            if contact_info:
                sender_email = input("Enter your email address: ")
                sender_password = input("Enter your email password: ")
                recipient_email = contact_info['email']
                send_email_alert(sender_email, sender_password, recipient_email)
            else:
                print("You need to set an emergency contact first.")
        
        elif choice == "2":
            # Display safety tips
            display_safety_tips()
        
        elif choice == "3":
            # Set emergency contact
            get_and_save_emergency_contact()
        
        elif choice == "4":
            print("Exiting the app. Stay safe!")
            sys.exit()
        
        else:
            print("Invalid option! Please choose a valid option (1-4).")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the app
if __name__ == "__main__":
    while True:
        main_menu()
        time.sleep(1)  # To make sure the user can see the result before the next prompt
