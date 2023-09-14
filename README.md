# spam-r3q

┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼██┼
┼┼┼┼███┼┼┼┼██┼┼
┼┼███┼┼█┼███┼┼┼
┼┼█┼┼┼┼███┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼


## Overview:

This Python script is for those who scoff at manual requests. It's designed for the bold and impatient, who thrive on efficiency.

## Features

- **Silent Requests**: This script sprints through requests using the Tor network, leaving no trace behind.
- **Error Tolerance**: It laughs at errors and handles them with the finesse of a pro.
- **Customizable Input Files**: Just dump your data in text files, and watch the magic unfold.
- **Request Records**: Keep a tight record of all your victorious requests.

## Usage

### Tor Setup (No compromises)

1. **Install and customize Tor**: 
```bash
   sudo apt install tor
   sudo systemctl restart tor
   sudo nano /etc/proxychains4.conf (add this line socks5 127.0.0.1 9050)
```

2. **Launch script with Tor**: Ensure Tor is up and running. It's your ticket to the fast lane.

  proxychains python3 spam-r3q.py
  
3. **Customize URLs**:
   - Replace the URLs in the script with your desired request destinations.

4. **Input Files**:
   - Populate these text files with one entry per line:
     - `ur_data`: Usernames
     - `ur_data`: Passwords
     - `ur_data`: Emails
     - `ur_Data`: GSM numbers
     - `ur_data`: First names
     - `ur_data`: Surnames

5. **Launch the Script**:
   - Fire it up in your Python environment. It's time to conquer.

6. **Monitor Output**:
   - All successful requests will be logged in `successful_req.txt`.

## Caveat

- **Tor Dependency**: Tor is not an option, it's a necessity. Ensure it's up and accessible.

## Disclaimer

This script is purely for educational and testing purposes. Any unauthorized or illicit use is strictly forbidden.

---

*Note: This script knows no mercy. Use it wisely.*
