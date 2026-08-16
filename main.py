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
          "timestamp": "10:00:08",
          "username": "Bob",
          "event_type": "login_failed",
          "source_ip": "192.168.1.30",
    },

    {
           "timestamp": "10:00:08",
           "username": "Charlie",
           "event_type": "login_failed",
           "source_ip": "192.168.1.50",
    }
]

failed_attempts = {}

for event in events:
    if event["event_type"] == "login_failed":

        username = event["username"]

        if username not in failed_attempts:
           failed_attempts[username].append(event["timestamp"]) = 1

        else :
           failed_attempts[username].append(event["timestamp"]) += 1
        
print(failed_attempts)