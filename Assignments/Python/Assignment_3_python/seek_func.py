
with open("sample.txt", "w") as f:
    f.write("Hello, My name is Sinjal Dahal.\nWe are becoming lazy.")

with open("sample.txt", "r") as f:
    print("Reading full file:")
    print(f.read())

    # Move file pointer to the beginning
    f.seek(0)
    print("\nAfter seek(0):")
    print(f.read(5))  # Read first 5 characters

    # Move pointer to position 18 
    f.seek(18)
    print("\nAfter seek(18):")
    print(f.read(6))  
