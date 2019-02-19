import movie_svc
import requests.exceptions


def main():
    print_header()
    search_event_loop()


def print_header():
    pass


def search_event_loop():
    search = "ONCE_THROUGH_LOOP"
    while search != "x":
        try:
            search = input("Movie search text (x to exit): ")
            if search != "x":
                results = movie_svc.find_movies(search)
                print("Found {} result.".format(len(results)))
                for r in results:
                    print("{} -- {}".format(r.year, r.title))
                print()
        except  requests.exceptions as ce:
            print("Network Error due to \n{}.....!".format(type(ce)))
        except  Exception as x:
            print("Error due to {}.....!".format(x))

    print("Exiting .... ... ... .")


if __name__ == "__main__":
    main()
