# Instagram Post Downloader

This Python script allows you to download all posts from an Instagram profile efficiently. It includes features to handle rate limits, download posts in parallel, filter posts (e.g., only videos), and resume interrupted downloads. The script uses the `instaloader` library.

## Features

- **Parallel Downloads**: Utilizes multiple threads to download posts concurrently, speeding up the process.
- **Rate Limiting**: Adds random delays between downloads to avoid getting banned by Instagram.
- **Post Filtering**: Option to download only specific types of posts (e.g., videos).
- **Resuming Downloads**: Supports resuming downloads in case of interruptions.
- **Enhanced Error Handling**: Provides detailed error messages and logs exceptions.

## Prerequisites

- Python 3.6+
- `instaloader` library

## Installation

1. Clone the repository or download the script.
2. Install the `instaloader` library:

    ```bash
    pip install instaloader
    ```

## Usage

1. Run the script:

    ```bash
    python download_instagram_posts.py
    ```

2. Follow the prompts:
    - Enter the Instagram profile name.
    - Enter the wait time in seconds between downloads (recommended: 10-30 seconds).
    - Enter the number of parallel downloads (recommended: 4).
    - Specify if you want to download only video posts.

## Script Explanation

### Script: `download_instagram_posts.py`


### Parameters

- **profile_name**: The Instagram profile from which to download posts.
- **wait_time**: Base wait time in seconds between downloads to avoid rate limiting.
- **max_workers**: Number of parallel downloads (threads).
- **post_filter**: Function to filter posts to download (e.g., only videos).

### Functions

- **download_post(loader, post, profile_name)**: Downloads a single post.
- **download_instagram_posts(profile_name, wait_time, max_workers, post_filter)**: Main function to download posts from the profile.
- **video_post_filter(post)**: Filter function to download only video posts.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

- Ensure compliance with Instagram's terms of service and any applicable laws.
- The script introduces delays and random waits to mimic human behavior and avoid getting banned, but there are no guarantees against Instagram's rate limiting policies.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.
