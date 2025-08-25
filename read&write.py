def process_file():
    filename = input("Enter the filename you want to read: ")

    try:
        # Step 1: Read the file
        with open(filename, "r") as f:
            content = f.read()

        print("\n📄 Original File Content:")
        print(content)

        # Step 2: Modify the content (example: uppercase)
        modified_content = content.upper()

        # Step 3: Write modified content to new file
        output_file = "modified_" + filename
        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"\n✅ Modified content written to {output_file}")

    except FileNotFoundError:
        print("❌ File not found. Please check the filename.")
    except PermissionError:
        print("❌ You don’t have permission to access this file.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


# Run the program
process_file()