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
       "timestamp": "10:00:25",
       "username": "Alice",
       "event_type": "login_success",
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

from datetime import datetime

failed_attempts = {}

for event in events: 
    if event["event_type"] == "login_failed":

        username = event["username"]

        if username not in failed_attempts:
            failed_attempts[username] = []
            failed_attempts[username].append(event["timestamp"])
        else:
            failed_attempts[username].append(event["timestamp"])

for username, timestamp in failed_attempts.items():

 first_time = datetime.strptime(timestamp[0], "%H:%M:%S")
 last_time = datetime.strptime(timestamp[-1], "%H:%M:%S")

 difference = last_time - first_time

 print(username, difference)