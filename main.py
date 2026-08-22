events = [ 
   { 
        "timestamp": "10:00:01",
        "username": "Alice",
        "event_type": "login_failed",
        "source_ip": "192.168.1.21",
   },

   {
        "timestamp": "10:00:05",
        "username": "Alice",
        "event_type": "login_failed",
        "source_ip": "192.168.1.21",
   },
  
   {
       "timestamp": "10:00:10",
       "username": "Alice",
       "event_type": "login_failed",
       "source_ip": "192.168.1.21",
   },

   {
       "timestamp": "10:00:15",
       "username": "Alice",
       "event_type": "login_failed",
       "source_ip": "192.168.1.21",
   },

   {
       "timestamp": "10:00:20",
       "username": "Alice",
       "event_type": "login_failed",
       "source_ip": "192.168.1.21",
   },

   {
       "timestamp": "10:00:08",
       "username": "Bob",
       "event_type": "login_failed",
       "source_ip": "192.168.1.30",
   },

   {
          "timestamp": "10:00:12",
          "username": "Bob",
          "event_type": "login_failed",
          "source_ip": "192.168.1.30",
    },

    {
           "timestamp": "10:00:18",
           "username": "Charlie",
           "event_type": "login_failed",
           "source_ip": "192.168.1.50",
    }
]

from datetime import datetime, timedelta

failed_attempts = {}
source_ips = {}

for event in events: 
    if event["event_type"] == "login_failed":

        username = event["username"]
        source_ips[username] = event["source_ip"]
 

        if username not in failed_attempts:
            failed_attempts[username] = []
            failed_attempts[username].append(event["timestamp"])
        else:
            failed_attempts[username].append(event["timestamp"])

for username, timestamp in failed_attempts.items():

 failed_count = len(timestamp)

 first_time = datetime.strptime(timestamp[0], "%H:%M:%S")
 last_time = datetime.strptime(timestamp[-1], "%H:%M:%S")

 difference = last_time - first_time 
 limit = timedelta(minutes=2)

 if failed_count >= 5 and difference <= limit:
    print("Brute-force attack detected:", username)
    print("Source IP:", source_ips[username])

 print(username, failed_count, difference) 