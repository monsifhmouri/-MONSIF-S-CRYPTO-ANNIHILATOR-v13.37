import os  
import sys  
import base64  
import itertools  
import multiprocessing  
from Crypto.Cipher import AES, DES3, ARC4  
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes  
from tqdm import tqdm  

# --- MONSIF'S TOUCH ---  
AUTHOR = "/* CRACKED BY MONSIF */"  
TARGET_FILE = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'annihilated_data.json')  
OUTPUT_FILE = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'monsif_loot.txt')  

# GPU-accelerated charset (using CPU parallelism)  
CHARSET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'  
MAX_KEY_LEN = 32  # For AES-256  

def generate_key_space():  
    # AI-powered pattern detection (simulated)  
    return [  
        'WO39vdwwmkeYpB5KOSmfu28mW7e1sIQV9BoBDRs22wI=',  
        'monsif',  
        'certinia',  
        'admin123',  
        'secureKey',  
        'vulnerable'  
    ] + [''.join(p) for p in itertools.product(CHARSET, repeat=3)]  

def try_aes(key):  
    try:  
        cipher = AES.new(key.ljust(32, b'\0')[:32], AES.MODE_ECB)  
        decrypted = cipher.decrypt(encrypted_data)  
        if b'json' in decrypted:  
            return decrypted  
    except:  
        pass  
    return None  

def try_des(key):  
    try:  
        cipher = DES3.new(key.ljust(24, b'\0')[:24], DES3.MODE_ECB)  
        decrypted = cipher.decrypt(encrypted_data)  
        if b'json' in decrypted:  
            return decrypted  
    except:  
        pass  
    return None  

def try_rc4(key):  
    try:  
        cipher = ARC4.new(key)  
        return cipher.decrypt(encrypted_data)  
    except:  
        return None  

def brute_force_parallel():  
    pool = multiprocessing.Pool()  
    keys = generate_key_space()  
    
    print(f"[!] Launching {multiprocessing.cpu_count()} core nuclear assault...")  
    for result in tqdm(pool.imap_unordered(test_key, keys), total=len(keys)):  
        if result:  
            pool.terminate()  
            return result  
    return None  

def test_key(key):  
    key = key.encode()  
    for algo in [try_aes, try_des, try_rc4]:  
        result = algo(key)  
        if result and b'vulns' in result:  
            return result.decode(errors='ignore')  
    return None  

def main():  
    global encrypted_data  
    with open(TARGET_FILE, 'rb') as f:  
        encrypted_data = f.read()  
    
    print(f"""  
    ███╗   ███╗ ██████╗ ███╗   ██╗███████╗██╗███████╗  
    ████╗ ████║██╔═══██╗████╗  ██║██╔════╝██║██╔════╝  
    ██╔████╔██║██║   ██║██╔██╗ ██║█████╗  ██║███████╗  
    ██║╚██╔╝██║██║   ██║██║╚██╗██║██╔══╝  ██║╚════██║  
    ██║ ╚═╝ ██║╚██████╔╝██║ ╚████║███████╗██║███████║  
    ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝╚══════╝  
    {AUTHOR}  
    """)  
    
    result = brute_force_parallel()  
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8', errors='replace') as f:  
        f.write(result if result else "/* FAILURE: Add more GPU power */")  
    
    print(f"[!] Decryption war concluded → {OUTPUT_FILE}")  

if __name__ == "__main__":  
    multiprocessing.freeze_support()  
    main()  