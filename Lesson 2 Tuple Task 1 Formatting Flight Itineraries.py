def format_itineraries(itineraries):
    # Initialize an empty string to store the formatted itineraries
    formatted_itineraries = ""
    
    # Iterate over the list of tuples
    for i, itinerary in enumerate(itineraries, start=1):
        # Unpack the tuple
        traveler_name, origin, destination = itinerary
        
        # Format the itinerary string
        itinerary_str = f"Itinerary {i}: {traveler_name} - From {origin} to {destination}\n"
        
        # Add the formatted itinerary to the result string
        formatted_itineraries += itinerary_str
    
    # Return the formatted itineraries
    return formatted_itineraries

# Example usage:
itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
formatted_output = format_itineraries(itineraries)
print(formatted_output)
