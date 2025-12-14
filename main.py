import pdfplumber
import nltk
from collections import defaultdict

# --- Configuration for Word Filtering ---
EXCLUDE_POS_PREFIXES = ('DT', 'VB') # DT (Determiners/Articles) and VB tags (Verbs)
CHAPTER_DELIMITER = "Chapter" 

# Final corrected function in main.py
def check_and_download_nltk_data():
    """
    Checks if necessary NLTK data is present and downloads it if missing.
    Ensures robustness by handling LookupError for missing resources.
    """
    # These are the correct resources for tokenizing and POS tagging
    required_packages = ['punkt', 'averaged_perceptron_tagger']
    
    print("Checking NLTK data dependencies...")
    for package in required_packages:
        try:
            # The standard way to check if NLTK data is installed
            nltk.data.find(package)
            print(f"✅ NLTK package '{package}' found.")
        except LookupError:
            print(f"⚠️ NLTK package '{package}' not found. Downloading...")
            try:
                # Attempt to download the specific package
                nltk.download(package, quiet=True)
                print(f"✅ NLTK package '{package}' downloaded successfully.")
            except Exception as e:
                # Catch any error during download
                print(f"❌ Error downloading NLTK package '{package}': {e}")
                # Re-raise the error to stop execution if essential data cannot be downloaded
                raise

def filter_and_count_words(text: str) -> tuple[int, int, dict]:
    """
    Tokenizes text, performs POS tagging, excludes articles/verbs, 
    and returns total count, excluded count, and a dict of counted words.
    """
    if not text:
        return 0, 0, {}

    # Tokenize the text into individual words
    tokens = nltk.word_tokenize(text)
    
    # Filter out non-alphabetic tokens (punctuation, numbers)
    clean_tokens = [word.lower() for word in tokens if word.isalpha()]
    
    # Perform Part-of-Speech (POS) Tagging
    tagged_words = nltk.pos_tag(clean_tokens)
    
    total_words = len(clean_tokens)
    excluded_count = 0
    word_counts = defaultdict(int)

    for word, tag in tagged_words:
        # Check if the POS tag starts with an exclusion prefix (DT for Articles, VB for Verbs)
        if tag.startswith(EXCLUDE_POS_PREFIXES):
            excluded_count += 1
        else:
            word_counts[word] += 1
    
    # Total counted words (non-excluded)
    counted_words = sum(word_counts.values())

    return total_words, excluded_count, dict(word_counts)

def analyze_pdf_by_chapter(pdf_path: str) -> dict:
    """
    Reads a PDF, splits its text based on a delimiter, and analyzes each section.
    Returns a dictionary of results per chapter.
    """
    # --- STEP 1: Ensure NLTK Data is Ready ---
    check_and_download_nltk_data()
    
    analysis_results = {}
    full_text = ""

    try:
        with pdfplumber.open(pdf_path) as pdf:
            print(f"Extracting text from {len(pdf.pages)} pages...")
            # 2. Extract all text from the PDF
            for page in pdf.pages:
                full_text += page.extract_text() + "\n"
    except Exception as e:
        # Handle file errors
        return {"error": f"Error reading PDF: {e}"}

    # 3. Split the text into chapters
    chapters = full_text.split(CHAPTER_DELIMITER)
    
    for i, chapter_text in enumerate(chapters):
        if not chapter_text.strip():
            continue

        # Use the delimiter and index for a chapter name
        chapter_name = f"{CHAPTER_DELIMITER} {i}" if i > 0 else "Introduction/Preface"
        
        # 4. Analyze the chapter text
        total, excluded, counts = filter_and_count_words(chapter_text)

        analysis_results[chapter_name] = {
            "total_words": total,
            "excluded_words": excluded,
            "counted_words_total": total - excluded,
            "top_words": sorted(counts.items(), key=lambda item: item[1], reverse=True)[:10] # Top 10 words
        }

    return {"success": analysis_results}

# --- Example Usage (for testing the backend logic) ---

if __name__ == '__main__':
    # REPLACE 'your_document.pdf' with a path to a test PDF file
    test_file_path = "The Biome.pdf" 
    
    # --- IMPORTANT ---
    # Remember to place a temporary PDF file named 'sample_book.pdf' 
    # in the same directory for local testing, or change the path above.
    # ---

    print(f"Starting analysis of: {test_file_path}\n")
    results = analyze_pdf_by_chapter(test_file_path)

    if "success" in results:
        print("\n--- Analysis Results Summary ---")
        for chapter, data in results["success"].items():
            print(f"\n--- {chapter} ---")
            print(f"Total Tokens: {data['total_words']}")
            print(f"Excluded (Articles/Verbs): {data['excluded_words']}")
            print(f"Final Counted Words: **{data['counted_words_total']}**")
            print(f"Top 10 Counted Words (Word: Count): {data['top_words']}")
    else:
        print(f"\nAnalysis Failed: {results['error']}")