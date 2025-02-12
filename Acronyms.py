def generate_acronym(pharse):
    words=pharse.split()
    acronym = "".join(word(0).upper() for word in words if word.isalpha())
    return acronym

def main():
    print("Welcome to the Acronym creator!")
    
    while True:
        pharse = input("\nEnter a pharse to generate its acronym:").strip()
        acronym = generate_acronym(pharse)
        print(f"The acronym for '{pharse}' is: {acronym}")
        choice = input("\nDo you want to generate another acronym? (y/n):").strip().lower()
        if choice != 'y':
            print("\nThank you for using the Acronym creator.")
            break

if __name__ == "__main__":
    main()