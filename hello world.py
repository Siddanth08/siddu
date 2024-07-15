import requests

def search_movie(title, year=None, plot='short', api_key='your_omdb_api_key_here'):
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}&plot={plot}"
    if year:
        url += f"&y={year}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx/5xx status codes
        movie_data = response.json()
        
        if movie_data['Response'] == 'True':
            return movie_data
        else:
            print(f"Error: {movie_data['Error']}")
            return None
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def print_movie_details(movie_data):
    print(f"Title: {movie_data['Title']}")
    print(f"Year: {movie_data['Year']}")
    print(f"IMDb Rating: {movie_data['imdbRating']}")
    print(f"Genre: {movie_data['Genre']}")
    print(f"Plot: {movie_data['Plot']}")
    print(f"Actors: {movie_data['Actors']}")
    print(f"Director: {movie_data['Director']}")
    print(f"Writer: {movie_data['Writer']}")
    print(f"Awards: {movie_data['Awards']}")

def main():
    print("Welcome to the Movie Database Search!")
    print("====================================")
    title = input("Enter the title of the movie: ").strip()
    year = input("Enter the year of release (optional): ").strip()
    plot_type = input("Enter plot type (short/full): ").strip().lower()

    if plot_type not in ['short', 'full']:
        print("Invalid plot type. Defaulting to 'short'.")
        plot_type = 'short'

    movie_data = search_movie(title, year, plot_type)
    if movie_data:
        print("\nMovie Details:\n")
        print_movie_details(movie_data)
    else:
        print("\nNo movie found with the given criteria.")

if __name__ == "__main__":
    main()


