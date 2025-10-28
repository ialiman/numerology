def calculate_name_numerology(full_name):
    """
    Calculate all name-based numerology numbers.
    
    Args:
        full_name (str): Full birth name (first, middle, last)
        
    Returns:
        dict: Dictionary containing all calculated numbers and their details
    """
    
    # Pythagorean numerology chart
    letter_values = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
        'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
        'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8
    }
    
    # Define vowels
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    def is_vowel(char, word, index):
        """Determine if a character is a vowel."""
        char = char.upper()
        if char in vowels:
            return True
        # Y is a vowel if it's not preceded by another vowel
        if char == 'Y':
            if index == 0:
                return False
            prev_char = word[index - 1].upper()
            return prev_char not in vowels
        return False
    
    def is_consonant(char, word, index):
        """Determine if a character is a consonant."""
        char = char.upper()
        if char in vowels:
            return False
        # Y is a consonant if it's at the beginning or preceded by a vowel
        if char == 'Y':
            if index == 0:
                return True
            prev_char = word[index - 1].upper()
            return prev_char in vowels
        return True
    
    def reduce_to_single_digit(number):
        """Reduce a number to single digit or master number (11, 22, 33)."""
        while number > 9 and number not in [11, 22, 33]:
            number = sum(int(digit) for digit in str(number))
        return number
    
    def calculate_soul_urge():
        """Calculate Soul Urge number from vowels."""
        name_parts = full_name.strip().split()
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
                calculation_str = f"{name}: {' + '.join(vowel_letters)} = {vowel_sum}"
                reduced_value = reduce_to_single_digit(vowel_sum)
                
                if reduced_value != vowel_sum:
                    calculation_str += f" => {reduced_value}"
                
                details.append(calculation_str)
                reduced_name_totals.append(reduced_value)
            else:
                details.append(f"{name}: No vowels")
        
        total = sum(reduced_name_totals)
        details.append(f"\nTotal: {' + '.join(map(str, reduced_name_totals))} = {total}")
        
        final_number = reduce_to_single_digit(total)
        
        if final_number != total:
            details.append(f"Final Reduction: {total} => {final_number}")
        
        return final_number, "\n".join(details)
    
    def calculate_personality():
        """Calculate Personality number from consonants."""
        name_parts = full_name.strip().split()
        reduced_name_totals = []
        details = []
        
        for name in name_parts:
            consonant_sum = 0
            consonant_letters = []
            
            for i, char in enumerate(name):
                if char.isalpha() and is_consonant(char, name, i):
                    value = letter_values[char.upper()]
                    consonant_sum += value
                    consonant_letters.append(f"{char.upper()}={value}")
            
            if consonant_letters:
                calculation_str = f"{name}: {' + '.join(consonant_letters)} = {consonant_sum}"
                reduced_value = reduce_to_single_digit(consonant_sum)
                
                if reduced_value != consonant_sum:
                    calculation_str += f" => {reduced_value}"
                
                details.append(calculation_str)
                reduced_name_totals.append(reduced_value)
            else:
                details.append(f"{name}: No consonants")
        
        total = sum(reduced_name_totals)
        details.append(f"\nTotal: {' + '.join(map(str, reduced_name_totals))} = {total}")
        
        final_number = reduce_to_single_digit(total)
        
        if final_number != total:
            details.append(f"Final Reduction: {total} => {final_number}")
        
        return final_number, "\n".join(details)
    
    def calculate_expression():
        """Calculate Expression number from all letters."""
        name_parts = full_name.strip().split()
        reduced_name_totals = []
        details = []
        
        for name in name_parts:
            letter_sum = 0
            letter_list = []
            
            for char in name:
                if char.isalpha():
                    value = letter_values[char.upper()]
                    letter_sum += value
                    letter_list.append(f"{char.upper()}={value}")
            
            if letter_list:
                calculation_str = f"{name}: {' + '.join(letter_list)} = {letter_sum}"
                reduced_value = reduce_to_single_digit(letter_sum)
                
                if reduced_value != letter_sum:
                    calculation_str += f" => {reduced_value}"
                
                details.append(calculation_str)
                reduced_name_totals.append(reduced_value)
            else:
                details.append(f"{name}: No letters")
        
        total = sum(reduced_name_totals)
        details.append(f"\nTotal: {' + '.join(map(str, reduced_name_totals))} = {total}")
        
        final_number = reduce_to_single_digit(total)
        
        if final_number != total:
            details.append(f"Final Reduction: {total} => {final_number}")
        
        return final_number, "\n".join(details)
    
    # Calculate all numbers
    soul_urge_num, soul_urge_calc = calculate_soul_urge()
    personality_num, personality_calc = calculate_personality()
    expression_num, expression_calc = calculate_expression()
    
    return {
        'soul_urge': {
            'number': soul_urge_num,
            'calculation': soul_urge_calc
        },
        'appearance': {
            'number': personality_num,
            'calculation': personality_calc
        },
        'expression': {
            'number': expression_num,
            'calculation': expression_calc
        }
    }


def display_name_group(full_name):
    """Display all NAME GROUP calculations in a formatted way."""
    
    print("=" * 70)
    print(f"NAME GROUP NUMEROLOGY CALCULATIONS")
    print("=" * 70)
    print(f"Name: {full_name}")
    print("=" * 70)
    
    # Calculate all numbers
    results = calculate_name_numerology(full_name)
    
    # Display Soul Urge
    print("\n1. SOUL URGE (Heart's Desire)")
    print("-" * 70)
    print("Uses: VOWELS from full birth name")
    print()
    print(results['soul_urge']['calculation'])
    print(f"\n✨ Soul Urge Number: {results['soul_urge']['number']}")
    
    # Display Appearance (Personality)
    print("\n\n2. APPEARANCE (Personality)")
    print("-" * 70)
    print("Uses: CONSONANTS from full birth name")
    print()
    print(results['appearance']['calculation'])
    print(f"\n✨ Appearance Number: {results['appearance']['number']}")
    
    # Display Expression (Destiny)
    print("\n\n3. EXPRESSION (Destiny)")
    print("-" * 70)
    print("Uses: ALL LETTERS from full birth name")
    print()
    print(results['expression']['calculation'])
    print(f"\n✨ Expression Number: {results['expression']['number']}")
    
    # Summary
    print("\n\n" + "=" * 70)
    print("SUMMARY - NAME GROUP")
    print("=" * 70)
    print(f"1. Soul Urge:    {results['soul_urge']['number']}")
    print(f"2. Appearance:   {results['appearance']['number']}")
    print(f"3. Expression:   {results['expression']['number']}")
    print("=" * 70)
    
    return results


# Main program
if __name__ == "__main__":
    # Test example
    print("\n*** EXAMPLE CALCULATION ***\n")
    test_results = display_name_group("Ian Dubin Aliman")
    
    # Interactive mode
    print("\n\n\n*** CALCULATE YOUR OWN NAME GROUP ***\n")
    
    user_name = input("Enter your full birth name: ")
    
    print("\n")
    user_results = display_name_group(user_name)

    