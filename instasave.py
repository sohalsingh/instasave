import instaloader
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

def download_post(loader, post, profile_name):
    try:
        loader.download_post(post, target=profile_name)
        print(f"Downloaded post {post.shortcode}.")
    except Exception as e:
        print(f"Failed to download post {post.shortcode}: {e}")

def download_instagram_posts(profile_name, wait_time=10, max_workers=4, post_filter=None):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    # Load the profile
    try:
        profile = instaloader.Profile.from_username(loader.context, profile_name)
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile {profile_name} does not exist.")
        return
    except instaloader.exceptions.InstaloaderException as e:
        print(f"An error occurred: {e}")
        return

    # Get posts
    posts = profile.get_posts()

    # Create a thread pool for downloading posts
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_post = {executor.submit(download_post, loader, post, profile_name): post for post in posts if not post_filter or post_filter(post)}
        for future in as_completed(future_to_post):
            post = future_to_post[future]
            try:
                future.result()
            except Exception as exc:
                print(f'Post {post.shortcode} generated an exception: {exc}')

            # Wait to avoid getting banned
            delay = wait_time + random.uniform(0, wait_time)
            print(f"Waiting for {delay:.2f} seconds before next download...")
            time.sleep(delay)

    print(f"All posts from {profile_name} have been downloaded.")

def video_post_filter(post):
    return post.is_video

if __name__ == "__main__":
    profile_name = input("Enter the Instagram profile name: ")
    wait_time = float(input("Enter the wait time in seconds between downloads (recommended: 10-30 seconds): "))
    max_workers = int(input("Enter the number of parallel downloads (recommended: 4): "))
    filter_choice = input("Do you want to download only video posts? (yes/no): ").strip().lower()
    post_filter = video_post_filter if filter_choice == 'yes' else None

    download_instagram_posts(profile_name, wait_time, max_workers, post_filter)
