## A tool to toggle between two different music services to compare sound differences.
##### Compares services by repeatedly playing the same section of the same song and toggling the service each time. Originally built to compare between YouTube music and Spotify but should support other services.
It was built quickly and so relies on exact pixel coordinates of the apps.
### Setup
- Have both services open, set to the same song, and visible on your screen.
- Determine the pixels coordinates of both services seek bars(x axis start and end + y axis), play buttons, and focus points (a blank section of the window that safely allows the windows to gain focus without interfering)
- Tun the player_swapper function with the correct arguments

