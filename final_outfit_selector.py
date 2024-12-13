import random
from PIL import Image
import os

class Outfit:
    """
    Represents an outfit consisting of a single type of clothing.

    Attributes:
        clothes (str): A string describing the clothing item.
    
    Methods:
        __repr__(): Returns a string representation of the outfit.
        show_image(): Displays the outfit image if available.
    """
    def __init__(self, clothes: str):
        self.clothes = clothes

    def __repr__(self):
        return self.clothes


class MoodOutfitSelector:
    """ A program that suggests outfits based on the user's mood and other contextual factors
    such as the weather. It provides mood-based clothing recommendations to align with
    or boost the user's emotional state.
    
    """

    def __init__(self):
        
        self.outfit_suggestions = {
            "happy": {
                "sunny": [Outfit("bright sundress"), Outfit("colorful t-shirt and shorts"), Outfit("light linen outfit")],
                "rainy": [Outfit("yellow raincoat"), Outfit("jeans and waterproof boots"), Outfit("cute umbrella accessory")],
                "cold": [Outfit("cheerful sweater"), Outfit("wool scarf and beanie"), Outfit("layered outfit with boots")],
                "hot": [Outfit("flowy summer dress"), Outfit("tank top and shorts"), Outfit("light pastel blouse")]
            },
            "calm": {
                "sunny": [Outfit("light blue shirt"), Outfit("comfortable jeans"), Outfit("soft cardigan")],
                "rainy": [Outfit("cozy hoodie"), Outfit("rainproof jacket"), Outfit("soft scarf")],
                "cold": [Outfit("oversized sweater"), Outfit("corduroy pants"), Outfit("knit beanie")],
                "hot": [Outfit("cotton jumpsuit"), Outfit("linen trousers and top"), Outfit("simple tank top")]
            },
            "excited": {
                "sunny": [Outfit("bright graphic tee"), Outfit("denim shorts"), Outfit("sneakers")],
                "rainy": [Outfit("water-resistant jacket"), Outfit("fun patterned boots"), Outfit("rain boots with a pop of color")],
                "cold": [Outfit("bold colored jacket"), Outfit("jeans with patches"), Outfit("chunky scarf")],
                "hot": [Outfit("colorful tank top"), Outfit("high-waisted shorts"), Outfit("floral skirt")]
            },
            "sad": {
                "sunny": [Outfit("cozy oversized sweater"), Outfit("jeans"), Outfit("slouchy beanie")],
                "rainy": [Outfit("long cardigan"), Outfit("dark raincoat"), Outfit("soft boots")],
                "cold": [Outfit("soft hoodie"), Outfit("thermal leggings"), Outfit("fuzzy socks")],
                "hot": [Outfit("loose, comfortable t-shirt"), Outfit("simple skirt"), Outfit("casual sandals")]
            },
            "anxious": {
                "sunny": [Outfit("relaxed hoodie"), Outfit("baggy pants"), Outfit("slip-on sneakers")],
                "rainy": [Outfit("windbreaker jacket"), Outfit("athletic shoes"), Outfit("soft scarf")],
                "cold": [Outfit("oversized puffer jacket"), Outfit("comfy leggings"), Outfit("fleece-lined gloves")],
                "hot": [Outfit("loose-fitting blouse"), Outfit("linen shorts"), Outfit("comfortable sneakers")]
            },
            "confident": {
                "sunny": [Outfit("sharp blazer"), Outfit("tailored pants"), Outfit("sleek boots")],
                "rainy": [Outfit("stylish trench coat"), Outfit("high heels"), Outfit("elegant scarf")],
                "cold": [Outfit("fitted wool coat"), Outfit("smart trousers"), Outfit("leather gloves")],
                "hot": [Outfit("vibrant dress"), Outfit("strappy sandals"), Outfit("sun hat")]
            },
            "nervous": {
                "sunny": [Outfit("casual button-up shirt"), Outfit("comfortable shorts"), Outfit("casual loafers")],
                "rainy": [Outfit("simple rain jacket"), Outfit("comfortable boots"), Outfit("beanie")],
                "cold": [Outfit("fleece zip-up jacket"), Outfit("jeans"), Outfit("scarf")],
                "hot": [Outfit("loose t-shirt"), Outfit("denim skirt"), Outfit("sandals")]
            }
        
        }

    def get_user_mood(self):

        """ Gets the user to enter their current mood.
        
        Returns:
            str: The mood input by the user (e.g., "happy", "calm").
        
        Raises:
            ValueError: If the user enters an invalid mood that is not recognized.
        """
        moods = list(self.outfit_suggestions.keys())
        mood = input(f"How are you feeling today? ({', '.join(moods)}): ").lower()
        while mood not in moods:
            print(f"Please enter a valid mood: {', '.join(moods)}.")
            mood = input(f"How are you feeling today? ({', '.join(moods)}): ").lower()
        return mood

    def get_weather_context(self):

        """ Gets the user to enter the current weather condition.

        Returns:
            str: The weather condition input by the user (e.g., "sunny", "rainy").
        """
        weather_conditions = ["sunny", "rainy", "cold", "hot"]
        weather = input(f"What's the weather like today? ({', '.join(weather_conditions)}): ").lower()
        while weather not in weather_conditions:
            print(f"Please enter a valid weather condition: {', '.join(weather_conditions)}.")
            weather = input(f"What's the weather like today? ({', '.join(weather_conditions)}): ").lower()
        return weather

    def suggest_outfit(self, mood, weather, uplift):

        """ Suggests an outfit based on mood and weather. Includes the option to boost the users mood.

        Args:
            mood (str): The user's mood.
            weather (str): The current weather condition.
            uplift (str): "yes" to boost the mood, "no" to stay aligned with the mood.

        Returns:
            str: A randomly selected outfit suggestion.
        """
        if uplift == "yes":
            mood = "happy"  # Boost mood by suggesting a 'happy' outfit

        try:
            outfits = self.outfit_suggestions[mood][weather]
            selected_outfit = random.choice(outfits)
            return selected_outfit
        except KeyError:
            return "No outfit suggestions available for this combination."   
        
    def load_outfit_images(self, outfit):
        """ Loads an image for the outfit based on its description.
        
        Args:
            outfit (str): The outfit that needs an image displayed for it

        Returns:
            str: The filename or path to the image.
        """
        outfit_images = {
            "bright sundress": "1.jpg", "colorful t-shirt and shorts": "2.jpg", "light linen outfit": "3.jpg",
            "yellow raincoat":  "4.jpg", "jeans and waterproof boots": "5.jpg", "cute umbrella accessory": "6.jpg",
            "cheerful sweater": "7.jpg", "wool scarf and beanie": "8.jpg", "layered outfit with boots": "9.jpg",
            "flowy summer dress": "10.jpg","tank top and shorts": "11.jpg", "light pastel blouse": "12.jpg",
            "light blue shirt": "13.jpg", "comfortable jeans": "14.jpg", "soft cardigan": "15.jpg",
            "cozy hoodie": "16.jpg", "rainproof jacket": "17.jpg", "soft scarf": "18.jpg",
            "oversized sweater": "19.jpg","corduroy pants": "20.jpg", "knit beanie": "21.jpg",
            "cotton jumpsuit": "22.jpg", "linen trousers and top":"23.jpg", "simple tank top":"24.jpg",
            "bright graphic tee": "25.jpg", "denim shorts": "26.jpg", "sneakers": "27.jpg",
            "water-resistant jacket": "28.jpg", "fun patterned boots": "29.jpg", "rain boots with a pop of color": "30.jpg",
            "bold colored jacket": "31.jpg", "jeans with patches": "32.jpg", "chunky scarf": "33.jpg",
            "colorful tank top": "34.jpg", "high-waisted shorts": "35.jpg", "floral skirt": "36.jpg",
            "cozy oversized sweater": "37.jpg", "jeans": "38.jpg","slouchy beanie": "39.jpg",
            "long cardigan":"40.jpg", "dark raincoat": "41.jpg", "soft boots": "42.jpg",
            "soft hoodie": "43.jpg", "thermal leggings": "44.jpg", "fuzzy socks": "45.jpg",
            "loose, comfortable t-shirt": "46.jpg", "simple skirt": "47.jpg", "casual sandals": "48.jpg",
            "relaxed hoodie": "49.jpg", "baggy pants": "50.jpg", "slip-on sneakers": "51.jpg",
            "windbreaker jacket": "52.jpg", "athletic shoes": "53.jpg", "soft scarf": "54.jpg",
            "oversized puffer jacket": "55.jpg", "comfy leggings": "56.jpg", "fleece-lined gloves": "57.jpg",
            "loose-fitting blouse": "58.jpg", "linen shorts": "59.jpg", "comfortable sneakers": "60.jpg",
            "sharp blazer": "61.jpg", "tailored pants": "62.jpg", "sleek boots": "63.jpg",
            "stylish trench coat": "64.jpg", "high heels": "65.jpg", "elegant scarf": "66.jpg",
            "fitted wool coat": "67.jpg", "smart trousers": "68.jpg", "leather gloves": "69.jpg",
            "vibrant dress": "70.jpg", "strappy sandals": "71.jpg", "sun hat": "72.jpg",
            "casual button-up shirt": "73.jpg", "comfortable shorts": "74.jpg", "casual loafers": "75.jpg",
            "simple rain jacket": "76.jpg", "comfortable boots": "77.jpg", "beanie": "78.jpg",
            "fleece zip-up jacket": "79.jpg", "jeans": "80.jpg", "scarf": "81.jpg",
            "loose t-shirt": "82.jpg", "denim skirt": "83.jpg", "sandals": "84.jpg",
            }

        outfit_name = str(outfit)
        image_file = outfit_images.get(outfit_name)

        if not image_file:
            return "Image not available"

        image_path = os.path.join("images", image_file)

        if not os.path.exists(image_path):
            return f"Image file '{image_file}' does not exist in the folder 'images'."

        user_input = input(f"Would you like to view the image for '{outfit_name}'? (yes/no): ").strip().lower()

        if user_input == "yes":
            try:
                img = Image.open(image_path)
                img.show()  # Opens the image in the default viewer
                return f"Image '{image_file}' displayed."
            except Exception as e:
                return f"An error occurred while opening the image: {e}"
        else:
            return "Image viewing skipped."
        
    def search_outfit_in_favorites(self, search_term):
        """ Search for an outfit in the favorites file based on a search term.
        
        Args:
            search_term (str): The term to search for in the favorites file.
        
        Returns:
            list: A list of matching outfits.
        """
        try:
            with open("favorite_outfits.txt", "r") as file:
                favorites = file.readlines()
            matches = [outfit.strip() for outfit in favorites if search_term.lower() in outfit.lower()]
            return matches
        except FileNotFoundError:
            print("No favorites file found. You need to save outfits first!")
            return [] 

    def remove_outfit(self, mood, weather, outfit):
        """ Removes an outfit from the suggestion list.

        Args:
            mood: The mood category of the outfit.
            weather: The weather category of the outfit.
            outfit: The outfit description to remove.
        """
        try:
            self.outfit_suggestions[mood][weather].remove(outfit)
            print(f"Outfit '{outfit}' has been removed from {mood} mood and {weather} weather.")
        except (KeyError, ValueError):
            print("Outfit not found or invalid mood/weather category.")

    def view_saved_outfits(self):
        """ Displays the saved outfits from the favorites file.

        """
        try:
            with open("favorite_outfits.txt", "r") as file:
                saved_outfits = file.readlines()
            if saved_outfits:
                print("\nYour favorite outfits:")
                for i, outfit in enumerate(saved_outfits, start=1):
                    print(f"{i}. {outfit.strip()}")
            else:
                print("\nNo saved outfits yet!")
        except FileNotFoundError:
            print("\nNo saved outfits yet!")

    def save_outfit(self, outfit):
        """ Saves the favorite outfit for later.
        
        Args:
            outfit: The outfit to save.
        """
        with open("favorite_outfits.txt", "a") as file:
            file.write(str(outfit) + "\n")  # Use str() to convert Outfit object to a string
        print(f"Outfit '{outfit}' has been saved to your favorites!")
             
