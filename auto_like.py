import time
import requests

# Yahan apne aur apne dosto ke UIDs add kar dein
UID_BANK = [
    "1229542378",
    "2076877917",
    "1856711429",
    "1837749051",
    "1773695118",
    "11633576702",
    "12642561964",
    "611802148"
    # Aur bhi UIDs yahan add kar sakte hain comma laga kar
]

SERVER_NAME = "ind"

def send_likes():
    print(f"Total UIDs in bank: {len(UID_BANK)}. Like sending shuru ho raha hai...\n")
    
    for idx, uid in enumerate(UID_BANK, 1):
        # Nayi API URL jisme server aur uid pass ho rahe hain
        api_url = f"https://like-with-level.vercel.app/like?server_name={SERVER_NAME}&uid={uid}"
        
        try:
            response = requests.get(api_url, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                # API ka proper response print karega
                print(f"[{idx}/{len(UID_BANK)}] [SUCCESS] UID: {uid}")
                print(f"   -> Nickname: {data.get('PlayerNickname')}")
                print(f"   -> Level: {data.get('Level')}")
                print(f"   -> Likes Before: {data.get('LikesbeforeCommand')}")
                print(f"   -> Likes After: {data.get('LikesafterCommand')}")
                print(f"   -> Status: {data.get('status')}\n")
            else:
                print(f"[{idx}/{len(UID_BANK)}] [ERROR] UID {uid} failed with HTTP status: {response.status_code}\n")
                
        except requests.exceptions.Timeout:
            print(f"[{idx}/{len(UID_BANK)}] [TIMEOUT] API request timed out for UID: {uid}\n")
        except Exception as e:
            print(f"[{idx}/{len(UID_BANK)}] [EXCEPT] Error for UID {uid}: {e}\n")
            
        # Server par load na pade isliye har request ke beech 5 seconds ka gap
        time.sleep(5)
        
    print("[SUCCESS] Sabhi UIDs ka process complete ho gaya hai!")

if __name__ == "__main__":
    send_likes()
