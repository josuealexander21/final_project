import random

class Outfit:
    """
    Represents an outfit consisting of a single type of clothing.

    Attributes:
        clothes (str): A string describing the clothing item.
    
    Methods:
        __repr__(): Returns a string representation of the outfit.
    """
    def __init__(self, clothes: str):
        self.clothes = clothes

    def __repr__(self):
        return self.clothes

class MoodOutfitSelector:
    """
    A program that suggests outfits based on the user's mood and other contextual factors
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

        """
        Gets the user to enter their current mood.
        
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

        """ 
        Gets the user to enter the current weather condition.

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

        """
        Suggests an outfit based on mood and weather. Includes the option to boost the users mood.

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
            return random.choice(outfits)
        except KeyError:
            return "No outfit suggestions available for this combination."   
             
def main():

    print("Welcome to your personal outfit finder!")
    selector = MoodOutfitSelector()

    # this gets user inputs
    mood = selector.get_user_mood()
    weather = selector.get_weather_context()
    uplift = input("Would you like an outfit to boost your mood? (yes/no): ").lower()

    # this will uggest outfit
    outfit = selector.suggest_outfit(mood, weather, uplift)
    print(f"\nHere's your suggested outfit: {outfit}")

def remove_outfit(self, mood, weather, outfit):
        """
        Removes an outfit from the suggestion list.

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
        """
        Displays the saved outfits from the favorites file.
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
        """
        Saves the favorite outfit for later.
        
        Args:
            outfit: The outfit to save.
        """
        with open("favorite_outfits.txt", "a") as file:
            file.write(outfit + "\n")
        print(f"Outfit '{outfit}' has been saved to your favorites!")

if __name__ == "__main__":
    main()