import rpc
import time
from time import mktime

print("Starting...")
client_id = '800033582214283275'  # Your application's client ID as a string. (This isn't a real client ID)
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)  # Send the client ID to the rpc module
print("RPC connection successful.")

time.sleep(5)
start_time = mktime(time.localtime())
while True:
    activity = {
            "state": "SeKC BUM's Music",  # anything you like
            "details": "Listening to falfoul's music...",  # anything you like
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": "Adobe",  # anything you like
                "small_image": "adobe",  # must match the image key
                "large_text": "xfalfoul",  # anything you like
                "large_image": "final"  # must match the image key
            }
        }
    rpc_obj.set_activity(activity)
    time.sleep(900)
