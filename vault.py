# --- Secure Data Vault (Engineering Edition) ---
# Logic: Caesar Cipher Encryption for access control
# Structure: Using pure Python lists and functions to manage data logic

def encrypt_input(text):
    """Simple Caesar Cipher: Shifting characters by 3"""
    encrypted = ""
    for char in text:
        encrypted += chr(ord(char) + 3)
    return encrypted

def show_menu():
    print("\n" + "="*30)
    print("      DATA VAULT MENU")
    print("="*30)
    print("1. ➕ Add New Secret")
    print("2. 📜 View All Secrets")
    print("3. 🗑️ Clear All Data")
    print("4. 🚪 Exit System")
    return input("\nSelect an option (1-4): ")

def main():
    # Encrypted version of "cs50" is "fv83"
    MASTER_KEY_ENCRYPTED = "fv83"
    vault_data = []
    
    print("--- System Initialized: Secure Logic Active ---")
    
    authenticated = False
    attempts = 3
    
    # Authentication Phase
    while attempts > 0:
        user_pass = input(f"🔒 Enter Master Password ({attempts} attempts left): ")
        if encrypt_input(user_pass) == MASTER_KEY_ENCRYPTED:
            authenticated = True
            print("\n✅ Access Granted. Welcome back, Engineer.")
            break
        else:
            attempts -= 1
            print("❌ Access Denied: Invalid Credentials.")

    # Application Phase
    if authenticated:
        while True:
            choice = show_menu()
            
            if choice == "1":
                secret = input("Enter data to secure: ")
                if secret.strip(): # Check if input is not empty
                    vault_data.append(secret)
                    print("✔️ Data stored successfully.")
                else:
                    print("⚠️ Cannot store empty data.")
                    
            elif choice == "2":
                print("\n--- Current Secured Records ---")
                if not vault_data:
                    print("[The vault is empty]")
                else:
                    # Using enumerate for better indexing (from CS50 concepts)
                    for i, record in enumerate(vault_data, 1):
                        print(f"Record #{i}: {record}")
                        
            elif choice == "3":
                confirm = input("⚠️ Are you sure you want to delete ALL data? (y/n): ")
                if confirm.lower() == 'y':
                    vault_data.clear()
                    print("🗑️ Vault wiped clean.")
                    
            elif choice == "4":
                print("Logging out... System secured. Goodbye!")
                break
            else:
                print(f"⚠️ Error: '{choice}' is not a valid command.")
    else:
        print("\n🚫 SECURITY ALERT: Multiple failed attempts. System Locked.")

if __name__ == "__main__":
    main()