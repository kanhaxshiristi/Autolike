import time
import requests

# Yahan apni aur apne dosto ki UIDs add kar dein
UID_BANK = [
    "1229542378",
    "2076877917",
    "1856711429",
    "1837749051",
    # Aur bhi UIDs yahan add kar sakte hain comma laga kar
]

SERVER_NAME = "ind"

def send_likes():
    print(f"Total UIDs in bank: {len(UID_BANK)}. Like sending shuru ho raha hai...")
    
    for idx, uid in enumerate(UID_BANK, 1):
        api_url = f"https://like-with-level-q64s5pt53-kanhas-projects-60c1d631.vercel.app/like?server_name={SERVER_NAME}&uid={uid}"
        
        try:
            response = requests.get(api_url, timeout=15)
            if response.status_code == 200:
                print(f"[{idx}/{len(UID_BANK)}] [SUCCESS] Like sent to UID: {uid}")
            else:
                print(f"[{idx}/{len(UID_BANK)}] [ERROR] UID {uid} failed with status: {response.status_code}")
        except Exception as e:
            print(f"[{idx}/{len(UID_BANK)}] [EXCEPT] Error for UID {uid}: {e}")
            
        time.sleep(3)
        
    print("\n[SUCCESS] Sabhi UIDs ko likes bhej diye gaye hain!")

if __name__ == "__main__":
    send_likes()
