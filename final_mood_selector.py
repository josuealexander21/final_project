import random

class MoodOutfitSelector:
    """
    A program that suggests outfits based on the user's mood and other contextual factors
    such as the weather. It provides mood-based clothing recommendations to align with
    or boost the user's emotional state.
    """

    def __init__(self):
        
        self.outfit_suggestions = {
            "happy": {
                "sunny": ["bright sundress", "colorful t-shirt and shorts", "light linen outfit"],
                "rainy": ["yellow raincoat", "jeans and waterproof boots", "cute umbrella accessory"],
                "cold": ["cheerful sweater", "wool scarf and beanie", "layered outfit with boots"],
                "hot": ["flowy summer dress", "tank top and shorts", "light pastel blouse"]
            },
            "calm": {
                "sunny": ["light blue shirt", "comfortable jeans", "soft cardigan"],
                "rainy": ["cozy hoodie", "rainproof jacket", "soft scarf"],
                "cold": ["oversized sweater", "corduroy pants", "knit beanie"],
                "hot": ["cotton jumpsuit", "linen trousers and top", "simple tank top"]
            },
            "excited": {
                "sunny": ["bright graphic tee", "denim shorts", "sneakers"],
                "rainy": ["water-resistant jacket", "fun patterned boots", "rain boots with a pop of color"],
                "cold": ["bold colored jacket", "jeans with patches", "chunky scarf"],
                "hot": ["colorful tank top", "high-waisted shorts", "floral skirt"]
            },
            "sad": {
                "sunny": ["cozy oversized sweater", "jeans", "slouchy beanie"],
                "rainy": ["long cardigan", "dark raincoat", "soft boots"],
                "cold": ["soft hoodie", "thermal leggings", "fuzzy socks"],
                "hot": ["loose, comfortable t-shirt", "simple skirt", "casual sandals"]
            },
            "anxious": {
                "sunny": ["relaxed hoodie", "baggy pants", "slip-on sneakers"],
                "rainy": ["windbreaker jacket", "athletic shoes", "soft scarf"],
                "cold": ["oversized puffer jacket", "comfy leggings", "fleece-lined gloves"],
                "hot": ["loose-fitting blouse", "linen shorts", "comfortable sneakers"]
            },
            "confident": {
                "sunny": ["sharp blazer", "tailored pants", "sleek boots"],
                "rainy": ["stylish trench coat", "high heels", "elegant scarf"],
                "cold": ["fitted wool coat", "smart trousers", "leather gloves"],
                "hot": ["vibrant dress", "strappy sandals", "sun hat"]
            },
            "nervous": {
                "sunny": ["casual button-up shirt", "comfortable shorts", "casual loafers"],
                "rainy": ["simple rain jacket", "comfortable boots", "beanie"],
                "cold": ["fleece zip-up jacket", "jeans", "scarf"],
                "hot": ["loose t-shirt", "denim skirt", "sandals"]
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