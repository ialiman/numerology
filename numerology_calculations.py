def calculate_soul_urge(full_name):
    """
    Calculate the Soul Urge (Heart's Desire) number from a full name.
    Uses only the vowels in the name.
    
    Args:
        full_name (str): Full birth name (first, middle, last)
        
    Returns:
        tuple: (final_number, calculation_details)
    """
    
    # Pythagorean numerology chart
    letter_values = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
        'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
        'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8
    }
    
    # Define vowels (Y is handled specially)
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    def is_vowel(char, word, index):
        """
        Determine if a character is a vowel.
        Y is considered a vowel when it sounds like a vowel.
        """
        char = char.upper()
        if char in vowels:
            return True
        # Y is a vowel if it's not preceded by another vowel
        # Simple rule: Y is vowel if previous char is not a vowel
        if char == 'Y':
            if index == 0:  # Y at beginning acts as consonant
                return False
            prev_char = word[index - 1].upper()
            # Y is vowel if previous letter is a consonant
            return prev_char not in vowels
        return False
    
    def reduce_to_single_digit(number):
        """Reduce a number to single digit or master number (11, 22, 33)."""
        while number > 9 and number not in [11, 22, 33]:
            number = sum(int(digit) for digit in str(number))
        return number
    
    # Split name into parts
    name_parts = full_name.strip().split()
    
    if not name_parts:
        return 0, "Invalid name provided"
    
    # Calculate for each name part
    reduced_name_totals = []
    details = []
    
    for name in name_parts:
        vowel_sum = 0
        vowel_letters = []
        
        for i, char in enumerate(name):
            if char.isalpha() and is_vowel(char, name, i):
                value = letter_values[char.upper()]
                vowel_sum += value
                vowel_letters.append(f"{char.upper()}={value}")
        
        if vowel_letters:
            # Show the calculation for this name
            calculation_str = f"{name}: {' + '.join(vowel_letters)} = {vowel_sum}"
            
            # Reduce this name's total to single digit or master number
            reduced_value = reduce_to_single_digit(vowel_sum)
            
            # Show reduction if it occurred
            if reduced_value != vowel_sum:
                calculation_str += f" => {reduced_value}"
            
            details.append(calculation_str)
            reduced_name_totals.append(reduced_value)
        else:
            details.append(f"{name}: No vowels")
    
    # Add all reduced name totals together
    total = sum(reduced_name_totals)
    details.append(f"\nTotal: {' + '.join(map(str, reduced_name_totals))} = {total}")
    
    # Reduce to single digit or master number
    final_number = reduce_to_single_digit(total)
    
    if final_number != total:
        details.append(f"Final Reduction: {total} => {final_number}")
    
    return final_number, "\n".join(details)


# Test the function
if __name__ == "__main__":
    # Example 1: Ian Dubin Aliman
    print("Example 1: Ian Dubin Aliman")
    print("=" * 50)
    soul_urge, calculation = calculate_soul_urge("Ian Dubin Aliman")
    print(calculation)
    print(f"\nSoul Urge Number: {soul_urge}")
    print()
    
    # Example 2: Thomas John Hancock
    print("\nExample 2: Thomas John Hancock")
    print("=" * 50)
    soul_urge, calculation = calculate_soul_urge("Thomas John Hancock")
    print(calculation)
    print(f"\nSoul Urge Number: {soul_urge}")
    print()
    
    # Example 3: Michael Joseph Jackson
    print("\nExample 3: Michael Joseph Jackson")
    print("=" * 50)
    soul_urge, calculation = calculate_soul_urge("Michael Joseph Jackson")
    print(calculation)
    print(f"\nSoul Urge Number: {soul_urge}")
    print()
    
    # Example 4: Mary Jane Smith
    print("\nExample 4: Mary Jane Smith")
    print("=" * 50)
    soul_urge, calculation = calculate_soul_urge("Mary Jane Smith")
    print(calculation)
    print(f"\nSoul Urge Number: {soul_urge}")
    print()
    
    # Interactive mode
    print("\n" + "=" * 50)
    print("Calculate your own Soul Urge Number")
    print("=" * 50)
    user_name = input("Enter your full birth name: ")
    soul_urge, calculation = calculate_soul_urge(user_name)
    print("\nCalculation:")
    print(calculation)
    print(f"\n✨ Your Soul Urge Number is: {soul_urge} ✨")

    