def main():
    """ Asks questions to user for what outfit they want 
        
        Args:
            none.
        """

    print("Welcome to your personal outfit finder!")
    selector = MoodOutfitSelector()

    while True:
        # User chooses an action
        action = input("\nWhat would you like to do? (suggest/search/quit): ").lower()
        if action == "suggest":
            mood = selector.get_user_mood()
            weather = selector.get_weather_context()
            uplift = input("Would you like an outfit to boost your mood? (yes/no): ").lower()

            outfit = selector.suggest_outfit(mood, weather, uplift)
            print(f"\nHere's your suggested outfit: {outfit}")

            view_image = input("Would you like to see an image of this outfit? (yes/no): ").lower()
            if view_image == "yes":
                image_path = selector.load_outfit_images(outfit)
                print(f"Here is your outfit image: {image_path}")

            save = input("Would you like to save this outfit to your favorites? (yes/no): ").lower()
            if save == "yes":
                selector.save_outfit(outfit)

        elif action == "search":
            search_term = input("Enter an outfit or keyword to search for in your favorites: ")
            matches = selector.search_outfit_in_favorites(search_term)
            if matches:
                print(f"Matching outfits found:\n" + "\n".join(matches))
            else:
                print("No matching outfits found in your favorites.")

        elif action == "quit":
            print("Thank you for using the Mood Outfit Selector! Goodbye!")
            break

        else:
            print("Invalid option. Please choose 'suggest', 'search', or 'quit'.")



if __name__ == "__main__":
    main()