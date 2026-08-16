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
   }
]

failed_attempts = {} 

for event in events:
    if event["username"] == "Alice":
        failed_attempts += 1

print("Failed attempts:", failed_attempts)