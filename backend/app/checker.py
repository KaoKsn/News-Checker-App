import argparse
from datetime import datetime
import json
import re
import requests
import time

'''
    Class URL

    Global variables:
        1. s_time - Stores the start time of checking.
        2. check_time - Stores the ISO time of checking.

    Instance variables:
        1. link - Stores the link that was passed.
        2. is_true - A boolean value to represent the truth value of a claim raised in the url.
            default - False
        3. truth_percentage - A floating point value to represent the truth value of a claim raised in the url out of 100.
            default - 0.0

    Setter-Getter pair:
        1. link() - Ensure the integrity of the news link from the user.
        2. is_true() - Ensure that the default value of is_true is False.
        3. truth_percentage() - Ensure the value of truth_percentage lies between 0 to 100(inclusive).

    Methods:
        1. __init__(self, link) - Constructor of the URL class. Initializes the value of link, is_true and truth_percentage.
        2. __str__(self, link) - Prints the truth value both in terms of a boolean and a floating point value.
        3. news_json() - Read the contents present in the link into a JSON format.
'''

class URL:
    supported_sites = {
                        "redd": "Reddit",
                        "reddit": "Reddit",
                        "x": "X"
                      }

    supported_formats = {
                   "http(s)://redd.it/{post_id}",
                   "https(s)://www.reddit.com/r/{subreddit}/{post_id}/{post_title}/",
                   "http(s)://x.com/{username}/status/{post_id}",
                   "http(s)://x.com/i/web/status/{post_id}"
               }

    def __init__(self, link):
        self.link = link
        self.is_true = False
        self.truth_percentage = 0.0
        self.check_time = datetime.now()
        self.s_time = time.time()

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, link):
        """
            Supported link formats:
                1. http(s)://redd.it/{post_id}
                2. https(s)://www.reddit.com/r/{subreddit}/{post_id}/{post_title}/
                3. http(s)://x.com/{username}/status/{post_id}
                4. http(s)://x.com/i/web/status/{post_id}

            Link validation
            1. Ensure that a non-empty string is read as the input.
            2. Ensure that the link comes from either Reddit or X.

            Exceptions:
                1. ValueError:
                    a. Empty input as link input.
                    b. If link from any other site other than Reddit or X.
        """

        # Ensure a non-empty string is read as a link.
        if not link:
            raise ValueError("Empty string. No link found!")

        if link_elements := re.search(r'^https?://(?:www\.)?(?:(redd)\.it/\w+|(reddit)\.com/r/(?:\w+/?){3}$|(x)\.com/(?:\w+/status/\w+|i/web/status/\w+))/?$', link):

            for element in link_elements.groups():
                # Get the site name, avoiding None. Eg: (None, None, x).
                if element and element in URL.supported_sites.keys():
                    self.site = URL.supported_sites[element]
                    # Set link name to the link input.
                    self._link = link

            # If no valid site name found, raise a ValueError.
            if not self.site:
                raise ValueError("Invalid Site. Currently supported sites: Reddit, X")


        else:
            print("Invalid Link Format!")
            raise ValueError("Invalid Link Format!")


    @property
    def is_true(self):
        return self._is_true

    @is_true.setter
    def is_true(self, value):
        if not isinstance(value, bool):
            raise TypeError("The value for is_true must be a boolean (True or False).")
        self._is_true = value

    @property
    def truth_percentage(self):
        return self._truth_percentage

    @truth_percentage.setter
    def truth_percentage(self, truth_percentage):
        # Ensure truth_percentage lies between 0 and 100.
        if not (0 <= truth_percentage <= 100):
            raise ValueError("Truth percentage can only lie in-between 0 to 100(inclusive)!")

        self._truth_percentage = truth_percentage


    # Print the status of check.
    def __str__(self):
        return f"\nCheck at: {self.check_time}\nThe claim at '{self._link}' from {self.site}, is most likely {self._is_true}.\nProbability of truth: {self._truth_percentage}.\nTime spent on analysis: {time.time()-self.s_time:.4f} s"


    # Use exception handling after reading the API.
    def news_json(self):
        # A dummy request.
        response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=weezer")

        # Ensure a valid response was received.
        if response.status_code == 200:
            response = response.json()
            print(json.dumps(response, indent = 4))

        else:
              print("Error Status during API request:", response.status_code)

    # A verbose verdict regarding the claim at the given link.
    def verbose_verdict(self):
        print("\n\n===========   Verdict   =============")
        print(f"Check requested at: {self.check_time}")
        print(f"Link: {self._link}")
        print(f"Site Detected: {self.site}")
        print(f"Truth Value: {self._is_true}")
        print(f"Probability of being true: {self._truth_percentage}")
        print(f"Time spent on analysis: {time.time() - self.s_time:.4f} s")

        # TODO: Add sources.

        print()


def main():
    # Command line arguments.
    parser = argparse.ArgumentParser(prog = "checker.py", description = "A python program to probabilistically determine the truth value of a claim raised in a link on platforms like Reddit/X.", epilog = "Source @ github.com/maurya-doshi/News-Checker-App\nContributors:\n1.KaoKsn\n2.Maurya Doshi")

    parser.add_argument("link") # Positional argument: link to the claim.

    # Flags
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-s", "--silent", action="store_true")
    parser.add_argument("-V", "--version", action="store_true")

    # Parsing the command line arguments.
    args = parser.parse_args()

    # Create a news_engine object.
    try:
        news_engine = URL(args.link)

    except ValueError:
        print("\nUsage:")
        for formats in URL.supported_formats:
            print(f"python checker.py {formats} [-s] [-v] [-V]")
        return 1

    else:
        # Read the contents of the link in JSON format.
        news_engine.news_json()

        # If a silent output requested, just give enough information.
        if args.silent:
            print(news_engine)

        # Else, provide verbose information.
        else:
            news_engine.verbose_verdict()

        return 0


if __name__ == "__main__":
    main()
